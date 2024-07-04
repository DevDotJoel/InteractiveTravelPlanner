<script>
	import '../app.css';
	import 'bootstrap/dist/css/bootstrap.css';
	import scriptSrc from 'bootstrap/dist/js/bootstrap.bundle.js?url';
	import Navbar from '$lib/components/ui/navbar.svelte';
</script>

<svelte:head>
	<script src={scriptSrc}></script>
</svelte:head>
<Navbar />
<div class="container mt-2">
	<slot></slot>
</div>
