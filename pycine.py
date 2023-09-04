from fastapi import FastAPI
from tmdb import get_json
app = FastAPI()

@app.get("/filme/{title}")
async def find_movie(title: str):
    """  """
    pass

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
    # ordenar filtro pelo atributo rank
    filtro.sort(reverse=True, key=lambda artist:artist['rank'])
    # return data
    return filtro

