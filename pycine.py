from fastapi import FastAPI
from tmdb import get_json
app = FastAPI()

from fastapi.middleware.cors import (
     CORSMiddleware
)
# habilita CORS (permite que o Svelte acesse o fastapi)
origins = [
    "http://localhost",
    "http://localhost:5173",
    "http://localhost:5174",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ========================================================

# ATIVIDADE 1

@app.get("/filme/{title}")
async def find_movie(title: str):
    """ 
    procura filmes pelo titulo e ordena pelos mais populares 
    Exemplo: /filme/avatar
    """
    return {"title": title}

# ========================================================

# ATIVIDADE 2

@app.get("/artista/filmes")
async def find_filmes_artista(personId: int):
    """ 
    busca os filmes mais populares de um artista 
    Exemplo: /artista/filmes?personId=1100
    """
    return {"id": personId}

# ========================================================

@app.get("/filmes")
async def filmes_populares(limit=3):
    """ Obtem os filmes mais populares usando endpoint discover """
    data = get_json(
        "/discover/movie", "?sort_by=vote_count.desc"
    )
    results = data['results']
    filtro = []
    for movie in results:
        filtro.append({
            "title": movie['original_title'], 
            "image": 
               f"https://image.tmdb.org/t/p/w185{movie['poster_path']}"
        })
    return filtro

# Precisa implementar o endpoint artista/1100
# app.get("")
# https://api.themoviedb.org/3/person/1100/

@app.get("/artista/{name}")
async def get_artista(name: str):
    """ 
    obtem lista de artista pelo nome e popularidade 
    """
    data = get_json(
        "/search/person", f"?query={name}&language=en-US"
    )
    results = data['results']
    filtro = []
    for artist in results:
        filtro.append({
            'id': artist['id'],
            'name': artist['name'],
            'rank': artist['popularity']
        })
    # ordenar lista de artistas (filtro) pelo atributo rank
    filtro.sort(reverse=True, key=lambda artist:artist['rank'])
    # return data
    return filtro

# 1. ativar o env
# source env/bin/activate

# 2. iniciar o uvicorn
# uvicorn pycine:app --reload

# 3. abre no navegador
# localhost:8000/filmes
