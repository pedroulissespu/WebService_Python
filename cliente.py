#Essa parte do cliente.py vai ser relacionado para requisição WEB
import requests # o requests vai servir exatamente para realizar as requisições
response = requests.get("http://127.0.0.1:5000/empregados/cargo/analista")

print(response) #Com isso vamos obter apenas a resposta do servidor
#Para obter o conteudo , vai ser necessario : 
print(response.text)