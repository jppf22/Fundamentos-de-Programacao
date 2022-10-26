# Potencia recursiva

def potencia_rec(x,k):
    #caso terminal
    if k == 0:
        return 1
    #caso geral
    elif k > 0:
        return x*potencia_rec(x,k-1)
    raise ValueError("potencia_rec: o expoente não pode ser negativo")

print(potencia_rec(2,10))

# Soma recursiva

def soma_rec_string(x):
    if(len(x) == 1):
        return int(x)
    else:
        return int(x[0]) + soma_rec_string(x[1:])

print(soma_rec_string("1234"))

def soma_rec_natural(x):
    if(x < 10):
        return x
    else:
        return x%10 + soma_rec_natural(x//10)

print(soma_rec_natural(1234))

# Factorial Recursivo

def factorial(x):
    if(x == 1):
        return x
    else:
        return x * factorial(x-1)

print(factorial(5))

# 