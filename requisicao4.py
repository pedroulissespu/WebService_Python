import json , requests

response = requests.get("http://jsonplaceholder.typicode.com/comments/1")
#Acessando conteudo especifico de um objeto , no caso quero do objeto 1

conteudo = json.loads(response.content) #Carregando os dados
print (conteudo['name']) #Carregar apenas o nome do Objeto 1