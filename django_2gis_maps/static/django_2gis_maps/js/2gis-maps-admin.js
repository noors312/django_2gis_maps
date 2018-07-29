/*
Integration for Google Maps in the django admin.

How it works:

You have an address field on the page.
Enter an address and an on change event will update the map
with the address. A marker will be placed at the address.
If the user needs to move the marker, they can and the geolocation
field will be updated.

Only one marker will remain present on the map at a time.

This script expects:

<input type="text" name="address" id="id_address" />
<input type="text" name="geolocation" id="id_geolocation" />

<script type="text/javascript" src="http://maps.google.com/maps/api/js?sensor=false"></script>

*/
DG.then(function () {
    map = DG.map('map', {
        'center': [42.882004, 74.582748],
        'zoom': 14
    });
    var marker;
    // map.locate({setView: true, enableHighAccuracy: true});
    // console.log(map.locate({setView: true, enableHighAccuracy: true, maxZoom: 15}));
    map.on('click', function (e) {
        // console.log(map);
        if (!marker) {
            marker = DG.marker([e.latlng.lat, e.latlng.lng]).addTo(map)
        }
        else {
            marker.setLatLng([e.latlng.lat, e.latlng.lng]);
        }
        // console.log(marker.getLatLng())
        $('#id_geolocation').val(marker.getLatLng().lat.toString() + ',' + marker.getLatLng().lng.toString())
    });
});
$(document).ready(function () {
    // var googlemap = googleMapAdmin();
    // googlemap.initialize();
});
