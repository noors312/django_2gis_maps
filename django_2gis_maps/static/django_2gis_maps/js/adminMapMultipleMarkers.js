DG.then(function () {
    var markers = DG.featureGroup();
    var markers_array = [];
    var geolocationInput = $('#id_geolocation');
    map = DG.map('map', {
        'center': [42.882004, 74.582748],
        'zoom': 14
    });
    prepareMap();

    map.on('click', function (e) {
        var marker = DG.marker([e.latlng.lat, e.latlng.lng], {draggable: true}).addTo(markers);
        markers.addTo(map);
        markers_array.push(marker);
        if (geolocationInput.val()) {
            geolocationInput.val(geolocationInput.val().toString() + ';' + e.latlng.lat.toString() + ',' + e.latlng.lng.toString());
        }
        else {
            geolocationInput.val(e.latlng.lat.toString() + ',' + e.latlng.lng.toString());
        }
        $('.clear-button').on('click', hideMarkers);
        $.each(markers_array, function (i, obj) {
            $(obj).on('moveend', function (e) {
                var old_geolocation = geolocationInput.val().split(';')[i];
                var new_geolocation = e.target._latlng.lat.toString() + ',' + e.target._latlng.lng.toString();
                geolocationInput.val(geolocationInput.val().replace(old_geolocation, new_geolocation))
            })
        });

        function hideMarkers() {
            markers.removeFrom(map);
            markers = DG.featureGroup();
            markers_array = [];
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