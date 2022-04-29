$(document).ready(function () {
    activarMenu();

});


function activarMenu() {
    $('#sidebarCollapse').on('click', function () {
        $('#sidebar').toggleClass('active');
        $('#carrusel').toggleClass('activo');
        $('#titulo').toggleClass('corrido');
    });
}