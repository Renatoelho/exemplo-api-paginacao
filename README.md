# Criando uma API de modelo com paginação em FastAPI

O FastAPI é uma framework para criação de APIs de alta performance em Python. Neste tutorial, vamos criar uma API de modelo com recursos de paginação para ensinar como colocar isso em prática.

# Pré-requisitos
Para seguir este tutorial, você precisará ter os seguintes pré-requisitos instalados em sua máquina:

Python 3.8 ou superior
O gerenciador de pacotes pip

```bash
pip install -r requirements.txt
```

Para criar um ambiente virtual com pip e ativá-lo, siga os seguintes passos:

1. Abra o terminal e crie a 'exemplo-api-paginacao' pasta para armazenar o ambiente virtual.

```bash
mkdir -p exemplo-api-paginacao
```

2. acesse a pasta criada e use o seguinte comando para criar um ambiente virtual:

```bash
python3 -m venv .venv
```

3. Ative o ambiente virtual usando o seguinte comando:

```bash
source .venv/bin/python3
```

4. Instalando os requirements, basta abrir o terminal e digitar o seguinte comando:

```bash
pip install -r requirements.txt
```

> ***OBS:*** Quando quiser desativar o ambiente virtual, basta usar o comando *deactivate*.

Isso irá instalar o FastAPI e todas as dependências necessárias.

# Criando a API de Exemplo

Para começar, vamos criar um arquivo chamado app.py e adicionar o seguinte código:

```python

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

```

Para iniciar a API, basta rodar o seginte comando no terminal.

```bash
python3 app.py
```

Isso irá iniciar a API em http://localhost:8080.

# Para fazer a paginação da API use a biblioteca requests, siga os seguintes passos:

Importe a biblioteca requests e outras bibliotecas necessárias:

```python

import requests

from time import sleep

```

Defina a URL da API e o nome do parâmetro de paginação:

```python

api_url = "http://localhost:8080/produtos/"
param_nome = "pagina"

```

Faça um loop para fazer as chamadas de API e pagar os resultados:

```python

pagina = 1
while True:
    # Adicione o parâmetro de paginação à URL
    url = f"{api_url}?{param_nome}={pagina}"
    
    # Faça a chamada da API
    resposta = requests.get(url)
    
    # Carregue os dados da resposta
    dados = resposta.json()
    # Verifique se a resposta tem itens
    if len(dados) == 0:
        break

    # Faça alguma coisa com os dados aqui, como armazená-los em um banco de dados ou imprimi-los na tela
    print(f"Página de produtos número: {pagina} e os produtos são:\n{dados}")
    print("*"*50)
    
    # Incremente a página para a próxima iteração do loop
    pagina += 1

    # Aguarda 5 segundos...
    sleep(5)
```

Esse código faz um loop infinito que faz chamadas à API, incrementando o parâmetro de paginação a cada iteração. A cada chamada, ele verifica se a resposta tem produtos e, se tiver carrega os dados da resposta e faz algo com eles (no exemplo acima, estamos simplesmente imprimindo os dados na tela). Quando a resposta não tem mais itens (por exemplo, quando chegamos à última página), o loop é interrompido.

Para a paginação da API, basta rodar o seginte comando no terminal.

```bash
python3 paginacao_api.py
```
