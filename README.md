# Desenvolvimento Web IV - 2023

- [Moodle](https://ava.ifpr.edu.br/course/view.php?id=10808)


## Aula 02

Exemplo de API com FastAPI

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

## start fastapi

```bash
uvicorn main:app --reload
```
