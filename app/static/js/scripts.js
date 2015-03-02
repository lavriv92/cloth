$(function() {
    $.fn.initMap = function() {
        var map, osmUrl, 
            osmAttrib, osm;

        map = new L.map($(this).attr('id'));
        osmUrl = 'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
        osmAttrib = 'Map data © <a href="http://openstreetmap.org">OpenStreetMap</a>';

        osm = new L.TileLayer(osmUrl, {
            minZoom: 8, 
            maxZoom: 12, 
            attribution: osmAttrib
        });
        map.setView(new L.LatLng(51.3, 0.7), 9);
        map.addLayer(osm);
    }

    $('#map')
        .height('300')
        .initMap();
});
