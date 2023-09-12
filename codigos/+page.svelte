<script>
  /* iniciar o servidor:
  npm run dev 
  */
	let promise = getFilmes();
	async function getFilmes() {
    // faz um request GET para endpoint /filmes
		const res = await fetch(`http://localhost:8000/filmes`);
		const text = await res.json();
		if (res.ok) { return text; } 
    else { throw new Error(text);}
	}
	function handleClick() {
		promise = getFilmes();
	}
</script>

<button on:click={handleClick}> Get filmes </button>

{#await promise}
	<p>...loading</p>
{:then filmes}
  <h1>Lista de filmes</h1>
  
  {#each filmes as filme}
		<p>{filme.title}</p>
	{/each}

{:catch error}
	<p style="color: red">{error.message}</p>
{/await}
