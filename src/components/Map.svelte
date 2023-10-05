<script>
    import "leaflet/dist/leaflet.css";
    import * as L from "leaflet";
    import { onMount } from "svelte";

    onMount(() => {
        let map = new L.Map("map", { tap: false });
        map.attributionControl.setPrefix("");
        let baseLayer = new L.TileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
            maxZoom: 19,
            noWrap: false,
            attribution:
                '<a href="https://www.openstreetmap.org/copyright" target="_blank">© OpenStreetMap contributors</a>'
        });
        let baseControl = L.control.scale({ metric: true, imperial: false });
        let mainMarker = new L.Marker([46.708465, 19.839248]);
        map.setView([46.708465, 19.839248], 17).addControl(baseControl).addLayer(baseLayer).addLayer(mainMarker);
    });
</script>

<div id="map" />

<style lang="scss">
    #map {
        width: 350px;
        height: 400px;
    }
</style>
