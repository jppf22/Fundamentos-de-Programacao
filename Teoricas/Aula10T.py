''' Conversão de temperatura: Fahrenheit para Celsius

def fahr_para_cent(fahr):
    return (5 * (fahr-32)/9)

def tabela(min_f, max_f):
    while(min_f <= max_f):
        print(min_f, "F = ", fahr_para_cent(min_f), "Cº")
        min_f+= 1

tabela(40,50)
'''

#-----------------------------------------------------

#''' Potência (iterativa)

#Refazer com expoentes positivos e negativos


#-----------------------------------------------------

''' Fatorial

def fat(n):
    res = 1
    while n >0:
        res = res * n
        n -= 1
    return res

print(fat(5))
'''

#-----------------------------------------------------

''' Máximo divisor comum

def mcf(m,n):
    if((type(m) == int) and (type(n) == int)) and m > 0  and n > 0:
        while n!=0:
            m,n = n, m%n
        return m
    else:
        raise ValueError("Os argumentos não são válidos.")

print(mcf(16,24))
'''
#------------------------------------------------------

#''' Raiz quadrada

from math import sqrt

def calcula_raiz(x, palpite):
    while not bom_palpite(x, palpite):
        palpite = novo_palpite(x,palpite)
    return palpite

def bom_palpite(x,palpite):
    delta = 1e-10
    return (abs(palpite*palpite-x) < delta)

def novo_palpite(x, palpite):
    return palpite((palpite + (x/palpite))/2)

def raiz(x):
    if x < 0:
        raise ValueError("raiz definida só para números positivos")
    return calcula_raiz(x, x/2)

print(raiz(2))
print(sqrt(2))
#'''