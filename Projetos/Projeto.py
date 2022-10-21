
# Exericio 1 ---------------------------------------------------------------
def limpa_texto(string):
    '''
    Returns a 'clean' string, that is, 
    a string which has no 'blank characters',
    with the exception of single whitespaces separating words.

    By 'blank characters' we define '\t','\n','\v','\f',
    '\r' and ' '

    string -> str
    return -> str
    '''

    blank_characters = ('\t','\n','\v','\f','\r')

    for i in blank_characters: 
        string = string.replace(i,' ')

    string = string.split() #With no arguments, Python will use ' ' as the delimiter and consider any group of whitespaces as a single one
    string = ' '.join(string)

    return string



def corta_texto(string_clean, width):
    '''
    Returns two 'clean' substrings of string_clean:
        - One containing each full word since the beginning of string_clean, including spaces, until reaching a maximum length that's equal to the width
        - The other containing what's left
    
    string_clean -> str
    width -> int
    return -> tuple(str,str)
    '''

    def isChar(char): #substituir por builtin
        return (char != ' ')

    if(len(string_clean) <= width):
        return (string_clean, "")

    sub_string1 = string_clean[:width] 
    while width != 0:
        #If substring1 has an incomplete word -> we need to make it shorter until there are only full words in it(since its maximum length is width)
        if(isChar(string_clean[width-1]) and isChar(string_clean[width])):
            sub_string1 = string_clean[:width-1]
        else:
            return (limpa_texto(sub_string1),limpa_texto(string_clean[width:]))
            # limpa_texto(sub_string1[:width-1])
            #se tem espaço ? a : b
            # ternary operator
        width -= 1
    
    return("",string_clean) #No full word fits the given width


