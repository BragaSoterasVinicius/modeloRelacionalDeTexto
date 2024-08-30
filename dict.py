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
        if dic_index(dic, n) < dic_index(dic, palavra):
            print(palavra + "[CASO ESPECIAL] item novo em coluna antiga " + n)
            colunaN = matrix[dic_index(dic, n)]
            print(dic_index(dic, palavra))
            print(dic_index(dic, n))
            print(dic_index(dic, palavra) - dic_index(dic, n)-1)
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

def show_dic(matrixname = 'matrixbackup'):
    dic = loadDic(matrixname)
    for n in dic:
        print(str(dic_index(dic, n))+"..."+  n)

def show_matrix(matrixname = 'matrixbackup'):
    matrix = loadMatrix(matrixname)
    for n in matrix:
        print(n.titulo + "..." + str(n.corpo))
    
#response do bot
def bot_response(matrixName, inp, algoritmo, energiaCognitiva):
    import response as r
    response = r.init_answer(matrixName, inp, algoritmo, energiaCognitiva)
    return response

#função principal de user -> dict
def user_message_to_matrix(matrixName, message, matrix, dic, retornar, algoritmo, energiaCognitiva, salvarNaMatrix):
    messageArray = split_mensagem(message)
    
    if (str(messageArray[0]) == "$/setSaveMatrix"):
        salvarNaMatrix = (messageArray[1] == 'True')
        return inpt(matrixName, matrix, dic, retornar, algoritmo, energiaCognitiva, salvarNaMatrix)
    if (str(messageArray[0]) == "$/set"):
        energiaCognitiva = float(messageArray[1])
        return inpt(matrixName, matrix, dic, retornar, algoritmo, energiaCognitiva, salvarNaMatrix)
    if (str(messageArray[0]) == "$/return"):
        return tela_inicial(matrixName, matrix, dic)
    uniquePalavras = palavras_unicas_por_mensagem(messageArray)

    if(salvarNaMatrix):
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
        print("dic e matrix sendo salvas...")
        saveDic(dic, matrixName)
        saveMatrix(matrix, matrixName)
    else:
        messageArrayS = [] + messageArray
        for m in messageArray:
            if is_word_in_dic(dic, m) == False:
                messageArrayS.remove(m)
        message = " ".join(messageArrayS)
            
    if(retornar):
        print(bot_response(matrixName, message, algoritmo, energiaCognitiva))
    
#interface de usuário 
def inpt(matrixName, matrix, dic, responder, algoritmo, energiaCognitiva = 0.7, salvarNaMatrix = True):
    message = str(input("\n"))
    if message == "quit":
        #saveMatrix(matrix)
        exit()
    if message == "$$/stresstest":
        for n in range(600):
            user_message_to_matrix(matrixName, str(n),matrix,dic, False, algoritmo, energiaCognitiva, True)
        print("Finalizado")
        print(len(dic))
        print(len(matrix))
        quit()
    user_message_to_matrix(matrixName, message, matrix, dic, responder, algoritmo, energiaCognitiva, salvarNaMatrix)
    #retorna para a função de input
    inpt(matrixName, matrix, dic, responder, algoritmo, energiaCognitiva, salvarNaMatrix)

def tela_inicial(matrixName, matrix, dic):
    if len(matrix)<1:
        print("...Matrix: Sem titulo...\nVersão 1 da interface do Dict - \nGuia de\nNavegação,\nOrientação e\nSuporte \nExtrapessoal \n\n Sujeito a alterações.")
    else:
        print("...Matrix: "+matrix[0].titulo+"...\nVersão 1 da interface do Dict - \nGuia de\nNavegação,\nOrientação e\nSuporte \nExtrapessoal \n\n Sujeito a alterações.")
    choice0 = int(input("Deseja proceder para conversa (1) ou estudo de pdfs(2)?"))
    if choice0 == 1 :
        YN = int(input(("Quer que o bot aprenda quieto(0) ou responda algo?(1) \n (Se a matrix for nova, ele será burro como um bebê e repetirá suas palavras)" )))
        responder = (YN == 1)
        algoritmo = input(str("Qual algoritmo será usado?"))
        inpt(matrixName, matrix, dic, responder, algoritmo)
    elif choice0 == 2:
        run_study(matrixName, matrix, dic)
        

#função de estudo de pdfs:
def run_study(matrixName, matrix, dic):
    import livros.pdfReader as p
    #Adicionar meio para que possa ler quais livros estão dentro da sua pasta e só selecionar por um index
    bookName = str(input("qual o nome do livro?"))+".pdf"
    firstPage = int(input("em qual pagina o robô deve iniciar a leitura?"))
    lastPage  = int(input("Até qual pagina a leitura deve ir?"))
    energiaCognitiva = float(input("Quanta atenção o bot deve ter ao livro? (de 0 a 1)"))
    bookContent = p.readBook(bookName, firstPage, lastPage)
    n = 0
    for linha in bookContent:
        n = n+ 1
        print("linha" + str(n))
        print(linha)
        user_message_to_matrix(matrixName, linha, matrix, dic, False, 'b', 0.7, True)
    print("estudo finalizado")

def new_matrix_dic(NewName):
    #adicionar código para nomear sua própria matrix
    matrix = []
    dic = []
    saveMatrix(matrix, NewName)
    saveDic(dic, NewName)
    tela_inicial(NewName, matrix, dic)
        
def old_matrix_dic(matrixname):
    try:
        matrix = loadMatrix(matrixname)
        dic = loadDic(matrixname)
        alreadySaved = True
    except:
        alreadySaved = False
        print("erro no carregamento da matrix. - old_matrix_dic()")
        new_matrix_dic(str(input('Insira um novo nome para a matrix...')))
    if alreadySaved:
        tela_inicial(matrixname, matrix, dic)
   
import os
if __name__ == "__main__":
    ch = int(input("Aperte....\n > 1 para carregar matrix. \n > 2 para criar nova matrix do zero.\n"))
    #adicionar código para selecionar matrix disponíveis na pasta
    if ch == 1:
        print("matrizes disponiveis... \n")
        [print(str(i)[0:-4]) for i in os.listdir('matrixLib')]
        old_matrix_dic(str(input("Insira a matrix escolhida...\n")))
    elif ch == 2:
        yn = str(input("Deseja iniciar uma nova matrix? (S/N)"))
        if yn.lower() == 's':
            new_matrix_dic(str(input('Insira um novo nome para a matrix...')))
        else:
            exit()
    elif ch == 0:
        print("opções de debug \n")
