
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
    Returns a string that fits the given width by adding spaces between each words,
    if it has more than 1 word, or adds spaces to the end of the string, if otherwise.

    string_clean -> str
    width -> int
    return -> str
    '''

    def num_whitespaces(dif,whitespaces_left): #used to figure out how many whitespaces (not counting the originals) must be put between each word, except the last
        if(whitespaces_left == 1):
            return dif
        
        return int(dif//whitespaces_left) + (dif%whitespaces_left > 0)

    def get_whitespaces(num):
        res = ''
        while num != 0:
            res += ' '
            num -= 1
        return res

    if(len(string_clean.split()) >= 2):
       dif = width - len(string_clean) #this amount will be filled by whitespaces
       whitespaces = string_clean.count(' ')
       
       whitespaces_per_word = () #this tuple specifies how many whitespaces will be after each word, except the last (a 'clean string' ends with a word)

       while whitespaces != 0: 
            whitespaces_here = num_whitespaces(dif,whitespaces)
            whitespaces_per_word += (whitespaces_here,)
            dif -= whitespaces_here
            whitespaces -= 1

       words = string_clean.split()
       string_final = ""
       for i in range(0,len(words)-1): #if we used only len(word), whitespaces_per_word would go out of range
            string_final = string_final + words[i] + get_whitespaces(whitespaces_per_word[i]+1)

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

