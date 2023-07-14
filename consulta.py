import csv
import requests
import time
from bs4 import BeautifulSoup
from datetime import datetime


def query_url(url):
    response = requests.get(url)
    # Process the response as per your requirements
    if (response.status_code != 200):
        print("Error al descargar informacion, no se cargo correctamente la pagina")
    data = response.text  # Assuming the response is in text format
    return data

def rate_limited_query(url, requests_per_minute):
    delay = 60 / requests_per_minute  # Delay between each request in seconds
    with open('input.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            print("Descargando informacion de: " + row[0])
            nro_cic = row[0]  # Assuming nro_cic is in the first column
            query_url_with_params = f'{url}?nro_cic={nro_cic}&envio=ok&bandera=1'
            start_time = time.time()
            data = query_url(query_url_with_params)
            end_time = time.time()

            # Process the data or do whatever you need to do
            row = getRow(data) 
            if(row == None or len(row) == 0):
                row = [nro_cic,'','','','','','','','','','','','','']
            row.insert(0,query_url_with_params)
            writeRow(row)

            elapsed_time = end_time - start_time
            if elapsed_time < delay:
                time.sleep(delay - elapsed_time)

def writeRow(row):
    with open(OUTPUT_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(row)

def writeHeader():
    with open(OUTPUT_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["URL","CI","Nombre","Apellido","Fecha de nacimiento","Sexo","Tipo Aseg.","Beneficiarios Activos","Enrolado","Vencimiento de fe de vida","Nro. Patronal","Empleador","Estado","Meses de aporte","Vencimiento","Ultimo Periodo Abonado"])

def getRow(html):
    soup = BeautifulSoup(html, 'html.parser')

    # Find the tables by their common attributes (class or id)
    tables = soup.find_all('table')

    rowsAll = []
    # Print the tables
    for table in tables:
        rows = table.find_all('tr')
        for row in rows:
            rowsAll.append(row)
    rowsAll = rowsAll[1:]
    cellsAll = []
    for row in rowsAll:
        cells = row.find_all('td')
        for cell in cells:
            if(cell.text.strip() != 'Nro Documento:'):
                cellsAll.append(cell.text.strip())
    # Remueve los espacios extras al principio
    return cellsAll[3:]

if __name__ == '__main__':
    url = 'https://servicios.ips.gov.py/consulta_asegurado/comprobacion_de_derecho_externo.php'
    requests_per_minute = 10  # Adjust this value as per your rate limit
    current_time = datetime.now().strftime("%Y-%m-%dT%H_%M_%S%z")
    OUTPUT_FILE=f"{current_time}.csv" 
    print("NO CERRAR ESTA VENTANA PARA QUE TERMINE DE DESCARGAR DATOS")
    print("Iniciando actualizacion de datos, leyendo input.csv")
    writeHeader()
    rate_limited_query(url, requests_per_minute)
    print("Trabajo terminado, output en: " + OUTPUT_FILE)
    input("Presione cualquier tecla para cerrar esta ventana.")