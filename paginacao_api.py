
import requests

from time import sleep


api_url = "http://localhost:8080/produtos/"
param_nome = "pagina"

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
