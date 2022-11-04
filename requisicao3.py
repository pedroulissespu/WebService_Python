import json , requests

#Importa as bibliotecas json e requests
#Json : Serve para carregar os arquivos JSON
#Requests : Serve para realizar as requisiçõe HTTP para consumir nossa API

#Fazer Requisições : Método GET

response = requests.get("http://jsonplaceholder.typicode.com/comments")
conteudo = json.loads(response.content)
#Aqui vai estar sendo realizado a leitura dos dados disponiveis no JSON do response

print(conteudo) #Para confirma podemos estar testando pelo print

#Com isso podemos estar fazendo certas operações com os dados , como por exemplo :
for conteudo in conteudo[0:10]:
    print(conteudo['name'] , " " , conteudo['email'])