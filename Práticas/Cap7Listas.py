# Exericico 1 ---------------------------------------

# a) Somatório que começa em i = 0 e vai até n de x * i

# b)
'''
misterior(2,3)
return 2*3 + misterio(2,2)
    return 2*2 + misterio(2,1)
        return 2*1 + misterio(2,0)
            return 0
        return 2+0
    return 4+2
return 6+6

output: 12
'''

#c) Recursão de operações adiadas, estamos sempre a adiar a obtenção do resultado até chegar ao caso terminal

#d)

'''
def misterio(x,n):
    def misterio_aux(x,n,acc):
        if(n==0):
            return acc 
        else:
            return misterio_aux(x,n-1,x*n + acc) #não há operações adiadas, são determinados logo os resultados
    return misterio_aux(x,n,0)

#print(misterio(2,3)) #2*3 + 2*2 + 2*1 + 2*0 = 12

'''

# Exericico 2 -------------------------------------
'''

#a)

def quadrado_rec_adiadas(n):
    if(n == 0):
        return 0
    else:
        return (n+n - 1) + quadrado_rec_adiadas(n-1)

print(quadrado_rec_adiadas(6))

#b)

def quadrado_rec_cauda(n):
    def quadrado_rec_cauda_aux(n, acc):
        if(n == 0):
            return acc
        else:
            return quadrado_rec_cauda_aux(n-1,n+n-1+acc)
    return quadrado_rec_cauda_aux(n,0)

print(quadrado_rec_cauda(6))

#c)

def quadrado_iteracao(n):
    res = 0
    while n > 0:
        res += n+n-1
        n -= 1
    return res

print(quadrado_iteracao(6))
'''

# Exercicio 3 -------------------------

'''
#a)
def numero_digitos_rec_adiada(n):
    if(type(n) != int or n <= 0):
        raise ValueError("numero_digitos_rec_adiada: argumento invalido")
    
    if(n < 10):
        return 1
    else:
        return numero_digitos_rec_adiada(n//10) + 1

print(numero_digitos_rec_adiada(5153534))

#b)
def numero_digitos_rec_cauda(n):
    def numero_digitos_rec_cauda_aux(n,acc):
        if(type(n) != int or n <= 0):
            raise ValueError("numero_digitos_rec_adiada: argumento invalido")

        if(n < 10):
            return acc+1
        else:
            return numero_digitos_rec_cauda_aux(n//10,acc+1)
    return numero_digitos_rec_cauda_aux(n,0)

print(numero_digitos_rec_cauda(5153534))

#c) 

def numero_digitos_iterativo(n):
    if(type(n) != int or n <= 0):
        raise ValueError("numero_digitos_rec_adiada: argumento invalido")
    
    occ = 0
    while n > 0:
        occ += 1
        n = n // 10
    
    return occ

#print(numero_digitos_iterativo(5153534))

# Exericio 4--------------------------------------------------------

def eh_capicua(n):
    def eh_capicua_aux(n):

        if(n == 0 or 0 < n < 10):
            return True

        dig_f = n%10
        dig_i = n//(10**(numero_digitos_iterativo(n)-1))

        if(dig_f != dig_i):
            return False
        else:
            n = n//10
            n = n - dig_i*(10**(numero_digitos_iterativo(n)-1))
            return eh_capicua_aux(n)
    return eh_capicua_aux(n)

#print(eh_capicua(10101)) #se não alteressamos o numero original e passasemos parametros que são o n da esquerda e da diretia seria possivel
#print(eh_capicua(1221))
#print(eh_capicua(12121))

def eh_capicua_str(n):

    def aux(n):
        if(len(n) == 1 or len(n)==0):
            return True
        
        if(n[0] != n[-1]):
            return False
        else:
            n = n[1:len(n)-1]
            return aux(n)

    length = numero_digitos_iterativo(n)
    if(length == 1):
        return True
    else:
        return aux(str(n))
'''

# Exercicio 5 ---------------------------------------

'''
def espelho(n):
    def espelho_aux(n,res):
        if(-1<n<10):
            return res*10 + (n%10)
        else:
            return espelho_aux(n//10,res*10+(n%10))

    if(-1 < n < 10):
        return n
    else:
        return espelho_aux(n,0)

print(espelho(381))
print(espelho(45674))
'''

# Exercicio 6 ------------------------------------------

# a)
'''
def g_recursiva(n):
    if(n == 0):
        return 0
    else:
        return n - g_recursiva(g_recursiva(n-1))

print(g_recursiva(3))
'''
# b)
'''
g(3):
    g(g(2)):
        g(2):
            g(g(1)):
                g(1):
                    g(g(0)):
                        g(0):
                        return 0
                    return 0
                return 1 - 0
            return 1 - 1
        return 2 - 0
    return 2 - 2
return 3 - 0
'''

#c) O processo é recursivo de operações adiadas (sendo esta n - g(g(n-1)))

# Exercicio 7 --------------------------------------------

'''
def calc_soma(x,n):
    def factorial(n):
        if(n == 0 or n==1):
            return 1
        else:
            return n*factorial(n-1)
    
    if(n == 0):
        return 1
    else:
        return (x**n)/factorial(n) + calc_soma(x,n-1)

print(calc_soma(1,3))
'''
#Nota: esta é a forma do enunciado
'''
def calc_soma(x,n):
    def aux(x,n,at,res,ult):
        if(at == n):
            return res + ult * (x/at)
        else:
            return aux(x,n,at+1,res + ult*(x/at),ult*(x/at))
    return aux(x,n,1,1,1)
print(calc_soma(1,3))
'''

# Exercicio 8 ----------------------------------------------

'''
def maior_inteiro(limite):
    def aux(limite,n,res):
        if(n + res <= limite and n + (n+1) + res <= limite):
            return aux(limite,n+1,res + n)
        else:
            return n
    return aux(limite,1,0)

print(maior_inteiro(6))
print(maior_inteiro(20))
print(maior_inteiro(1))
'''

# Exercicio 9 ------------------------------------------------

'''
def soma_divisores(n):
    def aux(n,d,acc):
        if(d == 0):
            return acc
        elif(n % d == 0):
            return aux(n,d-1,acc+d)
        else:
            return aux(n,d-1,acc)
    
    return aux(n,n,0)

print(soma_divisores(7))
print(soma_divisores(8))
'''

# Exercicio 10 ------------------------------------------------

# a)
'''
def perfeito_cauda(n):
    def aux(n,d,acc):
        if(d == 0):
            return acc
        elif(n % d == 0):
            return aux(n,d-1,acc+d)
        else:
            return aux(n,d-1,acc)
    
    return (aux(n,n-1,0) == n)

print(perfeito_cauda(6))

#b)

def perfeitos_entre(n1,n2):
    if(n1 == n2):
        return ([n2] if perfeito_cauda(n2) else [])
    else:
        return ([n1] if perfeito_cauda(n1) else []) + perfeitos_entre(n1+1,n2)

print(perfeitos_entre(6,30))
'''