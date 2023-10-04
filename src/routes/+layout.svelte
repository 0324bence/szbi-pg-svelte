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

    let showMobileMenu = false;
</script>

<div id="header">
    <div id="above-arc">
        <div id="navbar" class="no-mobile">
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
        <div id="navbar" class="only-mobile">
            <a href="{base}/"><img id="main-logo" src="https://szbi-pg.hu/images/logo_mobil.png" alt="PG logo" /></a>
            <button id="hamburger" on:click={() => (showMobileMenu = true)}>
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512"
                    ><!--! Font Awesome Free 6.4.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. --><path
                        d="M0 96C0 78.3 14.3 64 32 64H416c17.7 0 32 14.3 32 32s-14.3 32-32 32H32C14.3 128 0 113.7 0 96zM0 256c0-17.7 14.3-32 32-32H416c17.7 0 32 14.3 32 32s-14.3 32-32 32H32c-17.7 0-32-14.3-32-32zM448 416c0 17.7-14.3 32-32 32H32c-17.7 0-32-14.3-32-32s14.3-32 32-32H416c17.7 0 32 14.3 32 32z"
                    /></svg
                >
            </button>
        </div>
        <div id="pg150-kreta-container">
            <a href="http://pg150.hu/" target="_blank" class="no-mobile"
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

            <a href="https://szbi-kiskunfelegyhaza.e-kreta.hu/" target="_blank" class="no-mobile"
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
<!-- svelte-ignore a11y-click-events-have-key-events -->
<!-- svelte-ignore a11y-no-static-element-interactions -->
<div
    id="mobile-menu-container"
    class={showMobileMenu ? "shown" : ""}
    on:click|self={() => {
        showMobileMenu = false;
    }}
>
    <div id="mobile-menu" class={showMobileMenu ? "out" : ""}>
        <a href="http://pg150.hu/" target="_blank" class="logo">
            <img class="pg150-kreta-logo-mobile" src="https://szbi-pg.hu/images/logo150.png" alt="PG150 logo" /></a
        >
        <a href="https://szbi-kiskunfelegyhaza.e-kreta.hu/" target="_blank" class="logo">
            <img class="pg150-kreta-logo-mobile" src="https://szbi-pg.hu/images/kreta_logo.png" alt="Kreta logo" /></a
        >
        <button
            id="close-button"
            on:click={() => {
                showMobileMenu = false;
            }}
        >
            <span>&times;</span>
        </button>
        <div id="mobile-menu-content">
            <div class="item">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 512"
                    ><!--! Font Awesome Free 6.4.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. --><path
                        d="M310.6 233.4c12.5 12.5 12.5 32.8 0 45.3l-192 192c-12.5 12.5-32.8 12.5-45.3 0s-12.5-32.8 0-45.3L242.7 256 73.4 86.6c-12.5-12.5-12.5-32.8 0-45.3s32.8-12.5 45.3 0l192 192z"
                    /></svg
                ><a href="{base}/contacts">Elérhetőségek</a>
            </div>
            <div class="item">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 512"
                    ><!--! Font Awesome Free 6.4.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. --><path
                        d="M310.6 233.4c12.5 12.5 12.5 32.8 0 45.3l-192 192c-12.5 12.5-32.8 12.5-45.3 0s-12.5-32.8 0-45.3L242.7 256 73.4 86.6c-12.5-12.5-12.5-32.8 0-45.3s32.8-12.5 45.3 0l192 192z"
                    /></svg
                ><a href="{base}/munkatarsaink">Munkatársaink</a>
            </div>
            <div class="item">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 512"
                    ><!--! Font Awesome Free 6.4.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. --><path
                        d="M310.6 233.4c12.5 12.5 12.5 32.8 0 45.3l-192 192c-12.5 12.5-32.8 12.5-45.3 0s-12.5-32.8 0-45.3L242.7 256 73.4 86.6c-12.5-12.5-12.5-32.8 0-45.3s32.8-12.5 45.3 0l192 192z"
                    /></svg
                ><a href="{base}/">Dokumentumok</a>
            </div>
            <div class="item">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 512"
                    ><!--! Font Awesome Free 6.4.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. --><path
                        d="M310.6 233.4c12.5 12.5 12.5 32.8 0 45.3l-192 192c-12.5 12.5-32.8 12.5-45.3 0s-12.5-32.8 0-45.3L242.7 256 73.4 86.6c-12.5-12.5-12.5-32.8 0-45.3s32.8-12.5 45.3 0l192 192z"
                    /></svg
                ><a href="{base}/">Gyermekvédelem</a>
            </div>
            <div class="item">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 512"
                    ><!--! Font Awesome Free 6.4.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. --><path
                        d="M310.6 233.4c12.5 12.5 12.5 32.8 0 45.3l-192 192c-12.5 12.5-32.8 12.5-45.3 0s-12.5-32.8 0-45.3L242.7 256 73.4 86.6c-12.5-12.5-12.5-32.8 0-45.3s32.8-12.5 45.3 0l192 192z"
                    /></svg
                ><a href="{base}/">Büszkeségeink</a>
            </div>
            <div class="item">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 512"
                    ><!--! Font Awesome Free 6.4.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. --><path
                        d="M310.6 233.4c12.5 12.5 12.5 32.8 0 45.3l-192 192c-12.5 12.5-32.8 12.5-45.3 0s-12.5-32.8 0-45.3L242.7 256 73.4 86.6c-12.5-12.5-12.5-32.8 0-45.3s32.8-12.5 45.3 0l192 192z"
                    /></svg
                ><a href="{base}/">Galéria</a>
            </div>
            <div class="item">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 512"
                    ><!--! Font Awesome Free 6.4.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. --><path
                        d="M310.6 233.4c12.5 12.5 12.5 32.8 0 45.3l-192 192c-12.5 12.5-32.8 12.5-45.3 0s-12.5-32.8 0-45.3L242.7 256 73.4 86.6c-12.5-12.5-12.5-32.8 0-45.3s32.8-12.5 45.3 0l192 192z"
                    /></svg
                ><a href="{base}/">Adatkezelési Tájékoztató</a>
            </div>
            <div class="item">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 512"
                    ><!--! Font Awesome Free 6.4.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. --><path
                        d="M310.6 233.4c12.5 12.5 12.5 32.8 0 45.3l-192 192c-12.5 12.5-32.8 12.5-45.3 0s-12.5-32.8 0-45.3L242.7 256 73.4 86.6c-12.5-12.5-12.5-32.8 0-45.3s32.8-12.5 45.3 0l192 192z"
                    /></svg
                ><a href="{base}/">Felnőttképzés</a>
            </div>
            <div class="item">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 512"
                    ><!--! Font Awesome Free 6.4.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. --><path
                        d="M310.6 233.4c12.5 12.5 12.5 32.8 0 45.3l-192 192c-12.5 12.5-32.8 12.5-45.3 0s-12.5-32.8 0-45.3L242.7 256 73.4 86.6c-12.5-12.5-12.5-32.8 0-45.3s32.8-12.5 45.3 0l192 192z"
                    /></svg
                ><a href="{base}/">Keresés</a>
            </div>
        </div>
    </div>
