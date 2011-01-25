/*jslint maxerr: 1000, white: true, browser: true, devel: true, rhino: true, onevar: false, undef: true, nomen: true, eqeqeq: true, plusplus: true, bitwise: true, regexp: true, newcap: true, immed: true, sub: true */
/*global $: false, RAH: false, FB: false, WebFont: false, jQuery: false, window: false, google: false, require: false, define: false */
require(["libs/jquery.validation", "libs/jquery.ui", "libs/markerclusterer"], function () {
    $("#house_party_form").validate({ rules: { phone_number: { required: true }}});
    $('#house_party_link').click(function () { 
        $('#house_party_dialog').dialog('open'); 
        return false; 
    });
    $('#house_party_dialog').dialog({
        title: 'Energy meeting contact', 
        modal: true, 
        resizable: false, 
        draggable: false, 
        autoOpen: false, 
        buttons: { "Give me a call": function () { 
            $('#house_party_form').submit(); 
        }
        }
    });
    var myOptions = {
        zoom: 3,
        mapTypeId: google.maps.MapTypeId.TERRAIN,
        mapTypeControl: false,
        streetViewControl: false,
        scrollwheel: false,
        center: new google.maps.LatLng(37.0625, -95.677068)
    };
    var gmap = new google.maps.Map(document.getElementById("events_map"), myOptions);
    var infowindow = new google.maps.InfoWindow({ content: "" });
    var markers = [];
    for (var i = RAH.event_locations.length - 1; i > 0; i = i -1) {
        var marker = new google.maps.Marker({
            position: new google.maps.LatLng(RAH.event_locations[i].lat, RAH.event_locations[i].lon),
            map: gmap,
            info: RAH.event_locations[i].info
        });
        google.maps.event.addListener(marker, 'click', function() {
            infowindow.setContent(this.info);
            infowindow.open(gmap, this);
        });
        markers.push(marker);
    }
    // var markerCluster = new MarkerClusterer(gmap, markers, {gridSize: 10});
});
