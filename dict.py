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
'''
def loop_palavras_ordenadas_por_menor_index(uniquePalavras, dic, menorPalavra, novaOrdem):
   
    for n in uniquePalavras:
        if dic_index(dic, n) < menorPalavra:
            menorPalavra = dic_index(dic, n)
    novaOrdem.append(dic[menorPalavra])
    
    if len(uniquePalavras) == 1:
        novaOrdem.append(uniquePalavras[0])
        print("nova ordem")
        print(novaOrdem)
        return novaOrdem
    else:
        print("probleminha")
        print(uniquePalavras)
        print("probleminha")
        print(menorPalavra)
        uniquePalavras.remove(uniquePalavras[menorPalavra])
        print("probleminha remove")
        print(uniquePalavras)
        return loop_palavras_ordenadas_por_menor_index(uniquePalavras, dic, len(uniquePalavras)-1, novaOrdem)
    
def palavras_ordenadas_por_menor_index(uniquePalavras, dic):
    menorPalavra = "placeholder"
    novaOrdem = []
    uniquePalavras = loop_palavras_ordenadas_por_menor_index(uniquePalavras, dic, len(uniquePalavras)-1, novaOrdem)
    print(uniquePalavras)
    return uniquePalavras
    '''
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
    print(mensagemArray)
    retirar_valor_de_array(palavra, mensagemArray)
    print(mensagemArray)
    

    coluna = matrix[dic_index(dic, palavra)]
    for n in mensagemArray:
        if dic_index(dic, n)<dic_index(dic, palavra):
            print(palavra + "[CASO ESPECIAL] item novo em coluna antiga " + n)
            colunaN = matrix[dic_index(dic, n)]
            valor = colunaN.getCorpo(dic_index(dic, palavra) - dic_index(dic, n)-1)
            colunaN.setCorpo(dic_index(dic, palavra) - dic_index(dic, n)-1, valor+1)
        else:
            print(n)
            print(palavra)
            #agora vamos adicionar na coluna um valor mais um para cada aparição de uma palavra
            #assume-se que todas as palavras do mensagemArray já estejam registradas como uma linha
            #no dicionário
            print(len(dic))
            print("papo reto")
            print(dic_index(dic, n))
            print(dic_index(dic, palavra))
            print(dic_index(dic, n) - dic_index(dic, palavra)-1)
            #Se o index da palavra for maior que o index de n, o valor será negativo e o processo deverá ser feito adicionando palavra no corpo n e não o contrário
            valor = coluna.getCorpo(dic_index(dic, n) - dic_index(dic, palavra)-1)
            
            #valor = coluna.corpo[dic_index(dic, n) - dic_index(dic, palavra)-1]
            print(dic_index(dic, n))
            print(dic_index(dic, palavra))
            coluna.setCorpo(dic_index(dic, n) - dic_index(dic, palavra)-1, valor+1)

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

#Coisas usáveis tipo factories
def build_new_palavra(value, matrix, dic):
    add_word_to_dic(dic, value)
    add_coluna(matrix, value)

#save and load
#puxar dicionário junto
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
    
#setup de testes
def setupC():
    #método pra agilizar testes
    matrix = []
    add_coluna(matrix, "a")
    add_coluna(matrix, "b")
    add_coluna(matrix, "c")
    add_coluna(matrix, "d")
    arindic = ["a","b","c","d"]
    '''matrix[0].corpo = [0,0,0,0,0]
    matrix[1].corpo = [0,0,0,0,0]
    matrix[2].corpo = [0,0,0,0,0]
    matrix[3].corpo = [0,0,0,0,0]'''
    
    #for n in matrix:
    #    n.corpo = arrayCorpoGenerico
    dic = arindic
    message = split_mensagem("a a a a a a a a a b b b c c c c c d")
    #Eh o que eu escrevi la encima porem concretizada
    for n in palavras_unicas_por_mensagem(message):
        print("HORA DO "+ n)
        update_value_frequencia_coluna(matrix, dic, message, n)
        
    #Esse loop aqui embaixo vai ser bom para debugar dps
    print("resultados...")
    for n in range(len(matrix)):
        print(matrix[n].titulo+"..."+str(matrix[n].corpo))

def setup(matrix, dic, n):
    if is_word_in_dic(dic, n) == False:
        print("nova palavra sendo adicionada! " + n)
        add_word_to_dic(dic, n)
        #Talvez no futuro devesse unir essas duas condicionais em uma coisa só, afinal, se a palavra existe no dicionário
        #Também deve existir como coluna.
    if verify_coluna_existe(matrix, n) == False:
        print("nova coluna sendo adicionada! " + n)
        add_coluna(matrix, n)
#response do bot
def bot_response(inp):
    response = "Resposta\n"
    return response

#função principal de user -> dict
def user_message_to_matrix(message, matrix, dic):
    messageArray = split_mensagem(message)
    uniquePalavras = palavras_unicas_por_mensagem(messageArray)
    for m in uniquePalavras:
        setup(matrix, dic, m)
    print(uniquePalavras)
    print("bora bill")
    
    for n in uniquePalavras:
        print("HORA DO "+ n)
        update_value_frequencia_coluna(matrix, dic, messageArray, n)

    print("matrix...")
    for n in range(len(matrix)):
        print(matrix[n].titulo+"..."+str(matrix[n].corpo))

    print("dic...")
    for n in range(len(dic)):
        print(dic[n])

    #saveCoisas
    saveDic(dic)
    saveMatrix(matrix)

    #futuramente irá retornar uma resposta do bot
    bot_response(message)
    #retorna para a função de input
    inpt(matrix, dic)

#interface de usuário 
def inpt(matrix, dic):
    message = str(input("\n"))
    if message == "quit":
        exit()
    user_message_to_matrix(message, matrix, dic)

def tela_inicial(matrix, dic):
    if len(matrix)<1:
        print("...Matrix: Sem titulo...\nVersão 1 da interface do Dict - \nGuia de\nNavegação,\nOrientação e\nSuporte \nExtrapessoal \n\n Sujeito a alterações.")
    else:
        print("...Matrix: "+matrix[0].titulo+"...\nVersão 1 da interface do Dict - \nGuia de\nNavegação,\nOrientação e\nSuporte \nExtrapessoal \n\n Sujeito a alterações.")
    inpt(matrix, dic)
    
def new_matrix_dic(NewName):
    #adicionar código para nomear sua própria matrix
    matrix = []
    dic = []
    saveMatrix(matrix)
    saveDic(dic)
    tela_inicial(matrix, dic)
        
def old_matrix_dic():
    try:
        matrix = loadMatrix()
        dic = loadDic()
    except:
        print("erro no carregamento da matrix. - old_matrix_dic()")
    tela_inicial(matrix, dic)
        
if __name__ == "__main__":
    ch = int(input('''Aperte....\n > 1 para carregar matrix. \n > 2 para criar nova matrix do zero.\n '''))
    #adicionar código para selecionar matrix disponíveis na pasta
    if ch == 1:
        old_matrix_dic()
    else:
        yn = str(input("Deseja iniciar uma nova matrix? (S/N)\n(estará apagando a antiga...)"))
        if yn.lower() == 's':
            new_matrix_dic(str(input('Insira um novo nome para a matrix...')))
        else:
            exit()
            
