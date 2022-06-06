$(document).ready(function () {
    activarMenu();

});


function activarMenu() {
    $('#sidebarCollapse').on('click', function () {
        $('#sidebar').toggleClass('active');
        $('#carrusel').toggleClass('activo');
        $('#titulo').toggleClass('corrido');
        $('#tarjetas1').toggleClass('corridas');
        $('#tarjetas2').toggleClass('corridas');
        $('#tarjetas3').toggleClass('corridas');
        $('#tarjetas4').toggleClass('corridas');

    });
}

function calcularPorProducto(){
    
}