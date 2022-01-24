from ast import Return
from flask import Flask, jsonify, request
import json

app = Flask(__name__)

desenvolvedores = [
    {"nome": "Filipe",
     'habilidades': ['Python', 'Flask', 'Django']},
    {'nome': 'Castro',
     'habilidades': ['Python', 'Machine Learning']}
]
#Devolve os dados via ID, altera e delete os dados.
@app.route('/dev/<int:id>/', methods=['GET','PUT','DELETE'])
def index(id):
    try:
        if request.method == 'GET':
            response = desenvolvedores[id]
            return jsonify(response)
        elif request.method == 'PUT':
            dados = json.loads(request.data)
            desenvolvedores[id] = dados
            return jsonify(dados)
        elif request.method =='DELETE':
            desenvolvedores.pop(id)
            return jsonify({'status':'dados excluidos'})
    except IndexError:
        return jsonify({'Mensagem':'Erro, dados não encontrados.'})
#Lista todos os registros e inclui um novo registro
@app.route('/dev/', methods=['POST','GET'])
def lista_desenvolvedores():
    if request.method=='POST':
        dados = json.loads(request.data)
        desenvolvedores.append(dados)
        return jsonify({'status':'sucesso'})
    elif request.method == 'GET':
        return jsonify(desenvolvedores)
      
         
if __name__ == '__main__':
    app.run(debug=True)
