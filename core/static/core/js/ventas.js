$(document).ready(function () {
    activarMenu();
    editarVenta();
    guardarVenta();
});


function activarMenu() {
    $('#sidebarCollapse').on('click', function () {
        $('#sidebar').toggleClass('active');
        $('#titulo').toggleClass('corrido');
    });
}
const Test = (request) => {
    lista = ["Lasaña", "Charquican", "Porotos Granados"]
    contexto = { "nombre": "Oscar Mouras", "Comidas": Lista }

    return render(request, 'test.html', contexto)
}

function editarVenta() {
    $('#btnEditarVenta').on('click', function () {
        $('#selectPedido').prop("disabled", false);
        $('#btnEditarVenta').css("display", "none");
        $('#btnGuardarVenta').css("display", "inline");

    });
}

function guardarVenta() {
    $('#btnGuardarVenta').on('click', function () {
        $('#selectPedido').prop("disabled", true);
        $('#btnGuardarVenta').css("display", "none");
        $('#btnEditarVenta').css("display", "inline");
    });
}