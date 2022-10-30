

# TAD Gerador

def cria_gerador(bits,seed):
    pass

def obtem_estado(generator):
    pass

def define_estado(generator,state):
    pass

def atualiza_estado(generator, state):
    pass

def eh_gerador(arg):
    pass

def geradores_iguais(gene1,gene2):
    pass

def gerador_para_str(generator):
    pass

# Funções alto-nível para Gerador

def gera_numero_aleatorio(generator,max):
    pass

def gera_carater_aleatorio(generator,max):
    pass

# --------------------------------------------------

# TAD Coordenada

def cria_coordenada(col,lin):
    pass

def obtem_coluna(coordinate):
    pass

def obtem_linha(coordinate):
    pass

def coordenadas_iguais(c1,c2):
    pass

def coordenada_para_str(coordinate):
    pass

def str_para_coordenada(c_as_text):
    pass

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



