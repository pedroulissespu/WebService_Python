import json , requests

#Para inserir os dados , vamos criar entao uma variavel que vai armazenar esses dados
dados = data={"postId": 1, "name": "John Doe", "email": "john@doe.com", "body": "This is it!"}
#Data vai ser necessario para dizer o tipo na hora de salvar para JSON
response = requests.post("http://jsonplaceholder.typicode.com/comments/", data=dados)
#No da requisição GET estavamos usando GET para obter os dados , agr como vai ser usado o POST , vai ser
#Requests.post
#E colocando o data = dados para dizer que aquilo é os dados salvos
#Para ver se deu certo :
print(response.status_code)

#E para ver os dados que foram colocados : 
print(response.content)