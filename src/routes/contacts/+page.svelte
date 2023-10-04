<script>
    import Map from "../../components/Map.svelte";
</script>

<svelte:head>
    <title>Elérhetőségek</title>
</svelte:head>

<div id="content">
    <div id="info">
        <h3>Kiskunfélegyházi Szent Benedek PG Két Tanítási Nyelvű Technikum és Kollégium</h3>
        <p>OM: 203365</p>
        <p>6100 Kiskunfélegyháza, Kossuth u. 24.</p>
        <p>
            <a href="https://szbi-pg.hu/images/phocadownload/Kozzeteteli/Alap%C3%ADt%C3%B3%20Okirat%20technikum.pdf"
                >Intézményünk alapító okirata</a
            >, annak kelte: 2020. május 21
        </p>
        <p>
            <a
                href="https://szbi-pg.hu/images/phocadownload/Kozzeteteli/Joger%C5%91s%20m%C5%B1k%C3%B6d%C3%A9si%20enged%C3%A9ly.pdf"
                >Intézményünk működési engedélye</a
            >
        </p>
        <p>
            <a
                href="https://szbi-pg.hu/images/phocadownload/Kozzeteteli/nyilv%C3%A1ntart%C3%A1sba%20v%C3%A9teli%20Kiskunfelegyhazi_Szent_Benedek.pdf"
                >Intézményünk nyilvántartásba vételi határozat</a
            >ának száma, kelte, az engedélyező hatóság:<br />NSZFH/NSZFH/008967-50/2020, 2020. június 30. Nemzeti
            Szakképzési és Felnőttképzési Hivatal
        </p>
        <a href="mailto:titkarsag@szbi-pg.hu">titkarsag@szbi-pg.hu</a>
        <p>+36 76 462 332</p>
        <p>Mellékek:</p>
        <p class="padded">11 - titkárság</p>
        <p class="padded">14 - tanári</p>
        <p class="padded">15 - kollégium</p>
        <p class="padded">16 - könyvtár</p>
    </div>
    <div id="maps"><Map /></div>
</div>

<style lang="scss">
    #content {
        display: flex;
        flex-direction: row;
        justify-content: space-around;
        align-items: center;
        width: 100%;
        height: 100%;
        padding-left: 15vw;
        padding-right: 15vw;
    }

    #info {
        display: flex;
        flex-direction: column;
        justify-content: space-around;
        align-items: flex-start;
        height: 100%;
        gap: 0.5rem;
        flex: 1;

        .padded {
            padding-left: 2rem;
        }
    }

    #maps {
        flex: 0;
        display: flex;
        flex-direction: column;
        justify-content: space-around;
        align-items: center;
        height: 100%;
    }

    #maps #map {
        width: 350px;
        height: 400px;
    }

    @media screen and (max-width: 1100px) {
        #content {
            flex-direction: column;
            gap: 2rem;
        }
    }
</style>
