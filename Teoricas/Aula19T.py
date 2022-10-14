
# Numero de ocurrencias de cada simbolo---------------------------------------------------

# Para verificar se são letras sem importar podiamos ver se estavam nos intervalos unicode que
# apenas a letras maiusculas ou minusculas

import string

def symboltable(s):
    table = {}

    for c in s.lower(): # converter a string toda para minusculas para não distinguir entre M e m
        if c in string.ascii_letters:
            if c in table:
                table[c] += 1
            else:
                table[c] = 1   

    return table

res = symboltable("Sed up perpisciativs unde omnis")
for k in res:
    print(k, " -----> ", res[k])

# Exericio 2 - How can we print in alphabetical order?-----------------------

for k in sorted(res.keys()):
    print(f'{k} ---> {res[k]}')

# Exericio 3 - Count the total number of symbols--------------------
total = 0
for k in res:
    total += res[k]
print("Total:",total)

# Com sum(list)
print("Total:", sum(res.values()))

#Exercicio 4 - Create a new dict to store frequencies

n_d = {}
for k in res:
    n_d[k] = res[k]/total

for k in n_d:
    print(f'{k} ----> {res[k]}')

#Exercicio 5 - Show frequencies in order without losing key - value relation

def compare(x): #create custom comparison

    return x[1] # will compare the values instead of the keys

    #if we return two values, it will serve to decide in cases of draw
    #Ex: return x[1],x[0] - if the values are equal, it will decide by comparing keys

for item in sorted(n_d.items(), key=compare ,reverse=True): #the comparison will act on the returned values of compare() for each item
    print(f'{item[0]} -----> {item[1]}')


# Crivo de Erastótenes

from math import sqrt

def crivo(n):
    lista = [x for x in range(2,n+1)] # <=> lista = list(rang(2,n+1))
    p = lista[0]
    i=0
    while p <= sqrt(n):
        j = i+1
        while j < len(lista):
            if(lista[j] % p == 0): #Nota: quando acabmos o elemento atual,
                # o proximo vai ocupar o seu indice, logo não é necessário incrementar

                del(lista[j]) #will delete any numbers which have more than 2 divisors
            else:
                j += 1 #se for primo temos que incrementar jota
        i+=1
        p=lista[i]
    
    return lista

print(crivo(100000))


