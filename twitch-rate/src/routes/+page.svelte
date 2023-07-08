<script>
	import { Button } from 'flowbite-svelte';
	const bannerImg = "images/banner_img_1.jpg";
</script>

<svelte:head>
	<title>Home</title>
	<meta name="description" content="Svelte demo app" />
</svelte:head>

<section class="splash-section flex flex-col justify-center w-full h-[70dvh] bg-center bg-cover text-white font-bold ">
		<div class="flex flex-col mt-[10rem]">
			<h1 class="drop-shadow-[0_4.2px_4.2px_rgba(0,0,0,0.8)] text-5xl inline-block">Welcome to <br> Streamer Ranker</h1>
			<div class="mt-8 mx-auto flex gap-8">
				<Button class="p-2 w-24 min-w-max bg-white text-black hover:bg-white hover:brightness-90 font-bold mx-auto">Learn More</Button>
				<Button class="p-2 w-24 min-w-max bg-[#5C17C5] hover:bg-[#5C17C5] hover:brightness-125">Get Started</Button>
			</div>
		</div>
</section>

<style>
	.splash-section {
		background-image: url('images/banner_img_1.jpg');
	}
</style>
