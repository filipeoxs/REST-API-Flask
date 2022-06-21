from distutils.log import debug
from json import loads
from json.tool import main
from flask import Flask
from flask_restful import Resource, Api
from itsdangerous import json
# Inicializando o Flask
app = Flask(__name__)
# Inicializando o FlaskRESTful
api = Api(app)

desenvolvedores = [
    {"nome": "Filipe",
     'habilidades': ['Python', 'Flask', 'Django']},
    {'nome': 'Castro',
     'habilidades': ['Python']}
]

class Desenvolvedor(Resource):
    def get(self,id):
        try:
            response = desenvolvedores[id]
            return response
        except IndexError:
            return ({'Mensagem': 'Erro, dados não encontrados.'})

    def put(self):
        try:
            dados = json.loads(request.data)
            desenvolvedores[id] = dados
            return (dados)
        except IndexError:
            return ({'Mensagem': 'Erro, dados não encontrados.'})

    def delete(self):
        try:
            desenvolvedores.pop(id)
            return ({'status': 'dados excluidos'})
        except IndexError:
            return ({'Mensagem': 'Erro, dados não encontrados.'})

    def post(self):
        try:
            dados = json.loads(request.data)
            desenvolvedores.append(dados)
            return ({'status':'sucesso'})
        except IndexError:
            return ({'Mensagem': 'Erro, dados não encontrados.'})

class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores
    def post(self):
        try:
            dados = json.loads(request.data)
            desenvolvedores.append(dados)
            return ({'status':'sucesso'})
        except IndexError:
            return ({'Mensagem': 'Erro, dados não encontrados.'})

# Rotas
api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(ListaDesenvolvedores,'/dev/')

if __name__ == '__main__':
    app.run(debug=True)
