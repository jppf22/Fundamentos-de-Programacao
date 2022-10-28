
# Ver se são todos pares com funcionais
from functools import reduce

def todos_pares(lista):
    return len(list(filter(lambda x: x%2 == 0, lista))) == len(lista)

def todos_pares_apenas_funcionais(lista):
    return reduce(lambda x,y: x and y, map(lambda x: x%2 == 0, lista))

print(todos_pares([2,4,6,8,10]))
print(todos_pares_apenas_funcionais([2,4,6,8,10]))

# Fazer soma de quadrados impares

def soma_quadrados_impares(lista):
    return reduce(lambda x,y: x+y, map(lambda x: x*x, filter(lambda x: x%2 != 0,lista)))

print(soma_quadrados_impares([1,2,4,5,6]))

# Converter codigo binario a decimal equivalente

def converte(codigo):
    return reduce(lambda x,y: 2*x+y, map(int, codigo))

print(converte('100'))

# Descobrir raiz de um numero através de bissecção

def metodo_bissecao(f,a,b):
    def aproxima_raiz(f,a,b): 
        m = a + (b-a)//2
        delta = 0.001
        while not abs(f(m)) < delta: #enquanto a imagem da abcissa média não for 0
            if(f(m)): #se for > 0, sabemos que a solução está entre m e b
                a = m
            else: #caso contrário, está entre a e m
                b = m
            m = a + (b-a)//2
        return m

    x = f(a)
    y = f(b)
    if y < 0 < x:
        return aproxima_raiz(f,a,b)
    elif x < 0 < y:
        return aproxima_raiz(f,b,a)
    else:
        raise ValueError("metodo bissecao: sinais iguais")

from math import sin, pi
#print(metodo_bissecao(sin,2,4))

# Criar função que "cria" funções de expoente n
def make_power_of(n):
    def power(x):
        return x**n
    return power

'''Igual a make_power_of(n)
return lambda x: x**n
'''

#n = int(input("Introduza um expoente: "))
#pown = make_power_of(n) # creates function that determines the power of 3 of a certain x
#print("2 to the n:", pown(2))

# Cálculo da derivada
def derivada(f):
    def derivada_num_ponto(a):
        delta = 0.000001
        return (f(a+delta)- f(a))/delta
    return derivada_num_ponto #retorna a função derivada para o ponto que o utilizador escolher

g = derivada(sin)
print(g(pi))
