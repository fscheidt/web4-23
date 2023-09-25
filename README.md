# Desenvolvimento Web IV - 2023

- [Moodle](https://ava.ifpr.edu.br/course/view.php?id=10808)

## Front (svelte)
- https://github.com/fscheidt/front

## Aula 07
Adicionar ao `pycine.py`

```python
from fastapi.middleware.cors import (
     CORSMiddleware
)
# habilita CORS (permite que o Svelte acesse o fastapi)
origins = [
    "http://localhost",
    "http://localhost:5173",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## Aula 04

- Integração python com API TMDB - [tmdb.py](tmdb.py)

## Aula 02

Tópicos:

- Setup do ambiente de desenvolvimento python
	- criação do virtual env
	- instalação das dependências: fastapi e uvicorn
- Implementação: exemplo básico de API
- FastApi framework (conceitos):
	- Verbos: GET, POST, DELETE, PUT
	- Endpoint (recurso)
	- Síncrono vs Assíncrono
	- Serialização
    - Parâmetros url
- Teste e documentação
	- curl/http GET request
	- docs (post)


### ambiente python

Setup inicial do ambiente de desenvolvimento:

```bash
# 1. criar pasta do projeto
# mkdir projeto
# cd projeto
# 2. criar ambiente virtual
python3 -m venv env
# 3. ativar ambiente virtual
source env/bin/activate
# 4. instalar dependências
pip install fastapi uvicorn
code .
```

### Exemplo de API

Criar arquivo `main.py`

```python
from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

```

### iniciar fastapi

```bash
uvicorn main:app --reload
```

---

<details>
<summary><b>Utilitários</b></summary>

**httpie**

```bash
sudo apt-get install httpie
# ou
sudo snap install httpie
```

</details>