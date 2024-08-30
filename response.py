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
    #A energia media pertence ao bot como um todo e deve ser resultado da sua base de conhecimentos.
    return 20

def init_answer(matrixName, question, algoritmo, energiaCognitiva):
    #Futuramente a energia terá que mudar com base em um valor médio dos conhecimentos
    energia = set_energia()
    #função principal da classe
    questionArray = build_array(question)
    conjuntoResposta = percorrer_array(matrixName,questionArray, energia, algoritmo, energiaCognitiva)

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
def percorrer_array(matrixName,questionArray, energia, algoritmo, energiaCognitiva):
    #dada uma palavra, ela só vai ter acesso às palavras com index maior que ela
    #então se ela quiser procurar uma palavra que se encaixe nesse caso, o caminho terá
    #que ser feito ao contrário, por enquanto o sistema vai ser esse
    #só imagino que isso só vai mudar caso a ordem das palavras comece a importar no futuro
    matrix = loadMatrix(matrixName)
    dic = loadDic(matrixName)
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
        listatotal = []
        print("range", len(questionArrayByIndex))
        palavraInicial = questionArrayByIndex[num]
        print("rodada ",num ," ", palavraInicial)
        if num == len(questionArrayByIndex)-1:
            break
        palavraFinal = questionArrayByIndex[num+1]
        print("search")
        pos = 0
        #newSearch = search(palavraInicial, palavraFinal, listaProibida, energia, listaResposta, matrix, dic, pos)
        #newSearch = search_a(energia, listatotal, palavraInicial, palavraFinal, matrix, dic)
        #O ultimo campo do searchB é a energia que o bot tem para realizar a ligação entre duas palavras
        #(1 o bot vai só repetir o que foi dito)
        #(0 o bot não vai dizer nada)
        limiteCognitivo = energiaCognitiva
        print("Rodando sistema de resposta com limite cognitivo " + str(limiteCognitivo))
        newSearch = search_selector(matrixName, listatotal, palavraInicial, palavraFinal, matrix, dic, limiteCognitivo, algoritmo)
        print("search rodada ", num, "palavra Inicial: ", palavraInicial, "\npalavra Final: ", palavraFinal)
        print(newSearch)
        responseArrayFinal.append(newSearch)

    #responseStrFinal = " ".join(map(str, responseArrayFinal))
    responseStrFinal = search_build_string(responseArrayFinal)
    
    print("array original "+ str(questionArrayByIndex))
    print("array que temos"+ str(responseArrayFinal))
    print(search_build_string(responseArrayFinal))
    return search_build_string(responseArrayFinal)
   
def search_selector(matrixName, listatotal, palavraInicial, palavraFinal, matrix, dic, limiteCognitivo, algoritmo):
    if algoritmo == 'b':
        return search_b(matrixName, listatotal, palavraInicial, palavraFinal, matrix, dic, limiteCognitivo)
    elif algoritmo == 'a':
        return search_a(matrixName, 20, listatotal, palavraInicial, palavraFinal, matrix, dic)
#getPeso
def getPeso(matrix, palavraInicialIndex, palavraFinalIndex):
    peso = matrix[palavraInicialIndex].getCorpo(palavraFinalIndex-len(matrix)+1)
    return peso

def peso_medio_da_coluna(coluna, matrix, dic):
    m = 0
    for n in matrix[dic_index(dic, coluna)].corpo:
        m = m+n
    m = m/ len(matrix[dic_index(dic, coluna)].corpo)-1
    print("valor médio da coluna "+matrix[dic_index(dic, coluna)].titulo+": "+ str(m))
    return m

#A lista de percentuais deveria ter haver com o valor de cada item e não sua posição na coluna
def pegar_lista_de_percentuais_para_coluna(coluna):
    listaPercentuais = []
    #Quando uma palavra não mais nenhuma outra com relação a ela, sua lista é vazia e o metodo da vez deve retornar null.
    if(len(coluna.corpo) == 0):
        #isso aqui nao pode acontecer
        ptl = 100
    else:
        ptl = 100/len(coluna.corpo)
    for n in range(len(coluna.corpo)):
        m = (n+1)*ptl
        listaPercentuais.append(m)
    return listaPercentuais

def pegar_valor_de_Q(listaPercentuais, coluna, valor):
    #O percentual aqui está somente baseado na distância do valor ao ponto de referencia. Que bobeira, deve ser em relacao ao seu valor
    hierarquiaDeValores = []
    #hierarquia de valores vai ter os valores da coluna na ordem do menor para o maior, assim, o valor menos presente será o de menor percentual, ou de maior gasto, enquanto o de maior valor 
    #preservara 100 % do valor original. 
    hierarquiaDeValores = hierarquiaDeValores + coluna
    hierarquiaDeValores.sort()
    Q = listaPercentuais[hierarquiaDeValores.index(valor)]
    Q = Q/100
    return Q

def valor_finder(dic, matrix, palavraX, palavraY):
    if dic_index(dic, palavraX) > dic_index(dic, palavraY):
        coluna = matrix[dic_index(dic, palavraY)]
        print(coluna)
        valor = coluna.getCorpo(dic_index(dic, palavraX) - dic_index(dic, palavraY)-1)
    elif dic_index(dic, palavraX) <= dic_index(dic, palavraY):
        coluna = matrix[dic_index(dic, palavraX)]
        valor = coluna.getCorpo(dic_index(dic, palavraY) - dic_index(dic, palavraX)-1)
    return valor

