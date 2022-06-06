$(document).ready(function () {
    activarMenu();
	validarFormulario();

});


function activarMenu() {
    $('#sidebarCollapse').on('click', function () {
        $('#sidebar').toggleClass('active');
        $('#titulo').toggleClass('corrido');
    });
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

function validarFormulario() {
	$("#btnRegistrar").click(function (e) {
		var rut = $('#rutCli').val();
		var name = $('#nombreCli').val();
		var apellido = $('#apellidoCli').val();
		var email = $('#passCli').val();
		var telefono = $('#inputTelefono').val();
		var contrasena = $('#passCli').val();
		var errorValidacionDatos = false;
		if (rut == null || rut == ""){
			$("#spRut").addClass("has-error");
			$("#spRut").show();
			$("#spRut").html("Ingrese un Rut válido");
			$("#spRut").css("color", "#dc3545");
			errorValidacionDatos = true;
		}
		if (name == null || name == ""){
			$("#spName").addClass("has-error");
			$("#spName").show();
			$("#spName").html("Ingrese un nombre válido");
			$("#spName").css("color", "#dc3545");
			errorValidacionDatos = true;
		}
		if (apellido == null || apellido == ""){
			$("#spApellido").addClass("has-error");
			$("#spApellido").show();
			$("#spApellido").html("Ingrese un apellido válido");
			$("#spApellido").css("color", "#dc3545");
			errorValidacionDatos = true;
		}
		if (email == null || email == ""){
			$("#spEmail").addClass("has-error");
			$("#spEmail").show();
			$("#spEmail").html("Email no valido");
			$("#spEmail").css("color", "#dc3545");
			errorValidacionDatos = true;
		}
		if (telefono == null || telefono == ""){
			$("#spTelefono").addClass("has-error");
			$("#spTelefono").show();
			$("#spTelefono").html("Debe ingresar telefono valido");
			$("#spTelefono").css("color", "#dc3545");
			errorValidacionDatos = true;
		}
		if (contrasena == null || contrasena == ""){
			$("#spContra").addClass("has-error");
			$("#spContra").show();
			$("#spContra").html("Ingrese una contraseña como se le indica");
			$("#spContra").css("color", "#dc3545");
			errorValidacionDatos = true;
		}  
});
}