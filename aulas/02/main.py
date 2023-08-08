from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

# app é o framework fastapi
# define uma rota ou endpoint, localhost:8000/hora
# GET
@app.get("/hora") # <== endpoint
def horacerta():
    return { 
        "hora": datetime.now(),
        "tz": datetime.astimezone(tz=12),
        "local": "BR"
    }

@app.get("/upper/{nome}") # <== endpoint
def upper(nome):
    return { 
        "nome": nome,
        "upper": nome.upper()
    }


# Criar ao endpoint que realização a ação:
# Exercício 1 - retornar JSON indicando se numero é 
# "PAR" ou "IMPAR"

# Exercício 2 - Informar 3 horarios, de acordo com 
# a cidade que usuário brasilia, tokyo, londres.
# GET localhost:8000/hora/tokyo

# Ex. 3 - Dia da semana (segunda, terça, ...)
# /diasemana
# -> "segunda-feira"


# iniciar o servidor web pelo terminal:
# uvicorn main:app --reload