$(document).ready(function () {
    validarMetodoPago();
    activarMenu();
    rutCorrecto2();
    validarProducto();
    validarVendedor();

});

function activarMenu() {
    $('#sidebarCollapse').on('click', function () {
        $('#sidebar').toggleClass('active');
        $('#titulo').toggleClass('corrido');
    });
}

function soloLetras(e) {
    var key = e.keyCode || e.which,
        tecla = String.fromCharCode(key).toLowerCase(),
        letras = " áéíóúabcdefghijklmnñopqrstuvwxyz",
        especiales = [8, 37, 39, 46],
        tecla_especial = false;

    for (var i in especiales) {
        if (key == especiales[i]) {
            tecla_especial = true;
            break;
        }
    }

    if (letras.indexOf(tecla) == -1 && !tecla_especial) {
        return false;
    }
}

function soloNumerosDatos(e) {
    var key = e.keyCode || e.which,
        tecla = String.fromCharCode(key).toLowerCase(),
        letras = "12345678910",
        especiales = [8, 37, 39, 46],
        tecla_especial = false;

    for (var i in especiales) {
        if (key == especiales[i]) {
            tecla_especial = true;
            break;
        }
    }

    if (letras.indexOf(tecla) == -1 && !tecla_especial) {
        return false;
    }
}

function validarMetodoPago() {
    $("#btnAgregarMedio").click(function (e) {
        var medioPago = $('#medioPago').val();
        var errorValidacionMP = true;
        if (medioPago == null || medioPago == "") {
            $("#spMedioPago").addClass("has-error");
            $("#spMedioPago").show();
            $("#spMedioPago").html("Ingrese un método de pago válido");
            $("#spMedioPago").css("color", "#dc3545");
            errorValidacionMP = true;
        }
        else { errorValidacionMP = false }
        if (errorValidacionMP == true) {alertify.error('Medio de pago No Registrado');}
        if (errorValidacionMP == false) {
            alertify.confirm('Seguro?', function(){ alertify.success('Si'); $("#formulario_registroMedioPago").submit(); });
        }
    });
}

function validarProducto() {
    $("#btnAgregarProducto").click(function (e) {
        var nombre = $('#prodNombre').val();
        var precio = $('#precioProd').val();
        var imagen = $('#txtImagen').val();
        var descrip = $('#descProd').val();
        var tipo = $('#tipoProd').val();
        var errorValidacionProd = true;
        if (nombre == null || nombre == "") {
            $("#spNomProd").addClass("has-error");
            $("#spNomProd").show();
            $("#spNomProd").html("Ingrese un nombre válido");
            $("#spNomProd").css("color", "#dc3545");
            errorValidacionProd = true;
        }
        if (precio == null || precio == "") {
            $("#spPrecioProd").addClass("has-error");
            $("#spPrecioProd").show();
            $("#spPrecioProd").html("Ingrese un precio válido");
            $("#spPrecioProd").css("color", "#dc3545");
            errorValidacionProd = true;
        }
        if (imagen == null || imagen == "") {
            $("#spImgProd").addClass("has-error");
            $("#spImgProd").show();
            $("#spImgProd").html("Ingrese una imagen");
            $("#spImgProd").css("color", "#dc3545");
            errorValidacionProd = true;
        }
        if (descrip == null || descrip == "") {
            $("#spDescProd").addClass("has-error");
            $("#spDescProd").show();
            $("#spDescProd").html("Ingrese una descripción");
            $("#spDescProd").css("color", "#dc3545");
            errorValidacionProd = true;
        }
        if (tipo == "0") {
            $("#spTipoProd").addClass("has-error");
            $("#spTipoProd").show();
            $("#spTipoProd").html("Seleccione un tipo de alimento");
            $("#spTipoProd").css("color", "#dc3545");
            errorValidacionProd = true;
        }
        else if (nombre != null || nombre != "" && precio != null || precio != "" && imagen != null || imagen == "" &&
                descrip != null || descrip != "" && tipo != "0") {
            errorValidacionProd = false;
        }
        if (errorValidacionProd == true) {alertify.error('Producto No Registrado');}
        if (errorValidacionProd == false) {
            alertify.confirm('Seguro?', function(){ alertify.success('Si'); $("#formulario_registroProducto").submit(); });
        }

    });
}

function rutCorrecto2() {
    $('#txtRut').on("change", function () {
        if (!Fn2.validaRut2($('#txtRut').val())) {
            $('#txtRut').addClass('border-rojo');
            alertify.error('Rut invalido');
        } else {
            $('#txtRut').removeClass('border-rojo');
            $('#txtRut').addClass('border-verde');
        }
    });
}

var Fn2 = {
    // Valida el rut con su cadena completa "XXXXXXXX-X"
    validaRut2: function (rutCompleto) {
        if (!/^[0-9]+[-|‐]{1}[0-9kK]{1}$/.test(rutCompleto))
            return false;
        var tmp = rutCompleto.split('-');
        var digv = tmp[1];
        var rut = tmp[0];
        if (digv == 'K') digv = 'k';
        return (Fn2.dv(rut) == digv);
    },
    dv: function (T) {
        var M = 0, S = 1;
        for (; T; T = Math.floor(T / 10))
            S = (S + T % 10 * (9 - M++ % 6)) % 11;
        return S ? S - 1 : 'k';
    }
}

function validarVendedor() {
    $("#btnAgregarVendedor").click(function (e) {
        var rut = $('#txtRut').val();
        var prinom = $('#primNombre').val();
        var segnom = $('#segNombre').val();
        var appater = $('#apPaterno').val();
        var apmater = $('#apMaterno').val();
        var errorValidacionVend = true;
        if (rut == null || rut == "") {
            $("#sprutVend").addClass("has-error");
            $("#sprutVend").show();
            $("#sprutVend").html("Ingrese un rut válido");
            $("#sprutVend").css("color", "#dc3545");
            errorValidacionVend = true;
        }
        if (prinom == null || prinom == "") {
            $("#spprinomVend").addClass("has-error");
            $("#spprinomVend").show();
            $("#spprinomVend").html("Ingrese un Nombre válido");
            $("#spprinomVend").css("color", "#dc3545");
            errorValidacionVend = true;
        }
        if (segnom == null || segnom == "") {
            $("#spsegnomVend").addClass("has-error");
            $("#spsegnomVend").show();
            $("#spsegnomVend").html("Ingrese un Nombre válido");
            $("#spsegnomVend").css("color", "#dc3545");
            errorValidacionVend = true;
        }
        if (appater == null || appater == "") {
            $("#spappaterVend").addClass("has-error");
            $("#spappaterVend").show();
            $("#spappaterVend").html("Ingrese un Apellido válido");
            $("#spappaterVend").css("color", "#dc3545");
            errorValidacionVend = true;
        }
        if (apmater == null || apmater == "") {
            $("#spapmatVend").addClass("has-error");
            $("#spapmatVend").show();
            $("#spapmatVend").html("Ingrese un Apellido válido");
            $("#spapmatVend").css("color", "#dc3545");
            errorValidacionVend = true;
        }
        else { errorValidacionVend = false;}
        if (errorValidacionVend == true) {alertify.error('Vendedor No Registrado');}
        if (errorValidacionVend == false) {
            alertify.confirm('Seguro?', function(){ alertify.success('Vendedor Registrado'); $("#formulario-registroVendedor").submit(); });
        }
    });
}