
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    nome: str
    descricao: str
    preco: float

@app.get("/produtos/")
async def read_items(pagina: int=-1):
    items = [
        {"nome": "Arroz", "descricao": "grão completo que é uma opção mais saudável", "preco": 10.99},
        {"nome": "Frutas", "descricao": "nutritiva para adicionar às refeições e lanches", "preco": 12.99},
        {"nome": "Legumes", "descricao": "nutritivo para adicionar às refeições e lanches", "preco": 15.99},
        {"nome": "Queijo", "descricao": "feito com leite de ovelha ou vaca", "preco": 25.99},
        {"nome": "Carne moída", "descricao": "pode ser usada em muitos pratos", "preco": 17.99}
    ]
    if pagina > 0:
        tamanho_pagina = 2
        inicio_index = (tamanho_pagina * pagina) - tamanho_pagina
        fim_index = inicio_index + tamanho_pagina

        return items[inicio_index:fim_index]
    
    elif pagina == 0:
        return {}

    else:
        return items

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app="app:app",
        host="0.0.0.0",
        port=8080,
        log_level="info",
        reload=True
    )
