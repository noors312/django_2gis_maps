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
    var marker;
    var geolocationInput = $('#id_geolocation');
    map = DG.map('map', {
        'center': [42.882004, 74.582748],
        'zoom': 14
    });
    prepareMap();
    map.on('click', function (e) {
        if (!marker) {
            marker = DG.marker([e.latlng.lat, e.latlng.lng], {
                'draggable': true
            }).addTo(map);

            geolocationInput.val(e.latlng.lat + ',' + e.latlng.lng);

        }
        else {
            marker.setLatLng([e.latlng.lat, e.latlng.lng]);
            geolocationInput.val(e.latlng.lat + ',' + e.latlng.lng);
        }
        marker.on('dragend', function (data) {
            geolocationInput.val(data.target._latlng.lat + ',' + data.target._latlng.lng);
        });
    });

    function prepareMap() {
        if (geolocationInput.val()) {
            marker = DG.marker(geolocationInput.val().split(','), {'draggable': true}).addTo(map);
            return true;
        }
        return false;
    }
});