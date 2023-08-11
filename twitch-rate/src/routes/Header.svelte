<script>
	import { page } from '$app/stores';
	import { Button, Modal, Label, Input, Checkbox } from 'flowbite-svelte';

	let homeIconPath = 'images/monke.png';

	let loginModal = false;
	let signInModal = false;
</script>

<header class="flex justify-between px-[3.125rem] p-2 text-white bg-[#5C17C5]">
	<div class="w-8 rounded-full">
		<a href="/">
			<img src={homeIconPath} alt="toluafMONKE" />
		</a>
	</div>

	<nav>
		<ul class="flex gap-4 p-2">
			<li aria-current={$page.url.pathname === '/' ? 'page' : undefined}>
				<a href="/">Home</a>
			</li>
			<li aria-current={$page.url.pathname === '/about' ? 'page' : undefined}>
				<a href="/about">About</a>
			</li>
			<li>
				<a aria-current="page" href="/">Ratings</a>
			</li>
			<li>
				<a aria-current="page" href="/">Rankings</a>
			</li>
		</ul>
	</nav>
	<div class="flex p-2">
		<button on:click={() => (loginModal = true)} class="flex gap-2">
			<svg fill="#FFFFFF" xmlns="http://www.w3.org/2000/svg" height="1.5rem" viewBox="0 0 512 512"
				><!--! Font Awesome Free 6.4.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. --><path
					d="M406.5 399.6C387.4 352.9 341.5 320 288 320H224c-53.5 0-99.4 32.9-118.5 79.6C69.9 362.2 48 311.7 48 256C48 141.1 141.1 48 256 48s208 93.1 208 208c0 55.7-21.9 106.2-57.5 143.6zm-40.1 32.7C334.4 452.4 296.6 464 256 464s-78.4-11.6-110.5-31.7c7.3-36.7 39.7-64.3 78.5-64.3h64c38.8 0 71.2 27.6 78.5 64.3zM256 512A256 256 0 1 0 256 0a256 256 0 1 0 0 512zm0-272a40 40 0 1 1 0-80 40 40 0 1 1 0 80zm-88-40a88 88 0 1 0 176 0 88 88 0 1 0 -176 0z"
				/></svg>
			<span>Sign In</span>
		</button>
	</div>

	<!-- Main modal -->
	<Modal bind:open={loginModal} size="xs" autoclose={false} class="w-full">
		<form method="POST" action="?/login" class="flex flex-col space-y-2">
			<h3 class="mb-0 text-xl font-medium text-gray-900 dark:text-white text-center">Sign in</h3>
			<hr />
			<Label class="space-y-2">
				<span>Email</span>
				<Input type="email" name="email" placeholder="name@company.com" required />
			</Label>
			<Label class="space-y-2">
				<span>Password</span>
				<Input type="password" name="password" placeholder="•••••" required />
			</Label>
			<div class="flex items-start">
				<Checkbox>Remember me</Checkbox>
				<a href="/" class="ml-auto text-sm text-purple-800 hover:underline dark:text-primary-500"
					>Lost password?</a
				>
			</div>
			<Button type="submit" class="w-full bg-[#5C17C5] hover:bg-[#5C17C5] hover:brightness-125">Login to your account</Button>
			<div class="text-sm font-medium text-gray-500 dark:text-gray-300 text-center">
				Not registered? <a
					href="/"
					class="text-purple-800 hover:underline dark:text-purple-500"
					on:click={() => {
						signInModal = true;
						loginModal = false;
					}}>Create account</a
				>
			</div>
		</form>
	</Modal>

	<Modal bind:open={signInModal} size="xs" autoclose={false} class="w-full">
		<form class="flex flex-col space-y-2" method="POST" action="?/register">
			<h3 class="mb-0 text-xl font-medium text-gray-900 dark:text-white text-center">
				Create Account
			</h3>
			<hr />
			<Label class="space-y-2">
				<span>Email</span>
				<Input type="email" name="email" placeholder="name@company.com" required />
			</Label>
			<Label class="space-y-2">
				<span>Username</span>
				<Input type="text" name="username" placeholder="hunter123" required />
			</Label>
			<Label class="space-y-2">
				<span>Password</span>
				<Input type="password" name="password" placeholder="•••••" required />
			</Label>
			<Label class="space-y-2">
				<span>Confirm Password</span>
				<Input type="password" name="confirm_password" placeholder="•••••" required />
			</Label>

			<Button type="submit" class="w-full1 bg-[#5C17C5] hover:bg-[#5C17C5] hover:brightness-125">Sign up</Button>
			<div class="text-sm font-medium text-gray-500 dark:text-gray-300 text-center">
				Have an Account? <a
					href="/"
					class="text-purple-800 hover:underline dark:text-primary-500"
					on:click={() => {
						signInModal = false;
						loginModal = true;
					}}>Log in</a
				>
			</div>
		</form>
	</Modal>
</header>
