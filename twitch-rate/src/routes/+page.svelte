<script>
	import { Button, Card, Label, Input, Accordion, AccordionItem } from 'flowbite-svelte';
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
<section id="intro-section" class="px-24 pt-12">
	<div class="pl-36">
		<div class="text-7xl font-bold mb-8">This is Streamer Ranker</div>
		<div class="text-3xl font-bold text-gray-500 w-3/4 pb-8">Streamer Ranker is a platform where you can help your favorite small streamers grow their audience. All you have to do is rate, vote, and discover.</div>
		<Accordion flush class="w-3/4">
			<AccordionItem>
				<span slot="header" class="text-4xl font-bold text-black">Rate</span>
				<p class="text-xl font-bold text-black">Rating means you just find your favorite streamers, and do a quick rating of their stream by filling out our super short survey.</p>
			</AccordionItem>
			<AccordionItem>
				<span slot="header" class="text-4xl font-bold text-black">Vote</span>
				<p class="text-xl font-bold text-black">Voting is when you look at the ratings of your fellow viewers and chatters, and upvote or downvote them depending on how accurate you believe them to be, this allows us to decide exactly how does an audience feel about a creator. </p>
			</AccordionItem>
			<AccordionItem>
				<span slot="header" class="text-4xl font-bold text-black">Discover</span>
				<p class="text-xl font-bold text-black">Then we take all of this information, and combine it with analytics and statistics from Twitch, and we give you a list of new small streamers we think you'll enjoy. </p>
			</AccordionItem>
		</Accordion>
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
<section id="email-section" class="flex flex-col text-center bg-gray-300 py-8">
	<h1 class="text-5xl font-bold">Keep In Touch!</h1>
	<p>Enter your email, to know when we enter into beta.</p>
	<div class='mb-6 w-96 mx-auto'>
		<Label for='default-input' class='block mb-2'></Label>
		<Input id='default-input' placeholder="smith@example.com" />
	</div>
</section>

<style>
	.splash-section {
		background-image: url('images/banner_img_1.jpg');
	}
</style>
