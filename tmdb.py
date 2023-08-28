import requests
api_key = "d1da20fbfa65312b857fb7b517bf855c"

genres = [
    {'id': 28, 'name': 'Action'}, 
    {'id': 12, 'name': 'Adventure'}, 
    {'id': 16, 'name': 'Animation'}, 
    {'id': 35, 'name': 'Comedy'}, {'id': 80, 'name': 'Crime'}, {'id': 99, 'name': 'Documentary'}, {'id': 18, 'name': 'Drama'}, {'id': 10751, 'name': 'Family'}, {'id': 14, 'name': 'Fantasy'}, {'id': 36, 'name': 'History'}, {'id': 27, 'name': 'Horror'}, {'id': 10402, 'name': 'Music'}, {'id': 9648, 'name': 'Mystery'}, {'id': 10749, 'name': 'Romance'}, {'id': 878, 'name': 'Science Fiction'}, {'id': 10770, 'name': 'TV Movie'}, {'id': 53, 'name': 'Thriller'}, {'id': 10752, 'name': 'War'}, {'id': 37, 'name': 'Western'}]

def get_genero_id(id):
    """ retorna o nome do genero de acordo com o id """
    pass

# teste:
# get_genero_id(28) # Action

# ====================================
def get_json(endpoint, params=None):
    """ 
    fornecido o endpoint faz o request e retorna o resultado em json
    """
    url = f"{endpoint}{params}&api_key={api_key}"
    response = requests.get(url)
    return response.json()

# ====================================
def filmes_populares():
    """ Obtem os filmes mais populares usando endpoint discover """

    data = get_json(
        "https://api.themoviedb.org/3/discover/movie",
        "?sort_by=vote_count.desc"
    )
    results = data['results']
    print("="*20)
    for movie in results:
        print(movie['original_title']) 
        print(movie['id']) 
        print(movie['genre_ids'])
        print(movie['vote_count']) 
        print("----")
    print(f"Total: {len(results)}")

def get_generos():
    """ Obter a lista de generos """
    data = get_json(
        "https://api.themoviedb.org/3/genre/movie/list",
        "?language=en"
    )
    results = data['genres']
    print(results)



if __name__ == "__main__":
    # filmes_populares()
    get_generos()

