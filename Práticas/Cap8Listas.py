
# Exercicio 1--------------------------------------------------------

# a) {'nome':{'nomep':'John', 'apelido':'Doe'},'morada':{'rua':'West Hazeltine Ave.', 'num': 57, 'andar':','localidade':'Kenmore', 'estado':'NY', 'cp':'14317', 'pais':'USA'}}
# b) {'nomep':'John', 'apelido':'Doe'}
# c) 'Doe'
# d) 'D'

# Exercicio 2------------------------------------------
'''
def agrupa_por_chave(pairs):
    res = {}
    for i in pairs:
        if(res.get(i[0]) == None):
            res[i[0]] = [i[1]]
        else:
            res[i[0]].append(i[1])
    return res
            

print(agrupa_por_chave([('a',8),('b',9),('a',3),('b',3),('c',3),('d',3),('d',3),('a',60)]))
'''


# Exercicio 3 ----------------------------------------------

'''
# A)

valores = ('A','2','3','4','5','6','7','8','9','10','J','Q','K')
tipos = ('esp','copas','ouros','paus')

def baralho():
    deck = []
    for i in tipos:
        for j in valores:
            deck.append({'np':i,'vlr':j})
    return deck

#print(baralho())

# B)

from random import random

def baralha(deck):
    max = len(deck)
    for i in range(max):
        multiplier = random() 
        deck[i],deck[int(multiplier*max)] = deck[int(multiplier*max)],deck[i] # a number between 0 and 1 multiplied by length will always land between [0,40[
    return deck

#print(baralha(baralho()))

# C)

def distribui(deck):
    if(len(deck)%4 != 0):
        raise ValueError("distribui: argument needs to have a length that is a multiple of 4")
    cards_per_player = len(deck)//4
    players = []
    i=0
    while i < len(deck):
        players.append(deck[i:i+cards_per_player])
        i += cards_per_player
    return players

print(distribui(baralha(baralho())))
'''

# Exercicio 4 -------------------------------------------------

'''
def resumo_FP(notas_dict):
    alunos_passados = 0
    alunos_reprovados = 0
    notas  = 0
    for i in notas_dict.items():
        if(i[0] >= 10):
            alunos_passados += len(i[1])
            notas += (len(i[1]) * i[0])
        else:
            alunos_reprovados += len(i[1])
    return (notas/alunos_passados,alunos_reprovados)

print(resumo_FP({1 : [46592, 49212, 90300, 59312], \
15 : [52592, 59212], 20 : [58323]}))
'''

# Exercicio 5 ----------------------------------------------------------

'''
def metabolismo(info_pessoas):
    
    nomes = list(info_pessoas.keys())
    nomes.sort()

    res = {}
    for i in nomes:
        if(info_pessoas[i][0] == 'F'):
            res[i] = 655.0 + 4.3*info_pessoas[i][3] + 4.7*info_pessoas[i][2] + 4.7*info_pessoas[i][1]
        else:
             res[i] = 66.0 + 6.3*info_pessoas[i][3] + 12.9*info_pessoas[i][2] + 6.8*info_pessoas[i][1]
    return res

d = {'Maria' : ('F', 34, 1.65, 64), 'Pedro': ('M', 34, 1.65, 64), 'Ana': ('F', 54, 1.65, 120), 'Hugo': ('M', 12, 1.82, 75)}
print(metabolismo(d))
'''

# Exercicio 6 ---------------------------------------------------------------


'''
def conta_palavras(cc):
    palavras = cc.split()
    palavras.sort(key= lambda x: len(x),reverse=True)
    res = {}
    for i in palavras:
        if(res.get(i) == None):
            res[i] = 1
        else:
            res[i] += 1
    return res

cc = 'a aranha arranha a ra a ra arranha a aranha ' \
+ 'nem a aranha arranha a ra nem a ra arranha a aranha'

#print(conta_palavras(cc))


# Exercicio 7 -------------------------------------------------------------

def mostra_ordenado(word_ocurrences):
    resultados = list(word_ocurrences.items())
    while True:
        i = 1
        isSorted = True

        while i < len(resultados):
            if(resultados[i][0] < resultados[i-1][0]):
                isSorted = False
                resultados[i],resultados[i-1] = resultados[i-1],resultados[i]
            i+=1

        if(isSorted): #one full iteration without any swaps --> it means the list is sorted
            break
    
    for palavra in resultados:
        print(palavra[0],palavra[1],sep=' ')

mostra_ordenado(conta_palavras(cc))
'''

# Exericicio 8 ---------------------------------------------------------

# A)

def escreve_esparsa(matriz_esparsa):
    #find width and find heigth
    width, heigth = 0,0
    for posicoes in matriz_esparsa.keys():
        if(posicoes[0]+1 > heigth):
            heigth = posicoes[0]+1
        if(posicoes[1]+1 > width):
            width = posicoes[1]+1
    
    for i in range(heigth):
        for j in range(width):
            finish_char = ' '
            if(j == width-1):
                finish_char = '\n'

            if (i,j) in matriz_esparsa.keys():
                print(matriz_esparsa[(i,j)],end=finish_char)
            else:
                print(0,end=finish_char)

#escreve_esparsa({(1,5):4,(2,3):9,(4,1):1})

# B)

# TÁ MAL

def soma_esparsa(m1,m2):
    for i in m1:
        if(m1[i] in m2.keys()):
            value_in_m2 = m2.get(m1[i])
            m1[m1[i]] = m1[m1[i]] +value_in_m2
            m2.pop(m1[i][0])
        else:
            m1.update(m2[i])
    return m1
e1 = {(1,5): 4, (2, 3): 9, (4, 1): 1}
e2 = {(1, 6): 2, (4, 1): 2, (5,4): 2}
escreve_esparsa(soma_esparsa(e1,e2))

