
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

    def isChar(char):
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

    if(len(string_clean.split()) >= 2):
       dif = width - len(string_clean) 
       whitespaces_original = string_clean.count(' ') # amount of whitespaces on the original string
       
       whitespaces_per_word = () #this tuple specifies how many extra whitespaces will be after each word

       while whitespaces_original != 0: 
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

''' 
cad = ('Os Lusíadas é\t uma obra de poesia épica do escritor português Luís Vaz de Camões, \
a primeira epopeia \nportuguesa         publicada em versão impressa. Provavelmente iniciada em 1556 e concluída em 1571, \
foi publicada em Lisboa em 1572          no período literário do Classicismo, ou Renascimento tardio, três anos após o regresso\
 do autor do Oriente, via \vMoçambique.')

for l in justifica_texto(cad,10): print(l)
'''

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
   
    


def obtem_resultados_eleicoes():
    pass

#print(calcula_quocientes({'A': 12000, 'B': 7500, 'C': 5250, 'D': 3000}, 7))
#print(atribui_mandatos({'A': 12000, 'B': 7500, 'C': 5250, 'D': 3000}, 7))

info = {
            'Endor':   {'deputados': 7, 
                        'votos': {'A':12000, 'B':7500, 'C':5250, 'D':3000}},
            'Hoth':    {'deputados': 6, 
                        'votos': {'A':9000, 'B':11500, 'D':1500, 'E':5000}},
            'Tatooine': {'deputados': 3, 
                        'votos': {'A':3000, 'B':1900}}}

print(obtem_partidos(info))