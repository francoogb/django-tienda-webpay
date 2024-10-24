 function confirmaAlert(pregunta, ruta) {
     jCustomConfirm(pregunta, 'Tienda', 'Aceptar', 'Cancelar', function(r) {
         if (r) {
             window.location = ruta;
         }
     });
 }

 function alertAlert(mensaje) {
     jAlert(mensaje);
 }
function validaCorreo(valor) {
  if (/^(([^<>()[\]\.,;:\s@\"]+(\.[^<>()[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$/i.test(valor)){
   return true;
  } else {
   return false;
  }
}
 function agregarAlCarro()
 {
    var form=document.agregar_al_carro;
    form.cantidad.value=document.getElementById('cantidad').value;
    form.submit();
 }
 function sendLogin()
{
    var form=document.form_login;
    if(form.correo.value==0)
    {
        alertAlert('El campo E-Mail es obligatorio');
        form.correo.value='';
        return false;
    }
    if(validaCorreo(form.correo.value)==false)
    {
        alertAlert('El E-Mail no es válido');
        form.correo.value='';
        return false;
    }
    if(form.password.value==0)
    {
        alertAlert('El campo Contraseña es obligatorio');
        form.password.value='';
        return false;
    }
    form.submit();
}
function sendRegistro()
 {
    form=document.form_registro;
    if(form.nombre.value==0)
    {
        alertAlert('El campo Nombre es obligatorio');
        form.nombre.value='';
        return false;
    }
   
        if(form.apellido.value==0)
        {
            alertAlert('El campo Apellido es obligatorio');
            form.apellido.value='';
            return false;
        }
    
    
    if(form.correo.value==0)
    {
        alertAlert('El campo E-Mail es obligatorio');
        form.correo.value='';
        return false;
    }
    if(validaCorreo(form.correo.value)==false)
    {
        alertAlert('El E-Mail no es válido');
        form.correo.value='';
        return false;
    }
    if(form.password.value==0)
    {
        alertAlert('El campo Contraseña es obligatorio');
        form.password.value='';
        return false;
    }
    if(form.password2.value==0)
    {
        alertAlert('El campo Repetir Contraseña es obligatorio');
        form.password2.value='';
        return false;
    }
    if(form.password.value!=form.password2.value)
    {
        alertAlert('Las contraseñas ingresadas no coinciden');
        form.password.value='';
        form.password2.value='';
        return false;
    }
    form.submit();
 }
 function sendRestore()
 {
    var form=document.form_restore;
    
    
    
    if(form.password1.value==0)
    {
        alertAlert('El campo Contraseña es obligatorio');
        form.password1.value='';
        return false;
    }
    if(form.password2.value==0)
    {
        alertAlert('El campo Repetir Contraseña es obligatorio');
        form.password2.value='';
        return false;
    }
    if(form.password1.value!=form.password2.value)
    {
        alertAlert('Las contraseñas ingresadas no coinciden');
        form.password1.value='';
        form.password2.value='';
        return false;
    }
    form.submit();
 }
 function sendReset()
 {
    var form=document.form_reset;
    
    
    if(form.correo.value==0)
    {
        alertAlert('El campo E-Mail es obligatorio');
        form.correo.value='';
        return false;
    }
   
    form.submit();
 }
 function salir(ruta)
 {
    jCustomConfirm('¿Realmente desea cerrar sesión?', 'Tienda', 'Aceptar', 'Cancelar', function(r) {
         if (r) {
             window.location = ruta;
         }
     });
 }
 function modificarCantidadProductoCarro(id, cantidad)
 {
    let ruta="/carro/modificar-cantidad-carro/"+id+"/"+cantidad;
    window.location=ruta;
 }
 function sendPago()
 {
    let form=document.form_pagar;
    if(form.direccion.value==0)
    {
        alertAlert("Debes indicar la dirección del envío");
        return false;
    }
    if(form.indicaciones.value==0)
    {
        form.indicaciones.value="";
    }
    form.submit();
 }