#Quando duas palavras ficam MUITO ligadas, o custo para conectalas, fica negativo, o que infelizmente atrapalha o funcionamento do programa
#Pois o custo é extraido da energia, se esse custo é negativo, a energia aumenta. A energia sempre deve cair, mesmo que pouco para items muito relacionados.
def custo_do_peso_de(palavra, a, matrix, dic):
    percentuais = pegar_lista_de_percentuais_para_coluna(matrix[dic_index(dic, a)])
    #Quanto maior o Q (mais próximo de 1), mais da energia será guardada
    coluna = matrix[dic_index(dic, a)].corpo
    valor = valor_finder(dic, matrix, palavra, a)
    Q = pegar_valor_de_Q(percentuais, coluna, valor)
    '''indexRelativoDePalavraEmA = dic_index(dic, palavra) - dic_index(dic, a)
    pesoDePalavraEmA = matrix[dic_index(dic, a)].corpo[indexRelativoDePalavraEmA]
    pesoMedio = peso_medio_da_coluna(a, matrix, dic)
    conexaoIdeal = pesoMedio*2
    custoPeso = conexaoIdeal - pesoDePalavraEmA'''
    return Q*0.8

def cria_conjunto_pagavel_palavra_de(a, energia, matrix, dic):
    conjunto = []
    indexrelativo = -1
    coluna = matrix[dic_index(dic, a)].corpo
    for peso in coluna:
        indexrelativo += 1
        if peso < energia:
            posicaoGlobalDaPalavraSelecionada = dic_index(dic, a)+indexrelativo 
            palavra = matrix[posicaoGlobalDaPalavraSelecionada].titulo
            conjunto.append(palavra)
    return conjunto

def energiaDin(energia):
    import random as r
    return r.uniform(0,1)
    energiaDin = energia / set_energia()
    return energiaDin

def search_b(matrixName, listaTotal, palavraInicial, palavraFinal, matrix, dic, limite_cognitivo):
    import searchB
    return searchB.conversa_em_par(matrixName, listaTotal, palavraInicial, palavraFinal, matrix, dic, limite_cognitivo)

#Todo o metodo devera ser refeito, levando em consideracao que nao posso mais assumir que o a seja menor no dic que o b, devido a capacidade de exploracao
def search_a(energia, listatotal, a, b, matrix, dic):
    print("a energia esta assim" + str(energia))
    print("como vai a lista:", str(listatotal))
    if not matrix[dic_index(dic, a)].corpo:
        return None 
    if energia < 0.15:
        return listatotal
    listatotal.append(a)
    print("como vai a lista:", str(listatotal))
    if (dic_index(dic, b) - dic_index(dic, a)) > 0:
        Q = custo_do_peso_de(b, a, matrix, dic)
        print("relação "+str(Q))
        if 1-Q < energiaDin(energia):
            energia = energia*Q
            listatotal.append(b)
            return listatotal
        else:
            conjuntoPagavel = cria_conjunto_pagavel_palavra_de(a, energia, matrix, dic)
            for palavra in conjuntoPagavel:
                subenergia = 0
                #subenergia = energia - custo_do_peso_de(palavra, a, matrix, dic)
                Q = custo_do_peso_de(b, palavra, matrix, dic)
                subenergia = Q*energia
                novaListaTotal = []
                novaListaTotal = novaListaTotal + listatotal
                searchA = search_a(subenergia, novaListaTotal, palavra, b, matrix, dic) 
                if searchA != None:
                    return searchA
                else:
                    return
                    #energia e listatotal devem permanecer os mesmos,
                    # pegando os valores que possuiam antes do loop,
                    # em cada loop, eh como se fossem um backup para ir atras nas listas mesmo
                 #   energia = backupEnergia
                 #   listatotal = backupListaTotal
    else:
        return None
                
                
def search(inicio, fim, listaProibida, energia, listaResposta, matrix, dic, pos):
    #esse método é só para ir de uma palavra para outra, deve ser executada EM PARES
    #encontre f que n esteja na lista proibida e concorde com o gasto de energia
    # na lista[inicio]
    print(energia)
    energiaOriginal = energia
    
    for peso in matrix[dic_index(dic, inicio)].corpo:
        print("posição do corpo de "+str(inicio) + "na matrix eh" + str(pos))
        if matrix[dic_index(dic, inicio)+pos-1].titulo not in listaProibida and peso < energia:
            if energia<- 999:
                listaProibida.append(matrix[dic_index(dic, inicio)+pos+1].titulo)
                pos += 1
                return search(inicio, fim, listaProibida, energiaOriginal, listaResposta, matrix, dic, pos)
            else:
                listaResposta.append(matrix[dic_index(dic, inicio)+pos+1].titulo)
                energia = energia - (peso*-1)
                inicio = listaResposta[len(listaResposta)-1]
                if listaResposta[len(listaResposta)-1] == fim:
                    return listaResposta
                pos += 1
                return search(inicio, fim, listaProibida, energia, listaResposta, matrix, dic, pos)
        

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
def saveMatrix(matrix, name="backup_matrix"):
    print("saveMatrix" + name)
    with open("matrixLib/"+name+'.pkl', 'wb') as outp:
        p.dump(matrix, outp, p.HIGHEST_PROTOCOL)
        
def saveDic(dic, name="backup_matrix"):
    print("saveDic" + name)
    with open('dicLib/'+name+'.pkl', 'wb') as outp:
        p.dump(dic, outp, p.HIGHEST_PROTOCOL)
        
def loadMatrix(matrixname = "matrix"):
    print("loadMatrix")
    with open('matrixLib/'+matrixname+".pkl", 'rb') as m:
        matrix = p.load(m)
        return matrix

def loadDic(matrixname = "matrix"):
    print("loadDic")
    with open('dicLib/'+matrixname+'.pkl', 'rb') as m:
        dic = p.load(m)
        return dic
#debug response

def debug():
    init_answer("Receba um bot do Bora Bill favela")
    
