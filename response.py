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

def set_energia():
    #A energia média do percurso também pode ser entendida como quanto esforço a máquina vai colocar para encontrar ligações
    #Quanto maior a energia, menos resultados vazios, mais palavras.
    return 1000

def init_answer(question):
    #Futuramente a energia terá que mudar com base em um valor médio dos conhecimentos
    energia = set_energia()
    #função principal da classe
    questionArray = build_array(question)
    conjuntoResposta = percorrer_array(questionArray, energia)

    #nesse momento conjuntoReposta já deve ter as palavras que vai usar para responder, entre aspas, a pergunta

    return conjuntoResposta

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
    
    #fim debug
    
    responseArrayFinal = []
    for num in range(len(questionArrayByIndex)):
        listaProibida = []
        listaResposta = []
        print("range", len(questionArrayByIndex))
        palavraInicial = questionArrayByIndex[num]
        print("rodada ",num ," ", palavraInicial)
        if num == len(questionArrayByIndex)-1:
            break
        palavraFinal = questionArrayByIndex[num+1]
        print("search")
        newSearch = search(palavraInicial, palavraFinal, listaProibida, energia, listaResposta, matrix, dic)
        print("search rodada ", num, "palavra Inicial: ", palavraInicial, "\npalavra Final: ", palavraFinal)
        print(newSearch)
        responseArrayFinal.append(newSearch)

    #responseStrFinal = " ".join(map(str, responseArrayFinal))
    responseStrFinal = search_build_string(responseArrayFinal)
    
    print("array original "+ str(questionArrayByIndex))
    print("array que temos"+ str(responseArrayFinal))
    print(search_build_string(responseArrayFinal))
    return search_build_string(responseArrayFinal)
    
#getPeso
def getPeso(matrix, palavraInicialIndex, palavraFinalIndex):
    peso = matrix[palavraInicialIndex].corpo[palavraFinalIndex-len(matrix)+1]
    return peso
    
def search(inicio, fim, listaProibida, energia, listaResposta, matrix, dic):
    #esse método é só para ir de uma palavra para outra, deve ser executada EM PARES
    #encontre f que n esteja na lista proibida e concorde com o gasto de energia
    # na lista[inicio]
    print(energia)
    energiaOriginal = energia
    pos = 0
    for peso in matrix[dic_index(dic, inicio)].corpo:
        print(pos)
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
    init_answer("Receba um bot do Bora Bill favela")
    
