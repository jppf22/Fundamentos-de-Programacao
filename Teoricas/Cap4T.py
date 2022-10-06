
''' Substituição usando tuplos
def substitui(t,p,e):
    return t[:p] + (e,) + t[p+1:] # :p vai criar um tuplo até p, e p+1: vai criar um tuplo a partir de p+1

a = (1,2,3,4,5)
b = substitui(a,1,'ola')
print(a)
print(b)

'''

'''
def soma(t):
    soma = 0
    i = 0
    max = len(t)

    while(i < max): #chamar a função len(t) repetidamente consome mais memória do que criar uma variável com este valor
        soma += t[i]
        i+=1
    
    return soma

print(soma((1,2,3)))
'''

''' Alterar anterior para obter soma dos quadrados

def soma(t):
    soma = ()
    i = 0
    max = len(t)

    while(i < max): 
        soma += (t[i]**2,)
        i+=1
    
    return soma

print("A soma é:",soma((1,2,3)))
'''

'''

def soma_vetores_for_range(v1,v2): # é assumido que  len(v1) = len(v2)
    res = ()
    for i in range(len(v1)): # i vai tomar os valores de 0 até len(v1)-1 (tal e qual as posições dos elementos do tuplo)
        res = res + (v1[i]+v2[i],)
    return res

print(soma_vetores_for_range((1,2,3),(-1,-2,-3)))
print(soma_vetores_for_range(('a','b','c'),('A','B','C')))

'''

#''' Tabuada com neste for loops
x = int(input("Introduza o máximo: "))

for i in range(1,x+1):
    for j in range(1,11):
        print(i, ' x ', j, " = ", i*j)
#'''


