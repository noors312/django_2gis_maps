DG.then(function () {
    var markers = DG.featureGroup();
    var geolocationInput = $('#id_geolocation');
    map = DG.map('map', {
        'center': [42.882004, 74.582748],
        'zoom': 14
    });
    prepareMap();

    map.on('click', function (e) {
        DG.marker([e.latlng.lat, e.latlng.lng]).addTo(markers);
        markers.addTo(map);
        if (geolocationInput.val()) {

            geolocationInput.val(geolocationInput.val().toString() + ';' + e.latlng.lat.toString() + ',' + e.latlng.lng.toString());

        }
        else {

            geolocationInput.val(e.latlng.lat.toString() + ',' + e.latlng.lng.toString());

        }
        $('.clear-button').on('click', hideMarkers);

        function hideMarkers() {
            markers.removeFrom(map);
            markers = DG.featureGroup();
            $('#id_geolocation').val('');
        }


    });

    function addMarkers(positions) {
        for (var i = 0; i < positions.length; i++) {
            DG.marker(positions[i].split(',')).addTo(markers);
        }
        markers.addTo(map);
    }

    function prepareMap() {
        if (geolocationInput.val()) {
            if (geolocationInput.val().indexOf(';')) {
                addMarkers(geolocationInput.val().split(';'));
                return true;
            }
            addMarkers(geolocationInput.val());
            return true;
        }
        return false;
    }


});