<script>
    let data = [
        {
            title: "Vezetőség",
            people: [
                {
                    name: "Rokolya Csaba",
                    contact: "igazgató",
                    description: ["informatikus mérnöktanár"],
                    img: "https://szbi-pg.hu/images/Tanarok/Rokolya Csaba.jpg"
                },
                {
                    name: "Dobos László",
                    contact: "szakirányú oktatásért felelős igazgatóhelyettes",
                    description: ["informatika"],
                    img: "https://szbi-pg.hu/images/Tanarok/Dobos László.jpg"
                },
                {
                    name: "Gálfi Tamás Imre",
                    contact: "kollégiumvezető",
                    description: [""],
                    img: "https://szbi-pg.hu/images/Tanarok/Gálfi Tamás.jpg"
                },
                {
                    name: "Tóth Tímea",
                    contact: "nevelési igazgatóhelyettes,   11.a osztályfőnök",
                    description: ["német nyelv"],
                    img: "https://szbi-pg.hu/images/Tanarok/Tóth Tímea.jpg"
                },
                {
                    name: "Szabó Anikó",
                    contact: "gazdasági vezető",
                    description: [""],
                    img: "https://szbi-pg.hu/images/Tanarok/Seres Anikó.jpg"
                }
            ]
        },
        {
            title: "Oktatók",
            people: [
                {
                    name: "Andrási Endre Jánosné",
                    contact: "",
                    description: ["könyvtáros"],
                    img: "https://szbi-pg.hu/images/Tanarok/Andrási Endréné.jpg"
                },
                {
                    name: "Áron-Görög Szilvia",
                    contact: "9/knyc osztályfőnök",
                    description: ["gépészmérnök", "informatika"],
                    img: "https://szbi-pg.hu/images/Tanarok/Áron-Görög_Szilvia.jpg"
                },
                {
                    name: "Balázs László",
                    contact: "",
                    description: ["testnevelés"],
                    img: "https://szbi-pg.hu/images/Tanarok/Balázs László.jpg"
                },
                {
                    name: "Bogácsi Csaba Mihály",
                    contact: "2/12.CNC osztályfőnök",
                    description: ["műszaki szakoktató"],
                    img: "https://szbi-pg.hu/images/Tanarok/Bogácsi Csaba.JPG"
                },
                {
                    name: "Bozó Beáta",
                    contact: "12.d osztályfőnök",
                    description: ["angol nyelv", "biológia"],
                    img: "https://szbi-pg.hu/images/Tanarok/Bozó Beáta.JPG"
                },
                {
                    name: "Csanádi Gergely",
                    contact: "",
                    description: ["kollégiumi nevelőtanár"],
                    img: "https://szbi-pg.hu/images/Tanarok/Csanádi Gergely.jpg"
                },
                {
                    name: "Csenkiné Zatykó Helga",
                    contact: "10.c osztályfőnök",
                    description: ["matematika"],
                    img: "https://szbi-pg.hu/images/Tanarok/Csenkiné Zatykó Helga.jpg"
                },
                {
                    name: "Csősz Beáta",
                    contact: "11.d osztályfőnök",
                    description: ["magyar nyelv és irodalom"],
                    img: "https://szbi-pg.hu/images/Tanarok/Csősz Beáta.jpg"
                },
                {
                    name: "Csuka Tibor",
                    contact: "9.d osztályfőnök",
                    description: ["informatika"],
                    img: "https://szbi-pg.hu/images/Tanarok/Csuka Tibor.jpg"
                },
                {
                    name: "Darabos Andrea Gabriella",
                    contact: "kollégiumi nevelőtanár",
                    description: [""],
                    img: "https://szbi-pg.hu/images/Tanarok/Darabos Andrea.JPG"
                },
                {
                    name: "Dongó Péter",
                    contact: "",
                    description: ["informatika"],
                    img: "https://szbi-pg.hu/images/Tanarok/Dongó Péter.jpg"
                },
                {
                    name: "Erdélyi Szabolcs",
                    contact: "9.b osztályfőnök",
                    description: ["testnevelés"],
                    img: "https://szbi-pg.hu/images/Tanarok/Erdélyi Szabolcs.JPG"
                },
                {
                    name: "Fazekas-Kis Szilvia",
                    contact: "",
                    description: ["angol nyelv", "német nyelv"],
                    img: "https://szbi-pg.hu/images/Tanarok/Fazekas-Kis-Szilvia.jpg"
                },
                {
                    name: "Fekete-Csenki Eszter",
                    contact: "",
                    description: ["angol nyelv"],
                    img: "https://szbi-pg.hu/images/Tanarok/Fekete Csenki Eszter.jpg"
                },
                {
                    name: "Fekete László Károly",
                    contact: "",
                    description: ["szakoktató"],
                    img: "https://szbi-pg.hu/images/Tanarok/Fekete László Károly.jpg"
                },
                {
                    name: "Grósz Erika",
                    contact: "",
                    description: ["hittan"],
                    img: "https://szbi-pg.hu/images/Tanarok/female.jpg"
                },
                {
                    name: "Gyöngyösi Csaba",
                    contact: "",
                    description: ["fizika"],
                    img: "https://szbi-pg.hu/images/Tanarok/Gyöngyösi Csaba.jpg"
                },
                {
                    name: "Havas Attila",
                    contact: "9.i osztályfőnök",
                    description: ["informatika"],
                    img: "https://szbi-pg.hu/images/Tanarok/Havas Attila.JPG"
                },
                {
                    name: "Hódi Ágnes",
                    contact: "",
                    description: ["számítástechnika"],
                    img: "https://szbi-pg.hu/images/Tanarok/Hódi Ágnes.jpg"
                },
                {
                    name: "Juhász Árpád István",
                    contact: "kollégiumi nevelőtanár",
                    description: [""],
                    img: "https://szbi-pg.hu/images/Tanarok/Juhász Árpád.jpg"
                },
                {
                    name: "Kálmán Gábor",
                    contact: "kollégiumi nevelőtanár",
                    description: [""],
                    img: "https://szbi-pg.hu/images/Tanarok/Kálmán Gábor.jpg"
                },
                {
                    name: "Kiss Gábor István",
                    contact: "11.i osztályfőnök",
                    description: ["informatika"],
                    img: "https://szbi-pg.hu/images/Tanarok/Kiss Gábor.JPG"
                },
                {
                    name: "Kovács Dénes",
                    contact: "",
                    description: ["informatika"],
                    img: "https://szbi-pg.hu/images/Tanarok/Kovács Dénes.jpg"
                },
                {
                    name: "Kun Tímea",
                    contact: "",
                    description: ["angol nyelv"],
                    img: "https://szbi-pg.hu/images/Tanarok/Kun_Tímea.jpg"
                },
                {
                    name: "Maróthy Ádám",
                    contact: "",
                    description: ["angol nyelv", "történelem"],
                    img: "https://szbi-pg.hu/images/Tanarok/male.jpg"
                },
                {
                    name: "Messzi-Szabóné Major Márta",
                    contact: "10.d osztályfőnök",
                    description: ["angol nyelv", "történelem"],
                    img: "https://szbi-pg.hu/images/Tanarok/Messzi-Szabóné Major Márta.jpg"
                },
                {
                    name: "Michnáné Szabó Lilian",
                    contact: "",
                    description: ["angol nyelv", "történelem"],
                    img: "https://szbi-pg.hu/images/Tanarok/Szabó Lilian.jpg"
                },
                {
                    name: "Novák Olga",
                    contact: "9/knya osztályfőnök",
                    description: ["német nyelv"],
                    img: "https://szbi-pg.hu/images/Tanarok/Novák Olga.JPG"
                },
                {
                    name: "Palásti Ádám",
                    contact: "10.a osztályfőnök",
                    description: ["német nyelv"],
                    img: "https://szbi-pg.hu/images/Tanarok/Palásti Ádám.JPG"
                },
                {
                    name: "Pallagi Ernő Ferenc",
                    contact: "",
                    description: ["gépészmérnök"],
                    img: "https://szbi-pg.hu/images/Tanarok/Pallagi Ernő.jpg"
                },
                {
                    name: "Palotás Aranka Erzsébet",
                    contact: "",
                    description: ["magyar nyelv és irodalom", "angol nyelv"],
                    img: "https://szbi-pg.hu/images/Tanarok/Palotás Aranka.jpg"
                },
                {
                    name: "Patak Judit",
                    contact: "",
                    description: ["magyar nyelv és irodalom", "angol nyelv"],
                    img: "https://szbi-pg.hu/images/Tanarok/Patak Judit.jpg"
                },
                {
                    name: "Pásztor Zoltán Albert",
                    contact: "10.i osztályfőnök",
                    description: ["informatika"],
                    img: "https://szbi-pg.hu/images/Tanarok/Pásztor Zoltán.jpg"
                },
                {
                    name: "Preisz Csaba",
                    contact: "",
                    description: ["gépészmérnök"],
                    img: "https://szbi-pg.hu/images/Tanarok/Preisz Csaba.jpg"
                },
                {
                    name: "Preiszné Bene Mónika Melinda",
                    contact: "12.i osztályfőnök",
                    description: ["testnevelés"],
                    img: "https://szbi-pg.hu/images/Tanarok/Preiszné Bene Mónika.jpg"
                },
                {
                    name: "Sárkány Tamás",
                    contact: "",
                    description: ["gépészmérnök"],
                    img: "https://szbi-pg.hu/images/Tanarok/Sárkány Tamás.jpg"
                },
                {
                    name: "Simó Zsuzsanna",
                    contact: "12.a osztályfőnök",
                    description: ["matematika"],
                    img: "https://szbi-pg.hu/images/Tanarok/Simó Zsuzsanna.jpg"
                },
                {
                    name: "Süveges Zsolt Imre",
                    contact: "5/13.a osztályfőnök",
                    description: ["gépészmérnök"],
                    img: "https://szbi-pg.hu/images/Tanarok/Süveges Zsolt.JPG"
                },
                {
                    name: "Szél Nikoletta",
                    contact: "",
                    description: ["matematika"],
                    img: "https://szbi-pg.hu/images/Tanarok/Szél Nikoletta.jpg"
                },
                {
                    name: "Szijártó Sándor",
                    contact: "2/14.i osztályfőnök",
                    description: ["informatika", "fizika"],
                    img: "https://szbi-pg.hu/images/Tanarok/Szijártó_Sándor.jpg"
                },
                {
                    name: "Tóth Levente Zsoltné",
                    contact: "9.a osztályfőnök",
                    description: ["német nyelv"],
                    img: "https://szbi-pg.hu/images/Tanarok/Tóth Levente Zsoltné.JPG"
                },
                {
                    name: "Tóth Petra Dóra",
                    contact: "11.b osztályfőnök",
                    description: ["történelem", "német nyelv"],
                    img: "https://szbi-pg.hu/images/Tanarok/Tóth Petra.jpg"
                },
                {
                    name: "Tóth Tamás",
                    contact: "",
                    description: ["műszaki szakoktató"],
                    img: "https://szbi-pg.hu/images/Tanarok/Tóth Tamás.jpg"
                },
                {
                    name: "Törköly Csaba",
                    contact: "",
                    description: ["gépészmérnök"],
                    img: "https://szbi-pg.hu/images/Tanarok/Törköly Csaba.JPG"
                },
                {
                    name: "Vas Viola",
                    contact: "9.c osztályfőnök",
                    description: ["magyar nyelv és irodalom", "angol nyelv"],
                    img: "https://szbi-pg.hu/images/Tanarok/Vas Viola.jpg"
                },
                {
                    name: "Verebné Lénárt Judit",
                    contact: "9/knyd osztályfőnök",
                    description: ["angol nyelv"],
                    img: "https://szbi-pg.hu/images/Tanarok/Verebné Lénárt Judit.jpg"
                },
                {
                    name: "Vincze Zsolt",
                    contact: "10.b osztályfőnök",
                    description: ["történelem", "földrajz"],
                    img: "https://szbi-pg.hu/images/Tanarok/Vincze Zsolt.jpg"
                }
            ]
        },
        {
            title: "Óraadó oktatók",
            people: [
                {
                    name: "Alács Gyula",
                    contact: "",
                    description: ["testnevelés"],
                    img: "https://szbi-pg.hu/images/Tanarok/Alács Gyula.jpg"
                },
                {
                    name: "Buri Gábor Sándor",
                    contact: "műszaki vezető",
                    description: ["műszaki szakoktató"],
                    img: "https://szbi-pg.hu/images/Tanarok/Buri Gábor.JPG"
                },
                {
                    name: "Czakóné Kállai Ildikó",
                    contact: "",
                    description: ["fejlesztőpedagógus"],
                    img: "https://szbi-pg.hu/images/Tanarok/Czakóné Kállai Ildikó.jpg"
                },
                {
                    name: "Csenkiné Bihal Mária Magdolna",
                    contact: "",
                    description: ["gépírás"],
                    img: "https://szbi-pg.hu/images/Tanarok/Csenkiné Bihal Mária.jpg"
                },
                {
                    name: "Födő-Vargek Eleanor Elizabeth",
                    contact: "",
                    description: ["angol lektor"],
                    img: "https://szbi-pg.hu/images/Tanarok/Fördő-Vargek Eleanor.jpg"
                },
                {
                    name: "Gémesné Farkas Anikó",
                    contact: "",
                    description: ["fejlesztőpedagógus"],
                    img: "https://szbi-pg.hu/images/Tanarok/Gémesné Farkas Anikó.jpg"
                },
                {
                    name: "Göcs László",
                    contact: "",
                    description: ["informatika"],
                    img: "https://szbi-pg.hu/images/Tanarok/Göcs László.jpg"
                },
                {
                    name: "Kovács Éva",
                    contact: "",
                    description: ["gépészmérnök"],
                    img: "https://szbi-pg.hu/images/Tanarok/Kovács Éva.jpg"
                },
                {
                    name: "Meissner Eve-Marie",
                    contact: "",
                    description: ["német lektor"],
                    img: "https://szbi-pg.hu/images/Tanarok/Eve-Marie Meissner.jpg"
                }
            ]
        },
        {
            title: "Technikai dolgozók",
            people: [
                {
                    name: "Bodor László",
                    contact: "",
                    description: ["karbantartó"],
                    img: "https://szbi-pg.hu/images/Dolgozok/Bodor László.jpg"
                },
                {
                    name: "Bóbis Gyöngyike",
                    contact: "",
                    description: ["intézményi takarító"],
                    img: "https://szbi-pg.hu/images/Dolgozok/Bóbis Gyöngyike.jpg"
                },
                {
                    name: "Csuka Zoltán József",
                    contact: "",
                    description: ["karbantartási vezető"],
                    img: "https://szbi-pg.hu/images/Dolgozok/Csuka Zoltán.jpg"
                },
                {
                    name: "Drozdik Katalin",
                    contact: "",
                    description: ["intézményi takarító"],
                    img: "https://szbi-pg.hu/images/Dolgozok/Drozdik Katalin.jpg"
                },
                {
                    name: "Hegedűsné Mizsei Mónika",
                    contact: "",
                    description: ["intézményi takarító"],
                    img: "https://szbi-pg.hu/images/Dolgozok/Hegedűsné Mizsei Mónika.jpg"
                },
                {
                    name: "Horváth Viktor János",
                    contact: "",
                    description: ["portás", "karbantartó"],
                    img: "https://szbi-pg.hu/images/Dolgozok/Horváth Viktor.jpg"
                },
                {
                    name: "Juhász Mihály Sándor",
                    contact: "",
                    description: ["fűtő"],
                    img: "https://szbi-pg.hu/images/Dolgozok/Juhász Mihály.jpg"
                },
                {
                    name: "Kassainé Komló Ilona",
                    contact: "",
                    description: ["iskolatitkár"],
                    img: "https://szbi-pg.hu/images/Dolgozok/Kassainé Komló Ilona.jpg"
                },
                {
                    name: "Kiss Péter Ferenc",
                    contact: "",
                    description: ["rendszergazda"],
                    img: "https://szbi-pg.hu/images/Dolgozok/Kiss Péter Ferenc.jpg"
                },
                {
                    name: "Kovács István Zoltán",
                    contact: "",
                    description: ["gépszerelő", "karbantartó"],
                    img: "https://szbi-pg.hu/images/Dolgozok/Kovács István Zoltán.jpg"
                },
                {
                    name: "Nagy Margit Veronika",
                    contact: "",
                    description: ["iskolatitkár"],
                    img: "https://szbi-pg.hu/images/Dolgozok/Nagy Margit.jpg"
                },
                {
                    name: "Nagyné Gulyás Zsuzsanna Margit",
                    contact: "",
                    description: ["intézményi takarító"],
                    img: "https://szbi-pg.hu/images/Dolgozok/Nagyné Gulyás Zsuzsanna.jpg"
                },
                {
                    name: "Ördög József",
                    contact: "",
                    description: ["villanyszerelő", "karbantartó"],
                    img: "https://szbi-pg.hu/images/Dolgozok/Ördög József.jpg"
                },
                {
                    name: "Szabó Judit",
                    contact: "",
                    description: ["marketing asszisztens"],
                    img: "https://szbi-pg.hu/images/Dolgozok/Szabó Judit.jpg"
                },
                {
                    name: "Tarjányi Beáta",
                    contact: "",
                    description: ["intézményi takarító"],
                    img: "https://szbi-pg.hu/images/Dolgozok/Tarjányi Beáta.jpg"
                },
                {
                    name: "Tarjányi Mihály",
                    contact: "",
                    description: ["kollégiumi ügyelő", "karbantartó"],
                    img: "https://szbi-pg.hu/images/Dolgozok/Tarjányi Mihály.jpg"
                },
                {
                    name: "Törökné Varga Julianna",
                    contact: "",
                    description: ["intézményi takarító"],
                    img: "https://szbi-pg.hu/images/Tanarok/female.jpg"
                },
                {
                    name: "Urbán Illésné",
                    contact: "",
                    description: ["intézményi takarító"],
                    img: "https://szbi-pg.hu/images/Dolgozok/Urbán Illésné.jpg"
                }
            ]
        }
    ];
</script>

<svelte:head>
    <title>Munkatársaink</title>
</svelte:head>

<div id="content">
    {#each data as section}
        <div class="section">
            <h2 class="section-title">{section.title}</h2>
            <div class="section-content">
                {#each section.people as person}
                    <div class="person">
                        <img src={person.img} alt="" />
                        <h3 class="name">{person.name}</h3>
                        <p class="contact">{person.contact}</p>
                        <div class="description">
                            {#each person.description as descLine}
                                <p>{descLine}</p>
                            {/each}
                        </div>
                    </div>
                {/each}
            </div>
        </div>
    {/each}
</div>

<style lang="scss">
    #content {
        display: flex;
        flex-direction: column;
        width: 100%;
        height: 100%;
        padding-left: 10vw;
        padding-right: 10vw;
        gap: 5rem;

        .section {
            .section-title {
                margin-bottom: 0.8rem;
            }

            .section-content {
                display: flex;
                flex-direction: row;
                flex-wrap: wrap;
                gap: 3rem;

                .person {
                    width: 15rem;

                    img {
                        width: 100%;
                    }

                    .contact {
                        font-weight: bold;
                        margin-bottom: 0.5rem;
                    }
                }
            }
        }
    }
</style>
