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
    valorDePalavraEmColuna = colunaRef.corpo[dic_index(dic, palavraRef) - dic_index(dic, colunaRef.titulo)-1]
    gasto = 1 - (valorDePalavraEmColuna/somaColuna)
    return gasto

def hear_a(palavraInicial, palavraFinal, matrix, dic):
    return None
def makeUsableLista(colunaPalavraInicial, limiteCognitivo, matrix, dic):
    listaDeSubPalavrasUsaveis = []
    for n in range(len(colunaPalavraInicial.corpo)):
        n +=1
        palavra =  dic[dic_index(dic, colunaPalavraInicial.titulo)+n-1]
        print("Index - "+ str(n)+": Gasto enérgico da palavra "+str(palavra)+" na coluna "+ str(colunaPalavraInicial.titulo) + "..." + str(getGasto(colunaPalavraInicial, palavra, matrix, dic)))
        if getGasto(colunaPalavraInicial, palavra, matrix, dic) < limiteCognitivo:
            listaDeSubPalavrasUsaveis.append(palavra)
    return listaDeSubPalavrasUsaveis

def conversa_em_par(listaTotal, palavraInicial, palavraFinal, matrix, dic, limiteCognitivo):
    listaTotal.append(palavraInicial)
    colunaRelevante = matrix[dic_index(dic, palavraInicial)]
    print("Gasto energético = " + str(getGasto(colunaRelevante, palavraFinal, matrix, dic)))
    if getGasto(colunaRelevante, palavraFinal, matrix, dic) > limiteCognitivo:
        listaDeSubPrimarios = makeUsableLista(colunaRelevante, limiteCognitivo, matrix, dic)
        print (listaDeSubPrimarios)
        for eachMiddlePalavra in listaDeSubPrimarios:
            subListaTotal = []
            subListaTotal = subListaTotal + listaTotal
            conversaAprofundada = conversa_em_par(subListaTotal, eachMiddlePalavra, palavraFinal, matrix, dic)
            print("palavra do meio" + eachMiddlePalavra)
            print("subConversaListaTotal" + str(conversaAprofundada))

    else:
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
        
