import json , requests

#Alterar dados
dados = {"email": "john@doe.com"}
response = requests.post("http://jsonplaceholder.typicode.com/comments/10", data=dados)