def insere_espacos(string_clean, width):
    '''
    Returns a string that fits the given width 
    by adding whitespaces between each words (if there is more than 1 word) 
    or by adding whitespaces to the end of the string (otherwise).

    string_clean -> str
    width -> int
    return -> str
    '''

    def num_whitespaces(dif,whitespaces_left):
        '''Returns how many extra whitespaces must be put between each word'''
        if(whitespaces_left == 1):
            return dif
        
        return int(dif//whitespaces_left) + (dif%whitespaces_left > 0)

    def get_whitespaces(num):
        '''Returns a string made up of the necessary number of ' ' after a given word position'''
        res = ' ' 
        while num != 0:
            res += ' '
            num -= 1
        return res

#
#    string[] resultado final = string[width final que tu queres]
#    int pos = 0

#    int maxespacosnovos = X;
#    int espaçoCada = calcula espaços entre palavras (espacos total/espacos)
#    int restodadivisao = Y
#    for  int i = 0 ; i < string_clean.length(); i++
#        if string_clean[i] == espaco
#          for int j = i ; j < espaçoCada ; j++
#            resultados[pos++] = espaço
#          if (restoDaDivisao > 0)
#            resultado[pos++] = espaço
#            restoDaDivisao--  
#        else
#          resultado[pos++] = string_clean[i];
#
#
#

    if(len(string_clean.split()) >= 2):
       dif = width - len(string_clean) 
       whitespaces_original = string_clean.count(' ') # amount of whitespaces on the original string
       
       whitespaces_per_word = () #this tuple specifies how many extra whitespaces will be after each word

       while whitespaces_original != 0:  #----------------- Aqui dá para não chamar num_whitespaces 3 vezes se colocarmos uma condição que soma se ainda houver resto da divisão dif//whitespaces_original
            whitespaces_here = num_whitespaces(dif,whitespaces_original)
            whitespaces_per_word += (whitespaces_here,)
            dif -= whitespaces_here
            whitespaces_original -= 1
       
       words = string_clean.split()
       string_final = ""
       for i in range(0,len(words)-1): #the last word isn't followed by a whitespace there we use len(words)-1
            string_final = string_final + words[i] + get_whitespaces(whitespaces_per_word[i])

       return string_final + words[len(words)-1]
        
    else: 
        return string_clean.ljust(width,' ')


def justifica_texto(string,width):
    '''
    Returns a justified text that fits the given width
    
    string -> str
    width -> int
    return -> tuple (made up of str elements)
    '''

    if(len(string)==0 or width <= 0 or type(string) != str or type(width) != int):
        raise ValueError("justifica_texto: argumentos invalidos")


    string_toparse = limpa_texto(string)

    #verificação NOVA
    for palavras in string_toparse.split():
        if(len(palavras) > width):
            raise ValueError("justifica_texto: argumentos invalidos")
    
    string_tuple = ()
    
    while string_toparse != "":
        string_temp,string_toparse = corta_texto(string_toparse,width)
        if(string_toparse == ""):
            string_tuple += (string_temp.ljust(width,' '),)
        else:
            string_tuple += (insere_espacos(string_temp,width),)
    
    return string_tuple


#print(limpa_texto("\v    \t Fundamentos     \n\t \v     da   \f      Programacao\n          "))
#print(corta_texto("Fundamentos da Programacao",15))


cad = ('Os Lusíadas é\t uma obra de poesia épica do escritor português Luís Vaz de Camões, \
a primeira epopeia \nportuguesa         publicada em versão impressa. Provavelmente iniciada em 1556 e concluída em 1571, \
foi publicada em Lisboa em 1572          no período literário do Classicismo, ou Renascimento tardio, três anos após o regresso\
 do autor do Oriente, via \vMoçambique.')

#for l in justifica_texto(cad,10): print(l)


# Exercicio 2 ---------------------------------------------------------------------
def calcula_quocientes(votes_per_party,num_representatives):
    '''
    Returns a dictionary whose keys correspond to political parties
    and values correspond to the quotients, in descending order, 
    according to the Hondt method

    votes_per_party -> dict
    num_representatives -> int
    return -> dict{str:list}
    '''

    quotients_per_party = votes_per_party.copy()
    for i in range(len(quotients_per_party)):
        quotients = [list(quotients_per_party.values())[i]/x for x in range(1,num_representatives+1)]
        quotients_per_party[list(quotients_per_party.keys())[i]] = quotients
    return quotients_per_party

    

def atribui_mandatos(votes_per_party,num_representatives):
    '''
    Returns a list with a length equal to the number of representatives
    in which element corresponds to the political party that got the
    representative at that position (equal to the index+1)

    votes_per_party -> dict
    num_representatives -> int
    return -> list[str]
    '''
    def biggest_quotient(quotients_per_party):
        biggest = 0
        for i in quotients_per_party.values():
            for j in i:
                if(j > biggest):
                    biggest = j
        return biggest

    def which_has_less_votes(party1):
        return votes_per_party[party1]

    quotients_per_party = calcula_quocientes(votes_per_party,num_representatives)
    representatives_party = []

    for i in range(num_representatives):
        biggest_quotient_left = biggest_quotient(quotients_per_party)
        winner_parties = [i for i in quotients_per_party if biggest_quotient_left in quotients_per_party[i]]

        if(len(winner_parties) == 1):
            representatives_party.append(winner_parties[0])
        else: #if there is a draw
            winner_parties.sort(key=which_has_less_votes)
            for i in winner_parties:
                representatives_party.append(i)
                if(len(representatives_party) == num_representatives):
                    return representatives_party

        for i in quotients_per_party:
            if(biggest_quotient_left in quotients_per_party[i]): 
                quotients_per_party[i].remove(biggest_quotient_left)

    return representatives_party


def obtem_partidos(info_about_elections):
    '''
    Returns a list, in alfabetic order, with the name of each politcal party
    that participated in these elections-

    info_about_elections -> dict
    return -> list
    '''
    names = []
    for election_circle in info_about_elections.values():
        votes_circle = list(dict(election_circle).values())
        parties_circle = votes_circle[1]
        names_circle = list(parties_circle.keys())
        for i in names_circle:
            if(i not in names):
                names.append(i)
    
    return sorted(names)

def obtem_resultado_eleicoes(info_about_elections):
    '''
    Returns a list with the results of the elections per political party

    info_about_elections -> dict
    return -> list[tuple(str,int,int)]
    '''

    if(type(info_about_elections) != dict):
        raise ValueError("obtem_resultado_eleicoes: argumento invalido")

    parties = obtem_partidos(info_about_elections)
    election_circles = list(info_about_elections.keys())
    votes_seats_per_party = {} #format {party: [seats,votes]}

    for i in election_circles: 
        seats = info_about_elections[i]['deputados']
        votes = info_about_elections[i]['votos']
        mandates = atribui_mandatos(votes,seats)

        for j in parties: 

            if(j not in list(votes.keys())):
                continue

            seats_per_party = mandates.count(j)
            votes_per_party = votes[j]
            if(votes_seats_per_party.get(j) == None):
                votes_seats_per_party[j] = [0,0]
            votes_seats_per_party[j][0] += seats_per_party
            votes_seats_per_party[j][1] += votes_per_party

    res = list(votes_seats_per_party.items())

    for i in range(len(res)):
        res[i] = (res[i][0],res[i][1][0],res[i][1][1])

    res.sort(key=lambda x:(x[1],x[2]),reverse=True)
    return res
    
#print(calcula_quocientes({'A': 12000, 'B': 7500, 'C': 5250, 'D': 3000}, 7))
#print(atribui_mandatos({'A': 12000, 'B': 7500, 'C': 5250, 'D': 3000}, 7))
#info = {'Endor':   {'deputados': 7, 'votos': {'A':12000, 'B':7500, 'C':5250, 'D':3000}},'Hoth':    {'deputados': 6, 'votos': {'A':9000, 'B':11500, 'D':1500, 'E':5000}}, 'Tatooine': {'deputados': 3, 'votos': {'A':3000, 'B':1900}}}
#print(obtem_partidos(info))
#print(obtem_resultado_eleicoes(info))

def produto_interno(vector1,vector2):
    '''
    Returns the intern product of the given two same-dimension vectors

    vector1 -> tuple
    vector2 -> tuple
    return -> float
    '''
    return sum([vector1[x]*vector2[x] for x in range(len(vector1))])

def verifica_convergencia(matrice,vector_constants,current_solution,precision):
    '''
    Returns true if every equation of the expanded matrice has an absolute error inferior to the given precision

    matrice -> tuple
    vector_constants -> tuple
    current_solution -> tuple
    return -> bool
    '''
    length = len(matrice) #we know we will have same number of columns and rows
    for i in range(length):
        summation = produto_interno(matrice[i],current_solution)
        if abs(summation - vector_constants[i]) > precision:
            return False
    return True

#print(verifica_convergencia(((1, -0.5), (-1, 2)), (-0.4, 1.9), (0.1001, 1), 0.00001))
#print(verifica_convergencia(((1, -0.5), (-1, 2)), (-0.4, 1.9), (0.1001, 1), 0.001))

def retira_zeros_diagonal(matrice,vector_constants):
    '''
    Returns a reorganized matrice where there aren't 0's on the main diagonal 
    and a vector reflecting the same operations used on the matrice

    matrice -> tuple(tuple)
    vector_constants -> tuple
    return -> tuple(tuple,tuple)
    '''
    def isLineSwitchable(line1,n_line1,line2,n_line2):
        '''Indicates wether line1 and line2 can switch with one another or not, so no 0's are in the diagonal'''
        return (line1[n_line2] != 0 and line2[n_line1]!= 0)

    matrice_temp = list(matrice)
    constants_temp = list(vector_constants)

    for i in range(len(matrice)):
        if matrice_temp[i][i] == 0: #if there is a zero on the main diagonal

            for j in range(len(matrice)):
                if isLineSwitchable(matrice_temp[i],i,matrice_temp[j],j):
                    matrice_temp[i],matrice_temp[j] = matrice_temp[j],matrice_temp[i]
                    constants_temp[i],constants_temp[j] = constants_temp[j],constants_temp[i]
                    break
    
    return (tuple(matrice_temp),tuple(constants_temp))

#print(retira_zeros_diagonal(((3,4,0,6,7),(3,5,7,0,9),(4,4,4,4,4),(0,1,2,3,4),(8,9,1,2,0)), (1, 2, 3,4,5)))
    
def eh_diagonal_dominante(matrice):
    '''
    Returns true if the received matrice is diagonally dominant, false otherwise
    
    matrice -> tuple(tuple)
    return -> bool
    '''

    for i in range(len(matrice)):
        if not (sum(matrice[i]) <= abs(2*(matrice[i][i]))): #if a diognal entry is not bigger then the sum of the restant entries in a row -> the diagional is not dominant
            return False
    return True

def resolve_sistema(matrice,vector_constants,precision):
    '''
    Returns the solution to the given equation system (augmented matrice) using the Jacobi method

    matrice -> tuple(tuple)
    vector_constants -> tuple
    precision -> float
    return -> tuple
    '''
    def invalid_argument():
        raise ValueError("resolve_sistema: argumentos invalidos")

    def isErrorSmallerThanPrecision():
        def equation_error(n_equation):
            return abs(produto_interno(matrice[i],current_solution)-vector_constants[i])
        
        for i in range(len(matrice)):
            if(equation_error(i) > precision):
                return False
        return True

    # Argument validation
    if(type(matrice) != tuple or type(vector_constants) != tuple or \
        (type(precision) != float and type(precision) != int) or precision <= 0):
        invalid_argument()
    
    for i in matrice:
        if(type(i) != tuple):
            invalid_argument()
        for j in i:
            if(type(j) != int and type(j) != float):
                invalid_argument()
    
    matrice,vector_constants = retira_zeros_diagonal(matrice,vector_constants)

    if not eh_diagonal_dominante(matrice):
        raise ValueError("resolve_sistema: matriz nao diagonal dominante")
    
    # Discover solution
    current_solution = tuple([0 for x in range(len(matrice))])

    while not isErrorSmallerThanPrecision():
        temp_solution = ()
        for i in range(len(current_solution)):
            temp_solution += ((current_solution[i] + (vector_constants[i] - produto_interno(matrice[i],current_solution))/matrice[i][i]),)
        current_solution = temp_solution

    return current_solution

A4, c4 = ((2, -1, -1), (2, -9, 7), (-2, 5, -9)), (-8, 8, -6)
#print(resolve_sistema(A4, c4, 1e-20))
