$(document).ready(function () {
    activarMenu();

});


function activarMenu() {
    $('#sidebarCollapse').on('click', function () {
        $('#sidebar').toggleClass('active');
        $('#titulo').toggleClass('corrido');
    });
}
const Test = (request) => {
    lista=["Lasaña", "Charquican", "Porotos Granados"]
    contexto={"nombre":"Oscar Mouras","Comidas":Lista}

    return render(request, 'test.html', contexto)
}