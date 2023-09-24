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
