from bs4 import BeautifulSoup
from consulta import getRow
html = """
 <html><script type="text/javascript">
    var spector;
    var captureOnLoad = false;
    var captureOffScreen = false;
    window.__SPECTOR_Canvases = [];

    (function() {
        var __SPECTOR_Origin_EXTENSION_GetContext = HTMLCanvasElement.prototype.getContext;
        HTMLCanvasElement.prototype.__SPECTOR_Origin_EXTENSION_GetContext = __SPECTOR_Origin_EXTENSION_GetContext;

        if (typeof OffscreenCanvas !== 'undefined') {
            var __SPECTOR_Origin_EXTENSION_OffscreenGetContext = OffscreenCanvas.prototype.getContext;
            OffscreenCanvas.prototype.__SPECTOR_Origin_EXTENSION_OffscreenGetContext = __SPECTOR_Origin_EXTENSION_OffscreenGetContext;

            OffscreenCanvas.prototype.getContext = function () {
                var context = null;
                if (!arguments.length) {
                    return context;
                }
    
                if (arguments.length === 1) {
                    context = this.__SPECTOR_Origin_EXTENSION_OffscreenGetContext(arguments[0]);
                    if (context === null) {
                        return context;
                    }
                }
                else if (arguments.length === 2) {
                    context = this.__SPECTOR_Origin_EXTENSION_OffscreenGetContext(arguments[0], arguments[1]);
                    if (context === null) {
                        return context;
                    }
                }
    
                var contextNames = ["webgl", "experimental-webgl", "webgl2", "experimental-webgl2"];
                if (contextNames.indexOf(arguments[0]) !== -1) {
                    // context.canvas.setAttribute("__spector_context_type", arguments[0]);
                    // Notify the page a canvas is available.
                    var myEvent = new CustomEvent("SpectorWebGLCanvasAvailableEvent");
                    document.dispatchEvent(myEvent);
                    this.id = "Offscreen";
                    window.__SPECTOR_Canvases.push(this);
    
                    if (captureOnLoad) {
                        // Ensures canvas is in the dom to capture the one we are currently tracking.
                        if (false) {
                            spector.captureContext(context, 500, false, false);
                            captureOnLoad = false;
                        }
                    }
                }
    
                return context;
            }
        }

        HTMLCanvasElement.prototype.getContext = function () {
            var context = null;
            if (!arguments.length) {
                return context;
            }

            if (arguments.length === 1) {
                context = this.__SPECTOR_Origin_EXTENSION_GetContext(arguments[0]);
                if (context === null) {
                    return context;
                }
            }
            else if (arguments.length === 2) {
                context = this.__SPECTOR_Origin_EXTENSION_GetContext(arguments[0], arguments[1]);
                if (context === null) {
                    return context;
                }
            }

            var contextNames = ["webgl", "experimental-webgl", "webgl2", "experimental-webgl2"];
            if (contextNames.indexOf(arguments[0]) !== -1) {
                context.canvas.setAttribute("__spector_context_type", arguments[0]);
                // Notify the page a canvas is available.
                var myEvent = new CustomEvent("SpectorWebGLCanvasAvailableEvent");
                document.dispatchEvent(myEvent);

                if (captureOffScreen) {
                    var found = false;
                    for (var i = 0; i < window.__SPECTOR_Canvases.length; i++) {
                        if (window.__SPECTOR_Canvases[i] === this) {
                            found = true;
                            break;
                        }
                    }
                    if (!found) {
                        window.__SPECTOR_Canvases.push(this);
                    }
                }

                if (captureOnLoad) {
                    // Ensures canvas is in the dom to capture the one we are currently tracking.
                    if (this.parentElement || false) {
                        spector.captureContext(context, 500, false, false);
                        captureOnLoad = false;
                    }
                }
            }

            return context;
        }
    })()</script><head><script type="text/javascript" src="js/funciones_js.js"></script>
	   <script language="javascript1.4" type="text/javascript">
		  function validar_y_enviar(pag,vide_asecot,vnro_cic,cant_filas){
			 var entrada = new String();
			 entrada = trim(document.forms[0].ide_asecot);
			 trim(document.forms[0].nro_cic);
			 var ide_emplea;
			 var nro_movimi;
			 var i = new Number();
			 var tipo_frame
			 i=0;
			 if(pag != 0){
				if(cant_filas > 0){
				   for (i=1;i<=cant_filas;i++){
					  if (document.getElementById(i).checked){
						 vide_asecot = eval('document.forms[0].ide_asecot'+i+'.value');
						 location.replace(pag+'&ide_asecot='+vide_asecot+'&envio=ok'+'&tipo_frame='+tipo_frame);
					  }
				   }
				}
				if (pag == 'consulta_doc_sinadj.php?bandera=1'){ 
				   location.replace(pag+'&ide_asecot='+vide_asecot+'&envio=ok'+'&tipo_frame='+tipo_frame);
				}
			 }
		  }

		  function validar_nuevo_aseg(nro_docume){
			 var check;
			 var i;
			 var tipo_nacionalidad;
			 var tipo_frame;
			 if(document.forms[0].nro_cic.value == ""){
				document.forms[0].nro_cic.select();
				document.forms[0].nro_cic.focus();
				alert("No puede dejar en blanco el Nro Documento");
				return false;
			 }
		  }

		  function actualizar_detalle(ide_asecot, ind_estado){
			 var paramCot = document.forms[0].paramCot.value;
			 window.parent.frames[1].location="comprobacion_derecho_detalle.php?ind_estado="+ind_estado+"&ide_asecot="+ide_asecot+"&paramCot="+paramCot;
		  }

	   </script>
	<title>
	   INSTITUTO DE PREVISION SOCIAL  
	</title>
	
	   <link href="css/style2.css" rel="stylesheet" type="text/css">
	   
	   </head><body><center>
	   <center>
			<table width="100%">
				<tbody><tr>
					<td width="30%"><img src="images/logo1.jpg"></td>
					<td align="center" class="titulorojo">CONSULTA DE ASEGURADO</td>
					<td width="30%" align="right"><img src="images/logo2.jpg"></td>
				</tr>
			 </tbody></table>
		</center>
	   </center>
	
	
	<center>
	<form name="vesbrbacnorc" method="POST" action="comprobacion_de_derecho_externo.php">
	<table cellpadding="5" border="0" cellspacing="10">
	   <tbody><tr>
	   <!--
		  <td class=titulochico> Tipo de Asegurado: </td>
		  <td>
			 <select name="tipo" class=boton>
				<option value="cot">Asegurado Cotizante</option>
				<option value="ben">Beneficiario</option>

			 </select>
		  </td>
		  -->
		  <td class="titulochico"> Nro Documento: </td>
		  <td>
			 <input type="text" name="nro_cic" maxlength="15" size="12" value="343883" onkeydown="trim_2(document.forms[0].nro_cic)">
		  </td>
		  <td> <input type="submit" name="recuperar" value="Recuperar"> </td>
	   </tr>
	</tbody></table>

	<h4 align="left" class="titulochico">Jueves 13 de Julio de 2023</h4>
	<h4 align="left" class="titulochico">Datos de la persona</h4> 

	<table>
	   <tbody><tr>
		  <th class="titulochico" width="3%"> Elegir </th>
			<!--<th class=titulochico width=2%>
			  Actualizar
			</th> -->
		  <th class="titulochico" width="10%"> Nro Documento </th>
		  <th class="titulochico" width="20%"> Nombres </th>
		  <th class="titulochico" width="20%"> Apellidos </th>
		  <th class="titulochico" width="8%"> Fecha Nacim </th>
		  <th class="titulochico" width="6%"> Sexo </th>
		  <th class="titulochico" width="12%"> Tipo Aseg.</th>
		  <th class="titulochico" width="8%"> Beneficiarios Activos </th>
		  <th class="titulochico" width="8%"> Enrolado </th>
		   <th class="titulochico" width="8%"> Vencimiento de fe de vida </th>


		  <!--
		  <th class=titulochico width=15%> Vencimiento del Seguro Social </th>
		  <th class=titulochico width=30%> ï¿½ltimo periodo de aporte</th>
		  -->
	   </tr>
	<tr bgcolor="#e2e8f6">
	<td align="center">
												<input name="elegir" type="radio" value="" checked="" id="0">
											</td>
											<td align="center">
												343883				
											</td>
											<td align="center">MARIA HILDA
											</td>
											<td align="center">JARA DE GUILLEN
											</td>
											<td align="center">19-11-1943
											</td>
											<td align="center">FEMENINO
											</td>
											<td align="center">BENEF. MADRE
											</td>	
											<td align="center">
											</td>
											<td align="center">SI
											</td>
											<td align="center">
											</td>

											<!-- <td align=center>11-09-2023
											</td>
											<td align=center>
											</td>
												-->									
										</tr>	</tbody></table>
	<br>
	<br>
	<br>
	<br>



	   <table>
			   <tbody><tr>
				  <th class="titulochico" width="6%">Nro.</th>
				  <th class="titulochico" width="20%"> Titular</th>
				  <th class="titulochico" width="4%"> Estado</th>
				  <th class="titulochico" width="6%"> Meses de aporte</th>
				  <th class="titulochico" width="6%"> Vencimiento</th>
				  <th class="titulochico" width="6%"> Ultimo Periodo Abonado</th>

				 
			   </tr>
				   <tr bgcolor="#e2e8f6">

											<td align="center">
												0002-81-01634				
											</td>
											<td align="center">HILDA SUSANA GUILLEN JARA (MINISTERIO PUBLICO)
											</td>
											<td align="center">ACTIVO
											</td>
											<td align="center">154
											</td>
												<td align="center">11-09-2023</td><td align="center">JUNIO/2023</td></tr>	</tbody></table>
	<input type="hidden" name="envio" value="ok">
	</form>
	
	</center></body></html>
"""
cells = getRow(html)
print(cells.__len__())
print(cells) 