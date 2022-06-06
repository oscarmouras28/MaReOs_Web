$(document).ready(function () {
    activarMenu();

});


function activarMenu() {
    $('#sidebarCollapse').on('click', function () {
        $('#sidebar').toggleClass('active');
        $('#titulo').toggleClass('corrido');
    });
}
