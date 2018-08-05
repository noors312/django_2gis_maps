function addMarkers(positions) {
    for (var i = 0; i < positions.length; i++) {
        DG.marker(positions[i].split(',')).addTo(markers);
    }
    markers.addTo(map);
}

function prepareMap(geolocationInput, markers) {
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