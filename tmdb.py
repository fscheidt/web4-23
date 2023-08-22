import requests
# pip install fastapi uvicorn requests
api_key = "SUA_CHAVE_AQUI"

endpoint = "https://api.themoviedb.org/3/discover/movie"
# params = "?include_adult=false&include_video=false&language=en-US&page=1&sort_by=popularity.desc"
params = "?sort_by=vote_count.desc"
url = f"{endpoint}{params}&api_key={api_key}"
headers = {"accept": "application/json"}

# Faz a requisição GET para a url
# salva na variavel response o resultado da busca no tmdb
response = requests.get(url, headers=headers)
# converter a resposta da API para um objeto python (dictionary)
data = response.json()

# imprime a pagina do resultado
page = data['page']
print(f"page: {page}")

# obtem o primeiro filme do resultado
# filme1 = data['results'][0]
# print(filme1)

# Obtem apenas o tituto do primeiro filme
# print(filme1['original_title'])

# IMPRIMIR o titulo de todos os filmes em "data"

results = data['results']
print("="*20)
for movie in results:
    print(movie['original_title']) 
    print(movie['id']) 
    print(movie['genre_ids'])
    print(movie['vote_count']) 
    print("----")

print(f"Total: {len(results)}")

# Obter o nome dos generos
# 
end = f"https://api.themoviedb.org/3/genre/movie/list"
params = "?language=en"
url = f"{end}{params}&api_key={api_key}"

# imprimir os filmes (titulo) e o nome dos generos

