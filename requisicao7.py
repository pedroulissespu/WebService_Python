import json , requests

#Removendo dados
response = requests.delete("http://jsonplaceholder.typicode.com/comments/10")