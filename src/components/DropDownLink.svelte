<script lang="ts">
    interface Link {
        name: string;
        href: string;
    }
    export let href: Link[] = [];
</script>

<div class="dropdown-container">
    <a href="."><slot /></a>
    <div class="dropdown">
        {#each href as link}
            <a href={link.href} class="option">
                <div class="icon">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"
                        ><!--! Font Awesome Free 6.4.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. --><path
                            d="M256 512A256 256 0 1 0 256 0a256 256 0 1 0 0 512zm0-352a96 96 0 1 1 0 192 96 96 0 1 1 0-192z"
                        /></svg
                    >
                </div>
                {link.name}</a
            >
        {/each}
    </div>
</div>

<style lang="scss">
    a {
        text-decoration: none;
        color: black;
        text-transform: uppercase;

        &:hover {
            text-decoration-line: underline;
            text-decoration-thickness: 0.08rem;
        }
    }
    .dropdown-container {
        position: relative;

        &:hover {
            .dropdown {
                display: block;
            }
        }

        .dropdown {
            position: absolute;
            bottom: 0;
            left: 0;
            background-color: darken(white, 10);
            display: flex;
            flex-direction: column;
            gap: 2px;
            align-items: stretch;
            border: 1px solid black;
            z-index: 100;
            transition: opacity 1s ease;
            display: none;
            transform: translateY(100%);

            .option {
                padding: 1rem;
                background-color: darken(white, 2);
                width: 100%;
                display: flex;
                align-items: center;
                gap: 0.4rem;

                .icon {
                    min-width: 10px;
                    min-height: 10px;
                    max-width: 10px;
                    max-height: 10px;
                    position: relative;

                    svg {
                        width: 100%;
                        height: 100%;
                        position: absolute;
                        top: 0;
                        left: 0;
                    }
                }
            }
        }
    }
</style>
