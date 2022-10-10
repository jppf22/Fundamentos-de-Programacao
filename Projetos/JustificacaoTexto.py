
def limpa_texto(string):
    '''
    Returns a 'clean' string, that is, 
    a string which has no 'blank characters',
    with the exception of single whitespaces separating words.

    By 'blank characters' we define '\t','\n','\v','\f',
    '\r' and ' '
    '''

    blank_characters = ('\t','\n','\v','\f','\r')

    for i in blank_characters: #Replaces any blank_characters, except ' ', with a whitespace ' '
        string = string.replace(i,' ')

    string = string.split() #With no arguments, Python will use ' ' as the delimiter and consider any group of whitespaces as a single one
    string = ' '.join(string)

    return string



def corta_texto(string_clean, width):
    '''
    Returns two 'clean' substrings of string_clean:
        - One containing each full word since the beginning of string_clean, including spaces, until reaching a maximum length that's equal to the width
        - The other containing what's left
    '''

    def isChar(char):
        return (char != ' ')

    if(len(string_clean) <= width): #String is smaller or equal to the width - return full string
        return (string_clean, "")

    sub_string1 = string_clean[:width] #String is bigger than the width
    while width != 0:
        #If substring1 has an incomplete word -> we need to make it shorter until there are only full words in it(since its maximum len is width)
        if(isChar(string_clean[width-1]) and isChar(string_clean[width])):
            sub_string1 = string_clean[:width-1]
        else:
            return (limpa_texto(sub_string1),limpa_texto(string_clean[width:]))
        width -= 1
    
    return("",string_clean) #No full word fits the given width


def insere_espacos(string_clean, width):
    pass

def justifica_texto(string,width):
    pass

print(limpa_texto("\v    \t Fundamentos     \n\t \v     da   \f      Programacao\n          "))
print(corta_texto("Fundamentos da Programacao",15))

