dic = []
#Só serve para saber que palavras estão no sistema, não confundir com coluna
#Que são as colunas da matrix.

matrix = []
#misc
def retirar_valor_de_array(valor, array):
    for n in range(array.count(valor)):
        array.remove(valor)

#receber mensagem
def split_mensagem(mensagem):
    palavrasPorMensagem = mensagem.split()
    print(palavrasPorMensagem)
    return palavrasPorMensagem

def palavras_unicas_por_mensagem(mensagemArray):
    palavrasUnicasPorMensagem = []
    for x in mensagemArray:
        if x not in palavrasUnicasPorMensagem:
            palavrasUnicasPorMensagem.append(x)
    
    return palavrasUnicasPorMensagem

        
#coluna
class coluna:
    def __init__(self, titulo):
        self.id = 0
        self.titulo = titulo
        self.corpo = []
    #o titulo vai com a palavra de referencia da coluna e o corpo com quantas vezes
    #essa palavra titulo aparece com outra que tenha um index igual ao index da palavra
    #titulo + o index desta palavra no corpo da coluna.


def add_coluna(matrix, palavraTitulo):
    colunaNova = coluna(palavraTitulo)
    colunaNova.id = len(matrix)
    matrix.append(colunaNova)
    
def add_linha(coluna):
    coluna.append(0)
    
def verify_coluna_existe(matrix, palavra):
    for n in matrix:
        if n.titulo == palavra:
            return True
    return False

def update_value_frequencia_coluna(matrix, dic, mensagemArray, palavra):
    #Só pra que a palavra cuja frequencia está sendo medida não crie uma relação consigo
    #mesma. Não se vão querer mudar no futuro, mas melhor anotar.

    #O valor original de mensagemArray deve ser o msm toda vez q o metodo roda.
    retirar_valor_de_array(palavra, mensagemArray)
    print(mensagemArray)
    
    coluna = matrix[dic_index(dic, palavra)]
    for n in mensagemArray:
        print(n)
        #agora vamos adicionar na coluna um valor mais um para cada aparição de uma palavra
        #assume-se que todas as palavras do mensagemArray já estejam registradas como uma linha
        #no dicionário
        valor = coluna.corpo[dic_index(dic, n) - dic_index(dic, palavra)-1]
        print(dic_index(dic, n))
        print(dic_index(dic, palavra))
        coluna.corpo[dic_index(dic, n) - dic_index(dic, palavra)-1] = valor+1

    print("coluna montada")
    print(palavra +"..."+ str(coluna.corpo))
    return coluna.corpo

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

def setupA():
    #método pra agilizar testes
    add_coluna(matrix, "a")
    add_coluna(matrix, "b")
    add_coluna(matrix, "c")
    add_coluna(matrix, "d")
    arindic = ["a","b","c","d"]
    matrix[0].corpo = [0,0,0,0]
    matrix[1].corpo = [0,0,0,0]
    matrix[2].corpo = [0,0,0,0]
    matrix[3].corpo = [0,0,0,0]
    
    #for n in matrix:
    #    n.corpo = arrayCorpoGenerico
    dic = arindic
    add_value_frequencia(matrix, dic,  "b")
    
def setupB():
    #método pra agilizar testes
    add_coluna(matrix, "a")
    add_coluna(matrix, "b")
    add_coluna(matrix, "c")
    add_coluna(matrix, "d")
    arindic = ["a","b","c","d"]
    matrix[0].corpo = [0,0,0,0]
    matrix[1].corpo = [0,0,0,0]
    matrix[2].corpo = [0,0,0,0]
    matrix[3].corpo = [0,0,0,0]
    
    #for n in matrix:
    #    n.corpo = arrayCorpoGenerico
    dic = arindic
    message = split_mensagem("a b c a a")
    #Interessantemente, está funcionando, o método abaixo, por exemplo, denota em todas
    #as colunas anteriores quantas vezes b apareceu na mensagem. Aumentando o peso de b
    #nas colunas anteriores (nesse caso só >a< msm). Idealmente no lugar de b estaremos
    #colocando cada palavra da mensagem, uma única vez, na mensagem acima, por exemplo
    #testaríamos a, b, c e d uma única vez.
    add_value_frequencia(matrix, dic, message, "b")
    
def setupC():
    #método pra agilizar testes
    matrix = []
    add_coluna(matrix, "a")
    add_coluna(matrix, "b")
    add_coluna(matrix, "c")
    add_coluna(matrix, "d")
    arindic = ["a","b","c","d"]
    matrix[0].corpo = [0,0,0,0,0]
    matrix[1].corpo = [0,0,0,0,0]
    matrix[2].corpo = [0,0,0,0,0]
    matrix[3].corpo = [0,0,0,0,0]
    
    #for n in matrix:
    #    n.corpo = arrayCorpoGenerico
    dic = arindic
    message = split_mensagem("a a b b b c c c d")
    #Eh o que eu escrevi la encima porem concretizada
    for n in palavras_unicas_por_mensagem(message):
        print("HORA DO "+ n)
        update_value_frequencia_coluna(matrix, dic, message, n)
        
    #Esse loop aqui embaixo vai ser bom para debugar dps
    print("resultados...")
    for n in range(len(matrix)):
        print(matrix[n].titulo+"..."+str(matrix[n].corpo))
