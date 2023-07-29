<script>				
	import Header from './Header.svelte';
	import './styles.css';
	import '../app.css';
	let homeIconPath = 'images/monke.png';

	// placeholder for sitemap
	let items = ['item 1', 'item 2', 'item 3', 'item 4', 'item 5']
	let lists = ['List 1', 'List 2', 'List 3', 'List 4']

</script>

<div class="app">
	<Header />

	<main>
		<slot />
	</main>

	<footer class="flex flex-col">
		<div id="sitemap" class="mx-auto bg-[#5C17C5] w-full mt-[-1rem] py-4 flex justify-evenly">
			<div id="logo">
				<h1 class="text-xl text-white font-bold">Streamer Ranker</h1>
				<div class="w-24 mx-auto rounded-full">
					<a href="/">
						<img src={homeIconPath} alt="toluafMONKE" />
					</a>
				</div>
			</div>
			<div id="links" class="flex justify-between text-white font-bold text-lg">
				{#each lists as list}
					<div id={list} class="">
						<h1>{list}</h1>
						<ul class="mx-8">
							{#each items as item}
								<li><a href="/">{item}</a></li>
							{/each}
						</ul>
					</div>
				{/each}
			</div>
		</div>
		<div class="bg-black text-white font-bold w-full text-center py-2">
			<p>StreamerRanker All Rights Reserved &copy;</p>
		</div>
	</footer>
</div>

<style>
	.app {
		display: flex;
		flex-direction: column;
		min-height: 100vh;
	}

	main {
		flex: 1;
		display: flex;
		flex-direction: column;
		width: 100%;
		box-sizing: border-box;
	}

	footer {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		padding: 12px;
	}

	footer a {
		font-weight: bold;
	}

	@media (min-width: 480px) {
		footer {
			padding: 12px 0;
		}
	}
</style>
