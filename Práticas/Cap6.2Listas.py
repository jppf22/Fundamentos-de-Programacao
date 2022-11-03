
# Exercicio 1 ----------------------------

#a) Soma os termos dos múltiplos de 1 começando em 4 
#e terminando em 500

#b) Soma os quadrados dos múltiplos de 5 começando 
# em 5 e acabando em 500

#c) Soma os somatórios dos múltiplos de 1 de 1 a n, 
# sendo n o termo atual, para os n termos múltiplos de 1 
# começando em 1 e acabando em 5

# Exericico 2 -------------------------------

#a) 

from functools import reduce


def piatorio(l_inf,l_sup,func):
    produto = 1
    while l_inf <= l_sup:
        produto *= func(l_inf)
        l_inf += 1
    return produto

#print(piatorio(1,5,lambda x: 2*x))

#b)
n = 3
factorial = piatorio(1,n,lambda x:x)
print(factorial)

# Exericio 3 -----------------------------------------

'''
# a)
def soma_fn(n,fn):
    soma = 0
    for i in range(1,n+1):
        soma += fn(i)
    return soma

#print(soma_fn(4,lambda x: x*x))
#print(soma_fn(4,lambda x: x+1))

#b)

def soma_fn_rec(n,fn):
    if(n == 1):
        return fn(1)
    else:
        return fn(n) + soma_fn(n-1,fn)

#print(soma_fn_rec(4,lambda x: x*x))
#print(soma_fn_rec(4,lambda x: x+1))
'''

# Exericio 4 ------------------------------------

'''
#a)

def filtra(lst1,tst):
    if(len(lst1) == 0):
        return []
    else:
        if(tst(lst1[0])):
            return [lst1[0]] + filtra(lst1[1:],tst)
        else:
            return filtra(lst1[1:],tst)
print(filtra([1,2,3,4,5],lambda x: x%2 == 0))

#b)

def transforma(lst1,fn):
    if(len(lst1) == 0):
        return []
    else:
        return [fn(lst1[0])] + transforma(lst1[1:],fn)

print(transforma([1,2,3,4],lambda x: x**3))

#c)

def acumula(lst1,fn):
    if(len(lst1) == 1):
        return lst1[0]
    else:
        return acumula([fn(lst1[0],lst1[1])]+lst1[2:],fn)

print(acumula([1,2,3,4],lambda x,y: x+y))
print(acumula([1,2,3,4,5],lambda x,y: x+y))
'''

# Exercicio 5 --------------------------------

# Era suposto usar os do exercicio anterior
'''
def soma_quadrados_impares(lst):
    return reduce(lambda x,y: x+y, map(lambda x: x**2,filter(lambda x: x%2 != 0,lst),))

print(soma_quadrados_impares([1,2,3,4,5,6]))
'''

# Exercicio 6 ------------------------------------

'''
def eh_primo(n):
    if n == 1:
        return False
    else:
        for i in range(2,n):
            if n%i == 0:
                return False
        return True

def não_primos(n):
    return list(filter(lambda x: not eh_primo(x),range(1,n+1))) #começa em 1 porque são inteiros positivos

print(não_primos(10))
'''

# Exercicio 7 --------------------------------------

# a) Devolve o numero composto pelos digitos de n que cumprem o predicado

# b) 
'''
def filtra_pares(n):
    return misterio(n,lambda x: x%2 == 0)
'''

# Exercicio 8 -------------------------------------

'''
def lista_digitos(n):
    return list(map(lambda x: int(x), str(n)))

#print(lista_digitos(123))

# Exercicio 9 -----------------------------------

def produto_digitos(n,pred):
    return reduce(lambda x,y:x*y, filter(pred,lista_digitos(n)))

#print(produto_digitos(12345, lambda x: x > 3))

# Exercicio 10 ----------------------------------

def apenas_digitos_impares(n):
    return reduce(lambda x,y: x*10+y,filter(lambda x: x % 2 != 0, lista_digitos(n)))

#print(apenas_digitos_impares(123456789))
'''