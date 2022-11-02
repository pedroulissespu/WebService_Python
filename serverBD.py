#Instalar o Flask e Flask-SQLAlchemy
#Instalar da seguinte maneira : pip install Flask Flask-SQLAclhemy
import os
from flask import Flask, Response , render_template, request,url_for,redirect
from flask_sqlalchemy import SQLAlchemy
import json
from sqlalchemy.sql import func

#Flask para usarmos o Flask em si
#Importa o render_template para ter a função para ter alguns templates disponiveis
#O redirect para redirecionar os usuarios

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Usuario(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    nome = db.Column(db.String(50),nullable = False)
    cargo = db.Column(db.String(50),nullable = False)
    salario = db.Column(db.Integer)
    
    def __repr__(self):
        return f'<Usuario {self.nome}>'
    def to_json(self):
        return{"id": self.id,"nome" : self.nome , "cargo" : self.cargo , "salario" : self.salario}
    
@app.route("/usuarios",methods=["GET"]) #Puxar todos os usuarios
def seleciona_usuarios():
    usuarios_objetos = Usuario.query.all()
    usuarios_json = [usuario.to_json() for usuario in usuarios_objetos]
    
    return gera_response(200,"usuarios",usuarios_json)

@app.route("/usuario/<id>",methods=["GET"]) #Puxa apenas 1 usuario através de 1 valor , nesse caso o ID
def seleciona_usuario(id):
    usuario_objeto = Usuario.query.filter_by(id=id).first()
    usuario_json = usuario_objeto.to_json()
    
    return gera_response(200,"usuario",usuario_json)

@app.route("/usuario",methods=["POST"]) #Criar Usuario
def cria_usuario():
    body = request.get_json()
    
    try:
        usuario = Usuario(nome = body["nome"],cargo = body["cargo"] , salario = body["salario"])
        db.session.add(usuario)
        db.session.commit()
        return gera_response(201,"usuario",usuario.to_json(),"Criado com sucesso")
    except Exception as e:
        print('Erro',e)
        return gera_response(400,"usuario",{},"Erro ao cadastrar")
    
@app.route("/usuario/<id>",methods=["PUT"]) #Atualizar dados
def atualiza_usuario(id):
    usuario_objeto = Usuario.query.filter_by(id=id).first()
    body = request.get_json()
    
    try:
        if('nome' in body):
            usuario_objeto.nome = body['nome']
        if('cargo' in body):
            usuario_objeto.cargo = body['cargo']
        if('salario' in body):
            usuario_objeto.salario = body['salario']
        
        db.session.add(usuario_objeto)
        db.session.commit()
        return gera_response(200,"usuario",usuario_objeto.to_json(),"Atualizado com sucesso")
    except Exception as e:
        print('Erro',e)
        return gera_response(400,"usuario",{},"Erro ao atualizar")
    
@app.route("/usuario/<id>",methods=["DELETE"]) #Deleta usuario
def deleta_usuario(id):
    usuario_objeto = Usuario.query.filter_by(id=id).first()
    
    try:
        db.session.delete(usuario_objeto)
        db.session.commit()
        return gera_response(200,"usuario",usuario_objeto.to_json(),"Deletado com sucesso")
    except Exception as e:
        print('Erro',e)
        return gera_response(400,"usuario",{},"Erro ao deletar")

def gera_response(status,nome_do_conteudo,conteudo,mensagem = False):
    body = {}
    body[nome_do_conteudo] = conteudo
    
    if(mensagem):
        body["mensagen"] = mensagem
    
    return Response(json.dumps(body),status = status , mimetype="applications/json")

app.run()