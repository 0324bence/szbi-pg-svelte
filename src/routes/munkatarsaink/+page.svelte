<script>
    import data from "./data.json";
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

    @media screen and (max-width: 1100px) {
        .section-title {
            text-align: center;
        }
        .section-content {
            flex-direction: column !important;
            align-items: center;
        }
    }
</style>
