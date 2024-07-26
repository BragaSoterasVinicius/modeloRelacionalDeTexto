class coluna:
    def __init__(self, titulo):
        self.id = 0
        self.titulo = titulo
        self.corpo = []
        
    def setCorpo(self, pos, value):
        if len(self.corpo) == 0:
            self.corpo.append(0)
        if len(self.corpo)-1 < pos:
            for n in range(self.corpo[len(self.corpo)-1],pos):
                self.corpo.append(0)
            self.corpo.append(value)
        else:
            self.corpo[pos] = value

    def getCorpo(self, pos):
        if len(self.corpo)-1 < pos:
            self.setCorpo(pos, 0)
        return self.corpo[pos]

def init_answer(question):
    energia = 10
    questionArray = build_array(question)
    conjuntoResposta = percorrer_array(questionArray, energia)
    return conjuntoResposta

def build_array(question):
    palavrasPorMensagem = question.split()
    return palavrasPorMensagem

def organizar_questionArray_por_index(questionArray, dic):
    dicIndexes = []
    questionArrayIndexed = []
    for n in questionArray:
        dicIndexes.append(dic_index(dic, n))
    dicIndexes.sort()
    for d in dicIndexes:
        questionArrayIndexed.append(dic[d])
    return questionArrayIndexed

def percorrer_array(questionArray, energia):
    matrix = loadMatrix()
    dic = loadDic()
    questionArrayByIndex = organizar_questionArray_por_index(questionArray, dic)
    responseArrayFinal = []
    for num in range(len(questionArrayByIndex)):
        listaProibida = []
        listaResposta = []
        palavraInicial = questionArrayByIndex[num]
        if num == len(questionArrayByIndex)-1:
            break
        palavraFinal = questionArrayByIndex[num+1]
        newSearch = search(palavraInicial, palavraFinal, listaProibida, energia, listaResposta, matrix, dic)
        responseArrayFinal.append(newSearch)

    responseStrFinal = search_build_string(responseArrayFinal)
 
    return search_build_string(responseArrayFinal)
    
def getPeso(matrix, palavraInicialIndex, palavraFinalIndex):
    peso = matrix[palavraInicialIndex].corpo[palavraFinalIndex-len(matrix)+1]
    return peso
    
def search(inicio, fim, listaProibida, energia, listaResposta, matrix, dic):
    energiaOriginal = energia
    pos = 0
    for peso in matrix[dic_index(dic, inicio)].corpo:
        if matrix[dic_index(dic, inicio)+pos+1].titulo not in listaProibida and peso < energia:
            if energia< 3:
                listaProibida.append(matrix[dic_index(dic, inicio)+pos+1].titulo)
                return search(inicio, fim, listaProibida, energiaOriginal, listaResposta, matrix, dic)
            else:
                listaResposta.append(matrix[dic_index(dic, inicio)+pos+1].titulo)
                inicio = listaResposta[len(listaResposta)-1]
                if listaResposta[len(listaResposta)-1] == fim:
                    return listaResposta
                return search(inicio, fim, listaProibida, energia, listaResposta, matrix, dic)
        pos += 1

def search_build_string(listaResposta):
    stringResposta = ''
    for n in listaResposta:
        if n != None:
            for m in n:
                stringResposta +=(m)
                stringResposta += " " 
    return(stringResposta)

#dic
def is_word_in_dic(dic, word):
    for n in dic:
        if n == word:
            return True
    return False

def add_word_to_dic(dic, word):
    dic.append(word)

def dic_index(dic, word):
    return dic.index(word)

import pickle as p
def saveMatrix(matrix):
    with open('matrix.pkl', 'wb') as outp:
        p.dump(matrix, outp, p.HIGHEST_PROTOCOL)
        
def saveDic(dic):
    with open('dic.pkl', 'wb') as outp:
        p.dump(dic, outp, p.HIGHEST_PROTOCOL)
        
def loadMatrix():
    with open('matrix.pkl', 'rb') as m:
        matrix = p.load(m)
        return matrix

def loadDic():
    with open('dic.pkl', 'rb') as m:
        dic = p.load(m)
        return dic
    
def debug():
    init_answer("Receba um bot do Bora Bill favela")
    
