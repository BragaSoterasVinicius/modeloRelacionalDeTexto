import dict as d
import json
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
#Algum dia dou um jeito que não precise ter essa classe em todos os arquivos... 
class coluna:
    def __init__(self, titulo):
        self.id = 0
        self.titulo = titulo
        self.corpo = []
        #o titulo vai com a palavra de referencia da coluna e o corpo com quantas vezes
        #essa palavra titulo aparece com outra que tenha um index igual ao index da palavra
        #titulo + o index desta palavra no corpo da coluna.]
        
    def setCorpo(self, pos, value):
        if len(self.corpo) == 0:
            print(self.corpo)
            self.corpo.append(0)
        if len(self.corpo)-1 < pos:
            print(self.corpo)
            for n in range(len(self.corpo)-1,pos):
                print(self.corpo)
                self.corpo.append(0)
                print(self.corpo)
                print(len(self.corpo)-1)
            print("deve ter ido ate", pos)
            print(value)
            self.corpo[pos]= value
        else:
            print(self.corpo[pos])
            self.corpo[pos] = value

    def getCorpo(self, pos):
        print(len(self.corpo)-1)
        print(pos)
        if len(self.corpo)-1 < pos:
            print("coluna sem linha, adicionando 0.")
            self.setCorpo(pos, 0)
        return self.corpo[pos]

@app.route('/speak', methods=['POST'])
def speak():
    record = json.loads(request.data)

    matrixName = str(record['matrixName'])
    user_message = str(record['user_message'])
    shouldReturn = bool(record['shouldReturn'])
    algoritmo = str(record['algoritmo'])
    energiaCognitiva = float(record['energiaCognitiva'])
    salvarNaMatrix = bool(record['salvarNaMatrix'])
    returnObject = bool(record['returnObject'])

    response: str = d.user_message_to_matrix(matrixName, user_message, d.loadMatrix(matrixName), d.loadDic(matrixName), shouldReturn,
                                              algoritmo, energiaCognitiva, salvarNaMatrix, returnObject)
    if response !=None:
        return jsonify(response)
    else:
        return "Não sei o que te dizer a respeito disso aí...\n(O bot não retornou nada)"


import os
@app.route('/listmatrixes', methods=['GET'])
def list_matrixes():
    arraylista = []
    [arraylista.append(str(i)[0:-4]) for i in os.listdir('matrixLib')]
    return jsonify(arraylista)

@app.route('/listalgoritms', methods=['GET'])
def list_algoritms():
    lista = ['a', 'b']
    return jsonify(lista)
app.run()