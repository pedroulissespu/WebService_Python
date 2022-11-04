import json , requests

#Importa as bibliotecas json e requests
#Json : Serve para carregar os arquivos JSON
#Requests : Serve para realizar as requisiçõe HTTP para consumir nossa API

#Fazer Requisições : Método GET

response = requests.get("http://jsonplaceholder.typicode.com/comments")

print(response.content)
#Aqui vai estar sendo realizado o print de todo o conteudo disponivel no arquivo JSON
#Não vai estar sendo possivel realizar a manipulação com dados separados com a variavel response por si so
#Vai ser necessario criar uma outra variavel responsavel por realizar a leitura do conteudo JSON disponivel no response
#Para estar sendo possivel assim realizar o consumo dos dados obtidos