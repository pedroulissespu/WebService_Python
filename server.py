#pip install flask -> instalar o flask
from flask import Flask

empregados = [
                {'nome' : 'Valentina', 'cargo' : 'Analista' , 'salario' : 5000},
                {'nome' : 'Joao', 'cargo' : 'Analista' , 'salario' : 3000},
                {'nome' : 'Moises', 'cargo' : 'Garota de Programa' , 'salario' : 9999999}
            ] #Dados ficticios

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Pagina Principal</h1>"

@app.route("/empregados")
def get_empregados():
    return{'empregados': empregados}

@app.route("/empregados/<cargo>")
def get_empregados_cargo(cargo):
    out_empregados = []
    for empregado in empregados:
        if(cargo == empregado['cargo']):
            out_empregados.append(empregado)
    return {'empregados' : out_empregados}

if __name__ == "__main__":
    app.run(debug=True)