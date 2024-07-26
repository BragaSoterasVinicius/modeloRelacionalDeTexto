dic = []
matrix = []

def retirar_valor_de_array(valor, array):
    for n in range(array.count(valor)):
        array.remove(valor)

def split_mensagem(mensagem):
    palavrasPorMensagem = mensagem.split()
    return palavrasPorMensagem

def palavras_unicas_por_mensagem(mensagemArray):
    palavrasUnicasPorMensagem = []
    for x in mensagemArray:
        if x not in palavrasUnicasPorMensagem:
            palavrasUnicasPorMensagem.append(x)
    
    return palavrasUnicasPorMensagem

class coluna:
    def __init__(self, titulo):
        self.id = 0
        self.titulo = titulo
        self.corpo = []
        
    def setCorpo(self, pos, value):
        if len(self.corpo) == 0:
            self.corpo.append(0)
        if len(self.corpo)-1 < pos:
            for n in range(len(self.corpo)-1,pos):
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
    retirar_valor_de_array(palavra, mensagemArray)
    coluna = matrix[dic_index(dic, palavra)]
    for n in mensagemArray:
        if dic_index(dic, n) < dic_index(dic, palavra):
            colunaN = matrix[dic_index(dic, n)]
            valor = colunaN.getCorpo(dic_index(dic, palavra) - dic_index(dic, n)-1)
            colunaN.setCorpo(dic_index(dic, palavra) - dic_index(dic, n)-1, valor+1)
        else:
            valor = coluna.getCorpo(dic_index(dic, n) - dic_index(dic, palavra)-1)
            coluna.setCorpo(dic_index(dic, n) - dic_index(dic, palavra)-1, valor+1)
    return coluna.corpo

def is_word_in_dic(dic, word):
    for n in dic:
        if n == word:
            return True
    return False

def add_word_to_dic(dic, word):
    dic.append(word)

def dic_index(dic, word):
    return dic.index(word)

def build_new_palavra(value, matrix, dic):
    add_word_to_dic(dic, value)
    add_coluna(matrix, value)

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


def setup(matrix, dic, n):
    if is_word_in_dic(dic, n) == False:
        add_word_to_dic(dic, n)
    if verify_coluna_existe(matrix, n) == False:
        add_coluna(matrix, n)
        
#response do bot
def bot_response(inp):
    import response as r
    response = r.init_answer(inp)
    return response

#função principal de user -> dict
def user_message_to_matrix(message, matrix, dic):
    messageArray = split_mensagem(message)
    uniquePalavras = palavras_unicas_por_mensagem(messageArray)
    for m in uniquePalavras:
        setup(matrix, dic, m)
    
    for n in uniquePalavras:
        update_value_frequencia_coluna(matrix, dic, messageArray, n)

    #saveCoisas
    saveDic(dic)
    saveMatrix(matrix)

    #futuramente irá retornar uma resposta do bot
    print(bot_response(message))
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
    if ch == 1:
        old_matrix_dic()
    else:
        yn = str(input("Deseja iniciar uma nova matrix? (S/N)\n(estará apagando a antiga...)"))
        if yn.lower() == 's':
            new_matrix_dic(str(input('Insira um novo nome para a matrix...')))
        else:
            exit()
            
