

# TAD Gerador
# Chosen representation - type: list -> [bits,seed]

def cria_gerador(bits,seed):
    if(type(bits) != int or bits not in (32,64) or type(seed) != int or seed <= 0):
        raise ValueError("cria_gerador: argumentos invalidos")
    return [bits,seed]

def cria_copia_gerador(generator):
    return generator.copy()

def obtem_estado(generator):
    return generator[1]

def define_estado(generator,state):
    generator[1] = state
    return state

def atualiza_estado(generator):
    if generator[0] == 32:
        generator[1] ^= (generator[1] << 13) & 0xFFFFFFFF
        generator[1] ^= (generator[1] >> 17) & 0xFFFFFFFF
        generator[1] ^= (generator[1] << 5) & 0xFFFFFFFF
    elif(generator[0] == 64):
        generator[1] ^= (generator[1] << 13) & 0xFFFFFFFFFFFFFFFF
        generator[1] ^= (generator[1] >> 7) & 0xFFFFFFFFFFFFFFFF
        generator[1] ^= (generator[1] << 17) & 0xFFFFFFFFFFFFFFFF
    return generator[1]

def eh_gerador(arg):
    return (type(arg) == list and arg[0] in (32,64) and type(arg[1]) == int and 0 < arg[1])

def geradores_iguais(gene1,gene2):
    return (eh_gerador(gene1) and eh_gerador(gene2) and gene1[0] == gene2[0] and gene1[1] == gene2[1])

def gerador_para_str(generator):
    return "xorshift" + str(generator[0]) + "(s=" + str(generator[1]) + ")"

# Funções alto-nível para Gerador 

def gera_numero_aleatorio(generator,max):
    '''
    Returns a random number between 1 and max

    generator ->
    max -> int
    return -> int
    '''
    atualiza_estado(generator)
    return 1 + (obtem_estado(generator) % max)


def gera_carater_aleatorio(generator,max):
    '''
    Returns a random character between 'A' and the uppercase character max

    generator ->
    max -> str
    return -> str
    '''
    atualiza_estado(generator)
    max = max.upper()

    #Creates a string using .join() on an iterable made up of the characters 
    #between 'A' and the max char, including these.
    between_A_max = ''.join((chr(x) for x in range(ord('A'),ord(max)+1))) 

    return between_A_max[obtem_estado(generator) % len(between_A_max)]



# --------------------------------------------------

# TAD Coordenada -- imutable datatype!
# Chosen representation: type: tuple -> (col,lin) 

def cria_coordenada(col,lin):
    '''
    Returns a coordinate tuple where the first value is a str representing the column and the second a int representing the line

    col -> str
    lin -> int
    return -> tuple(str,int)
    '''
    if(type(col) != str or type(lin) != int or not('A' <= col <= 'Z') or not(1 <= lin <= 99)):
        raise ValueError("cria_coordenada: argumentos invalidos")

    return (col,lin)

def obtem_coluna(coordinate):
    '''
    Returns the column value of the given coordinate

    coordinate -> tuple(str,int)
    return -> str
    '''
    return coordinate[0]

def obtem_linha(coordinate):
    '''
    Returns the line value of the given coordinate

    coordinate -> tuple(str,int)
    return -> int
    '''
    return coordinate[1]

def eh_coordenada(arg):
    '''
    Returns True if the given argument correctly represents a coordinate,
    that is, if it follows the following representation: (col,lin) where col is a string and lin an int

    arg -> universal
    return -> bool
    '''
    return (type(arg) == tuple and len(arg) == 2 and type(arg[0]) == str and type(arg[1]) == int)

def coordenadas_iguais(c1,c2):
    '''
    Returns True if both coordinates are equal

    c1,c2 -> tuple(str,int)
    return -> bool
    '''
    return (eh_coordenada(c1) and eh_coordenada(c2) and c1[0] == c2[0] and c1[1] == c2[1])

def coordenada_para_str(coordinate):
    '''
    Returns a string that represents the coordinate in the format: "(col)(lin)" or "(col)0(lin)", if lin is only 1 digit

    coordinate -> tuple(str,int) = (col,lin)
    return -> str
    '''
    if(coordinate[1] < 10):
        return coordinate[0] + "0" + str(coordinate[1])
    else:
        return coordinate[0] + str(coordinate[1])


def str_para_coordenada(c_as_text):
    '''
    Returns the coordinate represented by the given string
    
    c_as_text -> str
    return -> tuple(str,int)
    '''
    if(c_as_text[1] == '0'):
        return (c_as_text[0],int(c_as_text[2]))
    else:
        return (c_as_text[0],int(c_as_text[1]+c_as_text[2]))

# Funções alto nível para Coordenada

def obtem_coordenadas_vizinhas(coordinate):
    pass

def obtem_coordenada_aleatoria(coordinate, generator):
    pass

# --------------------------------------------------------

# TAD Parcela

def cria_parcela():
    pass

def cria_copia_parcela(parcel):
    pass

def limpa_parcela(parcel):
    pass

def marca_parcela(parcel):
    pass

def desmarca_parcela(parcel):
    pass

def esconde_mina(parcel):
    pass

def eh_parcela(arg):
    pass

def eh_parcela_tapa(parcel):
    pass

def eh_parcela_marcada(parcel):
    pass

def eh_parcela_limpa(parcel):
    pass

def eh_parcela_minada(parcel):
    pass

def parcelas_iguais(p1,p2):
    pass

def parcela_para_str(parcel):
    pass

# Funções de alto nível para Parcela

def alterna_bandeira(parcel):
    pass

#---------------------------------------------------

# TAD Campo

def cria_campo(last_col,last_lin):
    pass

def cria_copia_campo(field):
    pass

def obtem_ultima_coluna(field):
    pass

def obtem_ultima_linha(field):
    pass

def obtem_parcela(field, coordinate):
    pass

def obtem_coordenadas(field):
    pass

def obtem_numero_minas_vizinhas(field, coordinate):
    pass

def eh_campo(arg):
    pass

def eh_coordenada_do_campo(field, coordinate):
    pass

def campos_iguais(f1,f2):
    pass

def campo_para_str(field):
    pass

# Funções de alto nível para Campo

def coloca_minas(field, coordinate,generator, n_mines):
    pass

def limpa_campo(field, coordinate):
    pass

# ---------------------------------------------------------

# Minesweeper game logic

def jogo_ganho(field):
    pass

def turno_jogador(field):
    pass

# Main function

def minas(last_col,last_lin,n_mines,generator_dimension,seed):
    pass



