#Essa parte do cliente.py vai ser relacionado para requisição WEB
import requests # o requests vai servir exatamente para realizar as requisições
data = {"username" : "Pedro1" , "secret" : "root","info":"salario","value": 5000}
response = requests.get("http://127.0.0.1:5000/empregados/cargo/analista")

print(response) #Com isso vamos obter apenas a resposta do servidor
#Para obter o conteudo , vai ser necessario : 
print(response.text)
#E para verificar o tipo da resposta :
print(type(response.text))
#Podemos também , inves de usar .text do response , salvar os dados JSON em uma variavel
message = response.json()
print(message)
#E se eu quiser fazer a mesma coisa de ver o tipo da resposta
print(type(message))
#Agora vai aparecer que é do tipo dicionario , ou seja , agora consigo navegar sem problemas pelos dados fornecidos pelo nosso JSON
#Assim entao podemos fazer a seguinte coisa :
print(message['empregados'])

response = requests.post("http://127.0.0.1:5000/informations" , data = data)

if response.status_code == 200:
    message = response.json()
    print(message['empregados'])
else:
    print(response.status_code)