/*Validaciones*/
function validarFormulario() {
    // removemos el div con la clase alert
    $('.alert').remove();

    // declarion de variables
    var nombre = $('#nombre').val(),
        email = $('#email').val(),
        direccion = $('#direccion').val(),
        phone = $('#phone').val(),
        cantidad = $('#cantidad').val(),
        mensaje = $('#mensaje').val();

    // validamos el campo nombre
    if (nombre == "" || nombre == null) {

        cambiarColor("nombre");
        // mostramos le mensaje de alerta
        mostraAlerta("Campo obligatorio");
        return false;
    } else {
        var expresion = /^[a-zA-ZñÑáéíóúÁÉÍÓÚ ]*$/;
        if (!expresion.test(nombre)) {
            // mostrara el mesaje que debe ingresar un nombre válido
            cambiarColor("nombre");
            mostraAlerta("No se permiten carateres especiales o numeros");
            return false;
        } else {
            colorDefault("nombre");
        }
    }

    // validamos el correo
    if (email == "" || email == null) {

        cambiarColor("email");
        // mostramos le mensaje de alerta
        mostraAlerta("Campo obligatorio");
        return false;
    } else {
        var expresion = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+$/;
        if (!expresion.test(email)) {
            // mostrara el mesaje que debe ingresar un nombre válido
            cambiarColor("email");
            mostraAlerta("Por favor ingrese un correo válido");
            return false;
        }
    }

    // validamos la direccion
    if (direccion == "" || direccion == null) {

        cambiarColor("direccion");
        // mostramos le mensaje de alerta
        mostraAlerta("Campo obligatorio");
        return false;
    } else {
        var expresion = /^[,\\.\\a-zA-Z0-9ñÑáéíóúÁÉÍÓÚ ]*$/;
        if (!expresion.test(direccion)) {
            // mostrara el mesaje que debe ingresar un nombre válido
            cambiarColor("direccion");
            mostraAlerta("No se permiten caracteres especiales");
            return false;
        }
    }

    // validamos telefono
    if (phone == "" || phone == null) {

        cambiarColor("phone");
        // mostramos le mensaje de alerta
        mostraAlerta("Campo obligatorio");
        return false;
    } else {
        var expresion = /^(\+?56)?(\s?)(0?9)(\s?)[987654]\d{7}$/;
        if (!expresion.test(phone)) {
            // mostrara el mesaje que debe ingresar un nombre válido
            cambiarColor("phone");
            mostraAlerta("Por favor ingrese un telefono válido");
            return false;
        }
    }

    // validamos cantidad de persona
    if (cantidad == "" || cantidad == null) {

        cambiarColor("cantidad");
        // mostramos le mensaje de alerta
        mostraAlerta("Campo obligatorio");
        return false;
    } else {
        var expresion = /^0*[1 - 9]\d*$/;
        if (expresion.test(cantidad) < 0 || expresion.test(cantidad) > 9) {
            // mostrara el mesaje que debe ingresar un nombre válido
            cambiarColor("cantidad");
            mostraAlerta("Por favor ingrese una cantidad válida");
            return false;
        }
    }

    // validamos el mensaje
    if (mensaje == "" || mensaje == null) {

        cambiarColor("mensaje");
        // mostramos le mensaje de alerta
        mostraAlerta("Campo obligatorio");
        return false;
    } else {
        var expresion = /^[,\\.\\a-zA-Z0-9ñÑáéíóúÁÉÍÓÚ ]*$/;
        if (!expresion.test(mensaje)) {
            // mostrara el mesaje que debe ingresar un nombre válido
            cambiarColor("mensaje");
            mostraAlerta("No se permiten caracteres especiales");
            return false;
        }
    }

    $('form').submit();


}

$('input').focus(function () {
    $('.alert').remove();
    colorDefault("nombre");
    colorDefault("email");
    colorDefault("direccion");
    colorDefault("phone");
    colorDefault("cantidad");
});

$('textarea').focus(function () {
    $('.alert').remove();
    colorDefault("mensaje");
});

// creamos un funcion de color por defecto a los bordes de los inputs
function colorDefault(dato) {
    $('#' + dato).css({
        border: "none",
        borderBottom: "1px solid #d63031"
    });
}

// creamos una funcio para cambiar de color a su bordes de los input
function cambiarColor(dato) {
    $('#' + dato).css({
        border: "1px solid #dd5144"
    });
}

// funcion para mostrar la alerta

function mostraAlerta(texto) {
    $('#boton').before('<div class="alert">Error: ' + texto + '</div>');
}