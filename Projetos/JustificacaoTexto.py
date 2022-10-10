
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
    pass

def insere_espacos(string_clean, width):
    pass

def justifica_texto(string,width):
    pass

print(limpa_texto("\v    \t Fundamentos     \n\t \v     da   \f      Programacao\n          "))