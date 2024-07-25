#coluna
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
    #Futuramente a energia terá que mudar com base em um valor médio dos conhecimentos
    energia = 10
    #função principal da classe
    questionArray = build_array(question)
    conjuntoResposta = percorrer_array(questionArray, energia)

    #nesse momento conjuntoReposta já deve ter as palavras que vai usar para responder, entre aspas, a pergunta

    return "resposta"

#msm coisa que o split_mensagem do dict.py
def build_array(question):
    palavrasPorMensagem = question.split()
    return palavrasPorMensagem

def organizar_questionArray_por_index(questionArray, dic):
    dicIndexes = []
    questionArrayIndexed = []
    for n in questionArray:
        dicIndexes.append(dic_index(dic, n))
    dicIndexes.sort()
    print("dicIndexes..."+str(dicIndexes))
    for d in dicIndexes:
        questionArrayIndexed.append(dic[d])
    print("questionArrayIndexed..."+str(questionArrayIndexed))
    return questionArrayIndexed
#percebi agora que organizar todos os items por array não vai ser tão necessário, vai ser bom fazer isso aí em duplas, pois então
#vou poder comparar uma palavra com a próxima, não tenho certeza ainda de como vai funcionar, vou usar esse aqui msm.

#segundo metodo mais importante da classe(afirmação subjetiva).  
def percorrer_array(questionArray, energia):
    #dada uma palavra, ela só vai ter acesso às palavras com index maior que ela
    #então se ela quiser procurar uma palavra que se encaixe nesse caso, o caminho terá
    #que ser feito ao contrário, por enquanto o sistema vai ser esse
    #só imagino que isso só vai mudar caso a ordem das palavras comece a importar no futuro
    matrix = loadMatrix()
    dic = loadDic()
    questionArrayByIndex = organizar_questionArray_por_index(questionArray, dic)
    #pegar primeira palavra, encontrar as outras duas, e tentar encontrar as próximas
    #sem perder toda a energia. já que estou começando com o menor index, com certeza os
    #outros dois estarão dentro dele e assim em diante.

    #debug
    palavraInicial = questionArrayByIndex[0]
    palavraFinal = questionArrayByIndex[len(questionArrayByIndex)-1]
    #fim debug
    search(10, palavraInicial, palavraFinal, dic, matrix)

    
#getPeso
def getPeso(matrix, palavraInicialIndex, palavraFinalIndex):
    peso = matrix[palavraInicialIndex].corpo[palavraFinalIndex-len(matrix)+1]
    return peso
    
def search(energia, palavraInicial, palavraFinal, dic, matrix):
    print("search")
    caminhoResposta = []
    palavraInicialIndex = dic_index(dic, palavraInicial)
    palavraFinalIndex = dic_index(dic, palavraFinal)
    getPeso(matrix, palavraInicialIndex, palavraFinalIndex)
    print("fim")
    if getPeso(matrix, palavraInicialIndex, palavraFinalIndex)< energia:
        caminhoResposta.append(palavraFinal)
        energia = energia -1

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

#load e save
import pickle as p
def saveMatrix(matrix):
    print("saveMatrix")
    with open('matrix.pkl', 'wb') as outp:
        p.dump(matrix, outp, p.HIGHEST_PROTOCOL)
        
def saveDic(dic):
    print("saveDic")
    with open('dic.pkl', 'wb') as outp:
        p.dump(dic, outp, p.HIGHEST_PROTOCOL)
        
def loadMatrix():
    print("loadMatrix")
    with open('matrix.pkl', 'rb') as m:
        matrix = p.load(m)
        return matrix

def loadDic():
    print("loadDic")
    with open('dic.pkl', 'rb') as m:
        dic = p.load(m)
        return dic
    
#debug response

def debug():
    init_answer("assenta na roda")
    init_answer("roda assenta")
