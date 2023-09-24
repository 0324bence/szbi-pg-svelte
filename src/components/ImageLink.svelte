<script lang="ts">
    export let image: string;
    export let title: string;
    export let subtitle: string;
    export let link: string;
</script>

<a class="image-link" href={link}>
    <img src={image} alt="{title} image" />
    <div class="texts">
        <p class="subtitle">{subtitle}</p>
        <div class="title-box">
            <p class="title">{title}</p>
        </div>
    </div>
</a>

<style lang="scss">
    .image-link {
        color: white;
        display: block;
        width: 100%;
        position: relative;
        height: fit-content;
        padding: 0;
        line-height: 0;

        img {
            width: 100%;
        }

        .texts {
            transition: color 400ms ease, background-color 400ms ease;
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            overflow: hidden;

            &:hover {
                background-color: rgba(0, 0, 0, 0.5);

                .title-box {
                    transform: translateY(100%);
                }

                .subtitle {
                    transform: translateY(0);
                    opacity: 1;
                }
            }

            p {
                text-transform: uppercase;
                font-family: Open Sans, sans-serif;
                line-height: normal;
                transition: opacity 0.2s, transform 0.35s;
            }

            .subtitle {
                font-size: 0.9rem;
                margin: 1em;
                margin-top: 1.2em;
                color: rgba(255, 255, 255, 0.8);
                transform: translateY(100%);
                opacity: 0;
            }

            .title-box {
                width: 100%;
                height: 15%;
                background-color: rgba(255, 255, 255, 0.7);
                color: black;
                display: flex;
                align-items: center;
                padding: 10px;
                font-weight: 600;
                transition: transform 0.35s;
            }
        }
    }
</style>
