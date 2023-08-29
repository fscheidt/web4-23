import requests
api_key = "d1da20fbfa65312b857fb7b517bf855c"

genres = [
    {'id': 28, 'name': 'Action'}, 
    {'id': 12, 'name': 'Adventure'}, 
    {'id': 16, 'name': 'Animation'}, 
    {'id': 35, 'name': 'Comedy'}, {'id': 80, 'name': 'Crime'}, {'id': 99, 'name': 'Documentary'}, {'id': 18, 'name': 'Drama'}, {'id': 10751, 'name': 'Family'}, {'id': 14, 'name': 'Fantasy'}, {'id': 36, 'name': 'History'}, {'id': 27, 'name': 'Horror'}, {'id': 10402, 'name': 'Music'}, {'id': 9648, 'name': 'Mystery'}, {'id': 10749, 'name': 'Romance'}, {'id': 878, 'name': 'Science Fiction'}, {'id': 10770, 'name': 'TV Movie'}, {'id': 53, 'name': 'Thriller'}, {'id': 10752, 'name': 'War'}, {'id': 37, 'name': 'Western'}]

def get_genero_id(id):
    """ retorna o nome do genero de acordo com o id """
    ids = []
    names = []
    if type(id) == list:
        ids = id
    else:
        ids.append(id)
    for genre in genres:
        if genre['id'] in ids:
            names.append(genre)
    return names

# ====================================

def get_json(endpoint, params=None):
    """ 
    fornecido o endpoint faz o request e retorna o resultado em json
    """
    url = f"https://api.themoviedb.org/3{endpoint}{params}&api_key={api_key}"
    response = requests.get(url)
    return response.json()

# ====================================

def filmes_populares(limit=3):
    """ Obtem os filmes mais populares usando endpoint discover """
    data = get_json(
        "/discover/movie", "?sort_by=vote_count.desc"
    )
    results = data['results']
    print("="*20)
    c=1
    for movie in results:
        print(c)
        print(movie['original_title']) 
        print(movie['id']) 
        print(movie['genre_ids'])
        generos = [g['name'] for g in get_genero_id(movie['genre_ids'])]
        print(generos)
        # print(get_genero_id(movie['genre_ids']))
        print(movie['vote_count']) 
        print("----")
        c+=1
        if c > limit: break
    print(f"Total: {len(results)}")
    return results

# ====================================
# endpoint /person
def get_artista():
    """ fornecido o nome do artista retorna sua bio """
    pass

# ====================================

def get_tmdb_genres(lang="us"):
    """ Obter a lista de generos """
    data = get_json(
        "/genre/movie/list", f"?language={lang}"
    )
    results = data['genres']
    return results

# ====================================

if __name__ == "__main__":
    # print(get_genero_id(12))
    filmes_populares()
    # teste:
    # print(get_tmdb_genres())
    # print(get_genero_id(28)) # Action
    # print(get_genero_id([28,12])) # Action
