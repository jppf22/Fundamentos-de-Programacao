
# Recursão em árvore optimizada -- Sequência Fibonacci

def fib(n):
    mem = {0:0, 1:1}
    def aux(n):
        if n in mem:
            return mem[n]
        else:
            mem[n] = aux(n-1)+aux(n-2)
            return mem[n]
    return aux(n)

#print(fib(10))


# Aceder a elementos atómicas de listas com sublistas...

def elementos_atom(tp):
    if not tp: #null value
        return 0
    else:
        if(type(tp[0]) == tuple):
            return elementos_atom(tp[0])+elementos_atom(tp[1:])
        else:
            return tp[0] + elementos_atom(tp[1:])

'''Nota: slicing a tuple doesn't throw an error whenever there is only 1 element since
there are actually two elements (3,) one tp[0] is 3 the other tp[1] is none'''

#print(elementos_atom((1,1,1,((((1,1,1),1,(),(1,1,1)))),(1,(1,1,(1))))))

# Aula 27T

# Misturar a soma de n quadrados com a soma de n naturais

def somatorio(l_inf,l_sup,fun):
    res = 0
    for x in range(l_inf,l_sup+1):
        res += fun(x)
    return res

def quadrado(x):
    return x*x

def identidade(x):
    return x

#print(somatorio(1,10,identidade))
#print(somatorio(1,3,quadrado))

# Programa reescrito usando funções anónimas e com stepping customizado

def somatorio_ano(l_inf,l_sup,fun_trans,fun_step):
    res = 0
    x = l_inf
    while x <= l_sup:
        res += fun_trans(x)
        x = fun_step(x) #o loop itera com a frequencia que quisermos
    return res

#print(somatorio_ano(1,10,lambda x: x, lambda x: x+1))
#print(somatorio_ano(0,100,lambda x: x/100,lambda x: x+50))    #1.5


# Customizar ordem de sorting de iterável

lst = ['AAAAAAA','BBBB','c','A','AAAA','AAAAAAAAAAAAAAAAAAAAA','b','BBB']
lst.sort(key=lambda x: (len(x), ord(x[0].upper()))) #compara primeiro pela length e depois pela ordem alfabetica da primeira letra
#print(lst)
    