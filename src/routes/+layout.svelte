<script lang="ts">
    import { page } from "$app/stores";
    import { afterNavigate } from "$app/navigation";
    let route = $page.url.pathname;
    afterNavigate(() => {
        route = $page.url.pathname;
    });
</script>

<div id="header">
    <div id="above-arc">
        <div id="navbar">
            <div>
                <a href="/"><img id="main-logo" src="https://szbi-pg.hu/images/logo.png" alt="PG logo" /></a>
            </div>

            <div id="navbar-links">
                <a href="/contacts">Elérhetőségek</a>
                <a href=".">Munkatársaink</a>
                <a href=".">Dokumentumok</a>
                <a href=".">Gyermekvédelem</a>
                <a href=".">Büszkeségeink</a>
                <a href=".">Galéria</a>
                <a href=".">Adatkezelési Tájékoztató</a>
                <a href=".">Felnőttképzés</a>
                <a href=".">Keresés</a>
            </div>
        </div>
        <div id="pg150-kreta-container">
            <a href="http://pg150.hu/" target="_blank"
                ><img class="pg150-kreta-logo" src="https://szbi-pg.hu/images/logo150.png" alt="PG150 logo" /></a
            >

            {#if route === "/"}
                <div class="sliderm" id="main-slider">
                    <h1>{route}</h1>
                    <!-- <div class="sliderm__slider">
                        <div class="sliderm__slides">
                            <div class="sliderm__slide">
                                <img src="https://szbi-pg.hu/images/Slider/KKF_NYNBANNER23-min.jpg" />
                            </div>
                            <div class="sliderm__slide">
                                <img src="https://szbi-pg.hu/images/banners/diakolimpia2022.jpg" />
                            </div>
                            <div class="sliderm__slide">
                                <img src="https://szbi-pg.hu/images/Slider/banner_Avat-min.jpg" />
                            </div>
                            <div class="sliderm__slide">
                                <img src="https://szbi-pg.hu/images/IMG_0205.jpeg" />
                            </div>
                            <div class="sliderm__slide">
                                <img src="https://szbi-pg.hu/images/banners/golyak2022.jpg" />
                            </div>
                        </div>
                    </div> -->
                </div>
            {:else}
                <div id="main-title">
                    <h1>{document.title}</h1>
                </div>
            {/if}

            <a href="https://szbi-kiskunfelegyhaza.e-kreta.hu/" target="_blank"
                ><img class="pg150-kreta-logo" src="https://szbi-pg.hu/images/kreta_logo.png" alt="Kreta logo" /></a
            >
        </div>
    </div>
    <div id="top-arc">
        <svg width="1920" viewBox="0 0 1920 217" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M1920 0C1277.26 200.082 757.047 200.082 0 0V216.5H1920V0Z" fill="#3F486C" />
        </svg>
    </div>
</div>
<div id="content">
    <slot />
</div>

<style lang="scss">
    @import "$lib/styles/variables.scss";
    #header {
        #above-arc {
            background-color: white;

            #navbar {
                padding: 2rem;
                padding-bottom: 0px;
                display: flex;
                justify-content: space-between;
                flex-wrap: wrap;

                #main-logo {
                    width: 40vw;
                }

                #navbar-links {
                    width: 45vw;
                    display: flex;
                    flex-wrap: wrap;
                    justify-content: center;
                    gap: 0rem 2rem;

                    a {
                        text-decoration: none;
                        color: black;
                        text-transform: uppercase;

                        &:hover {
                            text-decoration-line: underline;
                            text-decoration-thickness: 0.08rem;
                        }
                    }
                }
            }

            #pg150-kreta-container {
                display: flex;
                justify-content: space-between;
                margin-left: 40px;
                margin-right: 40px;
                align-items: flex-start;

                .pg150-kreta-logo {
                    margin-top: 2rem;
                    height: 80px;
                }
            }

            #main-slider {
                margin-top: 30px;
                width: 1400px;
                height: 600px;
                background-color: black;

                .sliderm__slider {
                    height: 600px;
                }
            }

            #main-title {
                margin-top: 30px;
                width: 1400px;
                display: flex;
                justify-content: center;
                align-items: center;

                h1 {
                    font-size: 5rem;
                    color: $main-blue;
                }
            }
        }

        #top-arc {
            position: relative;
            padding: 0;
            z-index: -1;
            height: 217px;
            // background-image: radial-gradient(ellipse at center, white 0%, white 70%, transparent calc(70% + 5px));
            background-position: bottom;
            // background-position-y: -350px;
            // background-size: 120% 120%;
            background-repeat: no-repeat;
            background-color: white;
            // background-image: url("./top.svg");
            // margin-bottom: -220px;
            svg {
                position: absolute;
                bottom: -5px;
                left: 0;
                width: 100%;
                path {
                    position: absolute;
                    bottom: 0;
                }
            }
        }
    }
    #content {
        width: 100%;
    }
</style>
