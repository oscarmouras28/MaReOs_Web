$(document).ready(function () {
    activarMenu();
    verSandwiches();

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

function verSandwiches(){
    $('#btnVerSandwich').on('click', function () {
        $('#flush-collapseOne').click();
        alert("holaaaaaa");
        console.log("aaaaa");
    
});

}