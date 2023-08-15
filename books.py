from fastapi import FastAPI
from datetime import datetime
import json

app = FastAPI()

# retorna um livro de acordo com o id
# exemplo endpoint: /book/2
@app.get("/book/{id}")
def get_book(id: int):
    with open("data/books.json") as f:
        data = json.load(f)
        for item in data:
            if item['id'] == id:
                return item
    return { "error": f"book id=[{id}] not found" }

# 2. Busca por ano

# 3. Busca por título

# 4. Busca por authors (usar o arquivo data/booksV2.json )

# iniciar o servidor web pelo terminal:
# uvicorn books:app --reload
# testar pelo terminal
# http :8000/book/1