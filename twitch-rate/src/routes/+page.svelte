<script>
	import { Button, Card } from 'flowbite-svelte';
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
<section class="explanation-section flex flex-col mx-auto p-12">
	<div class="flex flex-col mx-auto gap-8 sm:flex-row">
		<Card img="/images/rate_graphic.jpg">
			<h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">Rate</h5>
			<p class="font-normal text-gray-700 dark:text-gray-400 leading-tight">
			  Rate your favorite streamers, to boost their discoverability!
			</p>
		</Card>
		<Card img="/images/vote_graphic.jpg">
			<h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">Vote</h5>
			<p class="font-normal text-gray-700 dark:text-gray-400 leading-tight">
			  Vote on the ratings of others to increase their Rating Trust!
			</p>
		</Card>
		<Card img="/images/discover_graphic.jpg">
			<h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">Discover</h5>
			<p class="font-normal text-gray-700 dark:text-gray-400 leading-tight">
			  Discover new Streamers that are reccommended to you best on your previous ratings!
			</p>
		</Card>
	</div>
	<Button color="purple" class="mx-auto button">Get Ranking!</Button>
</section>

<style>
	.splash-section {
		background-image: url('images/banner_img_1.jpg');
	}
</style>