</div>

<style lang="scss">
    @import "$lib/styles/variables.scss";

    #mobile-menu-container {
        transition: background-color 0.5s;
        position: absolute;
        overflow: hidden;
        left: 0;
        top: 0;
        width: 100vw;
        height: 100vh;
        pointer-events: none;
        &.shown {
            pointer-events: all;
            background-color: rgba(0, 0, 0, 0.6);
        }
        #mobile-menu {
            transition: transform 0.5s ease-in-out;
            transform: translateX(100%);
            position: absolute;
            right: 0;
            top: 0;
            width: 65vw;
            height: 100vh;
            background-color: $side-blue;
            display: grid;
            grid-template-columns: 2fr 2fr 1fr;
            grid-auto-rows: min-content auto;

            &.out {
                transform: translateX(0%);
            }

            .logo {
                display: block;
                width: 100%;
                padding: 1rem;

                img {
                    width: 100%;
                }
            }

            #close-button {
                width: 100%;
                height: 100%;
                display: grid;
                place-items: center;
                font-size: 3.5rem;
                background: none;
                border: none;
                outline: none;
                color: white;
            }

            #mobile-menu-content {
                grid-column: span 3;
                display: flex;
                flex-direction: column;
                align-items: stretch;
                padding: 0.5rem;
                gap: 0.5rem;

                .item {
                    padding: 0.5rem;
                    text-transform: uppercase;
                    display: flex;
                    align-items: center;
                    gap: 0.5rem;

                    a {
                        color: white;
                        text-decoration: none;
                    }

                    svg {
                        height: 1rem;
                        fill: white;
                    }
                }
            }
        }
    }

    #header {
        #above-arc {
            background-color: white;

            #navbar {
                display: flex;
                width: 100%;
                height: auto;
                padding: 2rem;
                padding-bottom: 1rem;
                align-items: center;
                justify-content: space-between;

                #main-logo {
                    display: block;
                    height: 100%;
                    width: 40vw;
                }

                #hamburger {
                    height: 100%;
                    width: 10vw;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    background: none;
                    border: none;
                    &:hover {
                        cursor: pointer;
                        svg {
                            fill: lighten(black, 20);
                        }
                    }
                    svg {
                        aspect-ratio: 1 / 1;
                        height: 100%;
                    }
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
                margin-left: 2rem;
                margin-right: 2rem;
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

    //media query that activates when width is less than 1100px
    @media screen and (max-width: 1100px) {
        .no-mobile {
            display: none !important;
        }

        #top-arc {
            height: 100px !important;
        }

        #navbar {
            #main-logo {
                width: 60vw !important;
            }
        }

        #main-title {
            h1 {
                font-size: 3rem !important;
            }
        }
    }

    @media screen and (min-width: 1100px) {
        .only-mobile {
            display: none !important;
        }
    }
</style>
