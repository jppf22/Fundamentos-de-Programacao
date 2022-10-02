

''' Exemplos Funções

def soma(x,y):
    return x+y

print(soma(7,5)) 

'''

''' Exemplo com recursão (NÃO É SUPOSTO USAR ATÉ SER DADO)
def soma_ar(n):
    if(n == 1):
        return n
    else:
        return n + soma_ar(n-1)

print(soma_ar(10))
'''

''' Exemplos de uso de erro/excepções

x = eval(input("Introduza um número: "))

def inverte(n):
    if(type(n) == int or type(n) == float) and n != 0:
        return 1/n
    elif n == 0:
        raise ZeroDivisionError("inverte: divisão por zero")
    else:
        raise ValueError("inverte: argumento inválido") #por enquanto quando levantarmos um erro será sempre um catastrófico (termina o programa)        

print("O inverso do número é ", inverte(x))

'''
