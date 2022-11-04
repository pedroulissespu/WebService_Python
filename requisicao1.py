import json , requests

#Importa as bibliotecas json e requests
#Json : Serve para carregar os arquivos JSON
#Requests : Serve para realizar as requisiçõe HTTP para consumir nossa API

#Fazer Requisições : Método GET

response = requests.get("http://jsonplaceholder.typicode.com/comments")
#Response vai ser nossa variavel responsavel por fazer a requisição e pegar os dados presentes.

print(response.status_code)
#Aqui vai estar sendo realizado o print do STATUS da nossa requisição , se sair 200 é por que foi um sucesso