$(document).ready(function () {
    activarMenu();
    iniciarMap();
    calcularDelivery();
    habilitarDelivery();
});


function activarMenu() {
    $('#sidebarCollapse').on('click', function () {
        $('#sidebar').toggleClass('active');
        $('#titulo').toggleClass('corrido');
    });
}


function iniciarMap() {
    var coord = { lat: -33.610122, lng: -70.598798 };
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 15,
        center: coord,
        zoomControl: true,
    });
    var marker = new google.maps.Marker({
        position: { lat: -33.610122, lng: -70.598798 },
        map: map,
        draggable: true
    });


    $('#buscarDireccion').on('click', function () {
        // Creamos el objeto geodecoder
        var geocoder = new google.maps.Geocoder();
        $('#map').css("display", "block");
        $('#confirmarDireccion').css("display", "inline");

        address = document.getElementById('direccionDelivery').value;
        if (address != '') {
            // Llamamos a la función geodecode pasandole la dirección que hemos introducido en la caja de texto.
            geocoder.geocode({ 'address': address }, function (results, status) {
                if (status == 'OK') {
                    // Mostramos las coordenadas obtenidas en el p con id coordenadas
                    document.getElementById("coordenadas").innerHTML = 'Coordenadas:   ' + results[0].geometry.location.lat() + ', ' + results[0].geometry.location.lng();
                    // Posicionamos el marcador en las coordenadas obtenidas
                    marker.setPosition(results[0].geometry.location);
                    // Centramos el mapa en las coordenadas obtenidas
                    map.setCenter(marker.getPosition());
                    agendaForm.showMapaEventForm();
                }
            });
        }
    });
    
}

function calcularDelivery(){
    $('#confirmarDireccion').on('click', function () {
        $('#valorDelivery').val(2000);
    });
}

function habilitarDelivery(){
    $("input[type=radio][name=btnradio]").change(function () {
		if (this.value == 'delivery') {  
            $('#contenidoDelivery').css("display", "inline");
        } else {
            $('#contenidoDelivery').css("display", "none");
        }
      });
}