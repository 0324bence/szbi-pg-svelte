<script lang="ts">
    import { page } from "$app/stores";
    import { base } from "$app/paths";
    import { afterNavigate } from "$app/navigation";
    let route = $page.url.pathname;
    console.log(route);
    let title = document.title;
    afterNavigate(() => {
        route = $page.url.pathname;
        title = document.title;
    });

    import emblaCarouselSvelte from "embla-carousel-svelte";
    import Autoplay from "embla-carousel-autoplay";
    import DropDownLink from "../components/DropDownLink.svelte";

    let options = {
        loop: true
    };
    let plugins = [Autoplay()];

    let emblaApi: any;
    const onInit = (event: any) => {
        emblaApi = event.detail;
    };

    function onCarouselPrevClick() {
        emblaApi.scrollPrev(false);
    }

    function onCarouselNextClick() {
        emblaApi.scrollNext(false);
    }
</script>

<div id="header">
    <div id="above-arc">
        <div id="navbar">
            <div>
                <a href="{base}/"><img id="main-logo" src="https://szbi-pg.hu/images/logo.png" alt="PG logo" /></a>
            </div>

            <div id="navbar-links">
                <a href="{base}/contacts">Elérhetőségek</a>
                <a href="{base}/munkatarsaink">Munkatársaink</a>
                <DropDownLink
                    href={[
                        { href: `${base}`, name: "Közétételi lista" },
                        { href: `${base}`, name: "Letölthető dokumentumok" },
                        { href: `${base}`, name: "Közösségi szolgálat" },
                        { href: `${base}`, name: "Érettségi" }
                    ]}>Dokumentumok</DropDownLink
                >
                <!-- <a href="{base}/">Dokumentumok</a> -->
                <a href="{base}/">Gyermekvédelem</a>
                <a href="{base}/">Büszkeségeink</a>
                <a href="{base}/">Galéria</a>
                <a href="{base}/">Adatkezelési Tájékoztató</a>
                <a href="{base}/">Felnőttképzés</a>
                <a href="{base}/">Keresés</a>
            </div>
        </div>
        <div id="pg150-kreta-container">
            <a href="http://pg150.hu/" target="_blank"
                ><img class="pg150-kreta-logo" src="https://szbi-pg.hu/images/logo150.png" alt="PG150 logo" /></a
            >

            {#if route === `${base}` || route === `${base}/`}
                <div
                    class="embla"
                    id="main-container"
                    use:emblaCarouselSvelte={{ options, plugins }}
                    on:emblaInit={onInit}
                >
                    <div class="embla__container">
                        <div class="embla__slide">
                            <img src="https://szbi-pg.hu/images/Slider/KKF_NYNBANNER23-min.jpg" alt="" />
                        </div>
                        <div class="embla__slide">
                            <img src="https://szbi-pg.hu/images/banners/diakolimpia2022.jpg" alt="" />
                        </div>
                        <div class="embla__slide">
                            <img src="https://szbi-pg.hu/images/Slider/banner_Avat-min.jpg" alt="" />
                        </div>
                        <div class="embla__slide">
                            <img src="https://szbi-pg.hu/images/IMG_0205.jpeg" alt="" />
                        </div>
                        <div class="embla__slide">
                            <img src="https://szbi-pg.hu/images/banners/golyak2022.jpg" alt="" />
                        </div>
                    </div>
                    <button class="embla__prev carousel-button" on:click={onCarouselPrevClick}>
                        <svg xmlns="http://www.w3.org/2000/svg" height="1em" viewBox="0 0 448 512"
                            ><path
                                d="M9.4 233.4c-12.5 12.5-12.5 32.8 0 45.3l160 160c12.5 12.5 32.8 12.5 45.3 0s12.5-32.8 0-45.3L109.2 288 416 288c17.7 0 32-14.3 32-32s-14.3-32-32-32l-306.7 0L214.6 118.6c12.5-12.5 12.5-32.8 0-45.3s-32.8-12.5-45.3 0l-160 160z"
                            /></svg
                        >
                    </button>
                    <button class="embla__next carousel-button" on:click={onCarouselNextClick}
                        ><svg xmlns="http://www.w3.org/2000/svg" height="1em" viewBox="0 0 448 512"
                            ><path
                                d="M438.6 278.6c12.5-12.5 12.5-32.8 0-45.3l-160-160c-12.5-12.5-32.8-12.5-45.3 0s-12.5 32.8 0 45.3L338.8 224 32 224c-17.7 0-32 14.3-32 32s14.3 32 32 32l306.7 0L233.4 393.4c-12.5 12.5-12.5 32.8 0 45.3s32.8 12.5 45.3 0l160-160z"
                            /></svg
                        ></button
                    >
                </div>
            {:else}
                <div id="main-title">
                    <h1>{title}</h1>
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
<footer>
    {#if route === `${base}` || route === `${base}/`}
        <div id="footer-logos">
            <a target="_blank" href="https://www.netacad.com/"
                ><img src="https://szbi-pg.hu/images/2023/02/23/cisco.png" alt="cisco.png" /></a
            >
            <a href="https://www.cisco.com/c/hu_hu/index.html"
                ><img src="https://szbi-pg.hu/images/2023/02/23/oracle.png" alt="oracle.png" /></a
            >
            <img src="https://szbi-pg.hu/images/2023/02/23/aws.png" alt="aws.png" />
            <a href="https://bgazrt.hu/tamogatasok/hatartalanul/"
                ><img src="https://szbi-pg.hu/images/partnerek/logo_hat.png" alt="logo_hat.png" /></a
            >
        </div>
    {/if}
    <p>&copy 2023 PG</p>
    <p>Weboldal: &copy Deli Bence & Törteli Imre</p>
</footer>

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
                    align-items: center;
                    justify-content: center;
                    gap: 0px 2rem;

                    a {
                        display: block;
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

            .embla {
                overflow: hidden;
                width: 1000px;
                aspect-ratio: 16 / 9;
                position: relative;

                .carousel-button {
                    position: absolute;
                    top: 50%;
                    transform: translateY(-50%);
                    background-color: #333333cc;
                    border-radius: 50%;
                    border: none;
                    padding: 15px;
                    color: white;
                    aspect-ratio: 1 / 1;
                    cursor: pointer;

                    svg {
                        fill: white;
                    }
                }

                .embla__prev {
                    left: 0;
                }

                .embla__next {
                    right: 0;
                }

                .embla__container {
                    display: flex;
                    aspect-ratio: 16 / 9;

                    .embla__slide {
                        flex: 0 0 100%;
                        min-width: 0;

                        img {
                            width: 100%;
                            height: 100%;
                        }
                    }
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
            width: 100%;
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

    footer {
        margin-top: 10rem;
        padding-top: 2rem;
        padding-bottom: 2rem;
        display: flex;
        flex-direction: column;
        align-items: center;
        background-color: #49547e;

        #footer-logos {
            display: flex;
            flex-wrap: wrap;
            align-items: center;
            gap: 3rem;
            margin-bottom: 3rem;

            img {
                width: 20rem;
            }
        }
    }
</style>
