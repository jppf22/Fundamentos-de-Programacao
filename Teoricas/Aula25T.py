# Funções recursivas de cauda

def factorial(n):
    def factorial_aux(n,res):
        if n==0:
            return res
        else:
            return factorial_aux(n-1,n*res)
    return factorial_aux(n,1)

print(factorial(10))

def soma_rl(lista):
    if(len(lista) == 0):
        return 0
    else:
        return lista[0] + soma_rl(lista[1:])

def soma_rc(lista):
    def soma_rc_aux(lista,res):
        if(len(lista) == 0):
            return res
        else:
            return soma_rc_aux(lista[1:],res+lista[0])

    if(len(lista) == 0):
        return 0
    else:
        return soma_rc_aux(lista[1:],lista[0])

print(soma_rl([1,2,3,4]))
print(soma_rc([1,2,3,4]))