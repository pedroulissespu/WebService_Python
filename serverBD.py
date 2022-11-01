from doctest import REPORT_NDIFF
import sqlalchemy
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import sessionmaker
import json
from flask import Flask,Response,request
from flask_sqlalchemy import SQLAlchemy

engine = sqlalchemy.create_engine('sqlite:///minicurso.db', echo = True)

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer,primary_key=True)
    name = Column(String(50))
    cargo = Column(String(50))
    salario = Column(Integer)
    
    def to_json(self):
        return{"id" : self.id, "name": self.name , "cargo" : self.cargo , "salario" : self.salario}
    
    def __repr__(self):
        return "<User(name={},cargo={},salario={})>".format(self.name,self.cargo,self.salario)
    
Base.metadata.create_all(engine)

user = User(name = 'Pedro' , cargo = 'Host' , salario = 1000)

Session = sessionmaker(bind=engine)
session = Session()
session.add(user)
session.commit()

session.add_all([
    User(name = 'Rodrigo' , cargo = 'C D' , salario = 1),
    User(name = 'A' , cargo = 'A B' , salario = 2)
])

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///minicurso.db'

db = SQLAlchemy(app)

@app.route("/usuarios",methods=['GET'])
def seleciona_usuarios():
    usuarios_classe = User.query.all()
    usuarios_json = [usuario.to_json() for usuario in usuarios_classe]
    return gera_response(200,"usuarios",usuarios_json)


def gera_response(status,nome_do_conteudo,conteudo,mensagem=False):
    body = {}
    body[nome_do_conteudo] = conteudo
    
    if(mensagem):
        body["mensagem"] = mensagem
        
    return Response(json.dumps(body),status=status,mimetype="application/json")

app.run(debug=True)