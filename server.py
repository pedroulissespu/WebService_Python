#conda install flask -> instalar com anaconda
#pip install flask -> instalar o flask com o gerenciador de arquivos do Python
from flask import Flask # Importando o Flask

empregados = [
                {'nome' : 'Valentina', 'cargo' : 'Analista' , 'salario' : 5000},
                {'nome' : 'Joao', 'cargo' : 'Analista' , 'salario' : 3000},
                {'nome' : 'Moises', 'cargo' : 'Garota de Programa' , 'salario' : 9999999}
            ] #Dados ficticios em modelo JSON
#O motivo de usar JSON é por conta que o JSON é muito mais rápido comparado com o XML
#Além da sua sintaxe ser simples e de compreensão facil

app = Flask(__name__) #Construindo o APP

@app.route("/") #Decorator para a requisição da pagina inicial
def home():
    return "<h1>Pagina Principal</h1>"

@app.route("/empregados") #Decorator para a requisição da pagina com dados dos empregados
def get_empregados():
    return{'empregados': empregados} #Retorna todos os empregados

@app.route("/empregados/<cargo>") #Decorator para requisição da pagina com dados dos empregados de acordo com o cargo
def get_empregados_cargo(cargo):
    out_empregados = []
    for empregado in empregados:
        if cargo == empregado['cargo'].lower():
            out_empregados.append(empregado)
    return {'empregados' : out_empregados}

@app.route("/empregados/<info>/<value>") #Decorator para requisição da pagina empregados de acordo com a informação e o valor dela
def get_empregados_info(info,value):
    out_empregados = []
    for empregado in empregados:
        if info in empregado.keys():
            value_empregado = empregado[info]
            
            if type(value_empregado) == str:
                if value == value_empregado.lower():
                    out_empregados.append(empregado)
                if value == value_empregado:
                    out_empregados.append(empregado)
            
            if type(value_empregado) == int:
                if int(value) == value_empregado:
                    out_empregados.append(empregado)
    return {'empregados': out_empregados}

if __name__ == "__main__":
    app.run(debug=True) #Iniciando o aplicativo com debug para obter informações do servidor