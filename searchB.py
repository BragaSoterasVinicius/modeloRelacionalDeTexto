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

def dic_index(dic, word):
    return dic.index(word)

def getGasto(colunaRef, palavraRef, matrix, dic):
    somaColuna = sum(colunaRef.corpo)
    if dic_index(dic, palavraRef) < dic_index(dic, colunaRef.titulo):
        bkp = colunaRef.titulo
        colunaRef = matrix[dic_index(dic, palavraRef)]
        palavraRef = bkp
    indexDaPalavraNaColunaRef = dic_index(dic, palavraRef) - dic_index(dic, colunaRef.titulo)-1
    #Tenho que fazer algum sistema para inverter as coordenadas de uma coluna vazia para sua linha equivalente.
    if indexDaPalavraNaColunaRef > len(colunaRef.corpo)-1:
        valorDePalavraEmColuna = 0
    else:
        valorDePalavraEmColuna = colunaRef.corpo[indexDaPalavraNaColunaRef]
    if somaColuna == 0: 
        somaColuna = 1
    gasto = 1 - (valorDePalavraEmColuna/somaColuna)
    return gasto

def hear_a(palavraInicial, palavraFinal, matrix, dic):
    return None

def makeUsableLista(colunaPalavraInicial, limiteCognitivo, matrix, dic):
    listaDeSubPalavrasUsaveis = []
    print("Calculando palavras relacionadas...")
    for n in range(1, len(colunaPalavraInicial.corpo)+1):
        palavra =  dic[dic_index(dic, colunaPalavraInicial.titulo)+n]
        print("Index - "+ str(n)+": Gasto enérgico da palavra "+str(palavra)+" na coluna "+ str(colunaPalavraInicial.titulo) + "..." + str(getGasto(colunaPalavraInicial, palavra, matrix, dic)))
        if getGasto(colunaPalavraInicial, palavra, matrix, dic) < limiteCognitivo:
            listaDeSubPalavrasUsaveis.append(palavra)
    return listaDeSubPalavrasUsaveis

def show_gasto_energetico(colunaPalavraInicial, matrix, dic):
    for n in range(len(colunaPalavraInicial.corpo)):
        n +=1
        palavra =  dic[dic_index(dic, colunaPalavraInicial.titulo)+n-1]
        print("Index - "+ str(n)+": Gasto enérgico da palavra "+str(palavra)+" na coluna "+ str(colunaPalavraInicial.titulo) + "..." + str(getGasto(colunaPalavraInicial, palavra, matrix, dic)))

def conversa_em_par(matrixName, listaTotal, palavraInicial, palavraFinal, matrix, dic, limiteCognitivo, cansaco = 10):
    listaTotal.append(palavraInicial)
    colunaRelevante = matrix[dic_index(dic, palavraInicial)]
    print("Gasto energético = " + str(getGasto(colunaRelevante, palavraFinal, matrix, dic)))
    if getGasto(colunaRelevante, palavraFinal, matrix, dic) > limiteCognitivo:
        listaDeSubPrimarios = makeUsableLista(colunaRelevante, limiteCognitivo, matrix, dic)
        print (listaDeSubPrimarios)
        for eachMiddlePalavra in listaDeSubPrimarios:
            subListaTotal = []
            subListaTotal = subListaTotal + listaTotal
            conversaAprofundada = conversa_em_par(matrixName, subListaTotal, eachMiddlePalavra, palavraFinal, matrix, dic, limiteCognitivo)
            print("palavra do meio" + eachMiddlePalavra)
            print("subConversaListaTotal" + str(conversaAprofundada))
            if conversaAprofundada != None:
                return conversaAprofundada
    else:
        show_gasto_energetico(colunaRelevante, matrix, dic)
        listaTotal.append(palavraFinal)
        print(listaTotal)
        return listaTotal
    
def debugada():
    dic = ["turma","da","monica"]
    matrix= []
    turma = [2, 5]
    da = [3]
    monica = []
    turma1 = coluna("turma")
    da1 = coluna("da")
    monica1 = coluna("monica")
    turma1.corpo = turma
    da1.corpo = da
    monica1.corpo = monica
    matrix.append(turma1)
    matrix.append(da1)
    matrix.append(monica1)
    listaTotal = []
    conversa_em_par(listaTotal, "turma","monica", matrix, dic, 0.7)

    '''
        hear_a("turma", "da", matrix, dic)
        hear_a("turma", "da", matrix, dic)
        hear_a("turma", "da", matrix, dic)
        hear_a("da", "monica", matrix, dic)
        hear_a("da", "monica", matrix, dic)
        hear_a("da", "monica", matrix, dic)
    '''
        
