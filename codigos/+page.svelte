<script>
	let promise = getFilmes();
	async function getFilmes() {
    // faz um request GET para endpoint /filmes
		const res = await fetch(`http://localhost:8000/filmes`);
		const text = await res.text();
		if (res.ok) { return text; } 
    else { throw new Error(text);}
	}
	function handleClick() {
		promise = getFilmes();
	}
</script>

<button on:click={handleClick}> Get filmes </button>

{#await promise}
	<p>...waiting</p>
{:then number}
	<p>The number is {number}</p>
{:catch error}
	<p style="color: red">{error.message}</p>
{/await}
