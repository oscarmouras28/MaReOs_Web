$(document).ready(function () {
    activarMenu();
    verSandwiches();

});


function activarMenu() {
    $('#sidebarCollapse').on('click', function () {
        $('#sidebar').toggleClass('active');
        $('#carrusel').toggleClass('activo');
        $('#titulo').toggleClass('corrido');
        $('#contenidoTarjetas').toggleClass('corridas');
    });
}

function verSandwiches(){
    $('#btnVerSandwich').on('click', function () {
        $('#flush-collapseOne').click();
        alert("holaaaaaa");
        console.log("aaaaa");
    
});

}