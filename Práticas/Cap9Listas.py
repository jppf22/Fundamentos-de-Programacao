''' Exercicio 1

def criar_rac(n,d):
    return {'n':n,'d':d}

def num(r):
    return r['n']

def den(r):
    return r['d']

def eh_racional(arg):
    return (type(arg) == dict and list(arg.keys()) == ['n','d'] and type(arg['n']) == int and type(arg['d']) == int and arg['d'] > 0)
        
def eh_rac_zero(r):
    return r['n'] == 0

def rac_iguais(r1,r2):
    return (r1['n']*r2['d'] == r1['d']*r2['n'])

def escreve_rac(r):
    print(str(num(r)) + '/' + str(den(r)))

def produto_rac(r1,r2):
    return criar_rac(num(r1)*num(r2),den(r1)*den(r2))

rac1 = criar_rac(1,3)
print(num(rac1) == 1)
print(den(rac1) == 3)
print(eh_racional(rac1))
print(eh_racional([1,2]))
print(eh_racional({'a':1,'b':3}))
print(eh_rac_zero(rac1))
print(eh_rac_zero(criar_rac(0,2)))
print(rac_iguais(rac1,{'n':2,'d':6}))
escreve_rac(rac1)
'''

# Exercicio 3 ----------------------------------------

'''
def isBissexto(a):
        return ((a%4 == 0 and a%100 != 0) or (a%400 == 0))

def dias_de(m,a):
        if( m in (1,3,5,7,8,10,12)):
            return 31
        elif( m in (4,6,9,11)):
            return 30
        elif(m == 2 and isBissexto(a)):
            return 29
        elif(m==2 and not isBissexto(a)):
            return 28

def cria_data(d,m,a):
    if(type(d) == int and type(m) == int and type(a) == int and (0 <= d <= dias_de(m,a)) and (0 < m < 13)):
        return {'d':d,'m':m,'a':a}

def dia(data):
    return data['d']
def mes(data):
    return data['m']
def ano(data):
    return data['a']

def eh_data(arg): #there are different date formats therefore list[arg.keys()] == ['d','m','a'] is incorrect (ex: American format)
    if(type(arg) == dict and 'd' in arg.keys() and 'm' in arg.keys() and 'a' in arg.keys() and len(arg) == 3):
        if(type(arg['d']) == int and type(arg['m']) == int and type(arg['a'] == int and 0<=arg['d']<=dias_de(arg['m'],arg['a']) and 0 < arg['m'] < 13)):
            return True
    return False

def mesma_data(data1,data2):
    return (data1['m'] == data2['m'] and data1['d'] == data2['d'] and data1['a'] == data2['a'])

def escreve_data(data):
    res = ""

    d = dia(data)
    if(d < 10):
        res += ("0" + str(d))
    else:
        res += str(d)
    
    m = mes(data)
    if(m < 10):
        res += ("/0" + str(m))
    else:
        res += "/" + str(m)
    
    a = ano(data)
    if(a >= 0):
        res += "/" + str(a)
    else:
        res += "/" + str(abs(a)) + " AC"

    print(res)

def data_anterior(data1,data2):
    
    def compare(data):
        return ano(data),mes(data),dia(data)
    
    ordem = [data1,data2]
    ordem.sort(key=compare)

    if(ordem[0] == ordem[1]):
        return False
    elif(ordem[0] == data1):
        return True
    else:
        return False

def idade(nascimento,data_atual):
    if(data_anterior(data_atual,nascimento)):
        raise ValueError("idade: a pessoa ainda não nasceu")
    
    if(mes(data_atual) < mes(nascimento) or ((mes(data_atual) == mes(nascimento)) and (dia(data_atual)<dia(nascimento)))):
        return ano(data_atual)-ano(nascimento)-1
    else:
        return ano(data_atual)-ano(nascimento)

print(idade(cria_data(2, 1, 2003), cria_data(1, 1, 2005)))
'''

# Exercicio 5 --------------------------------------------------------------------

'''
def vetor(x,y):
    if((type(x) == int or type(x) == float) and (type(y) == int or type(y) == float)):
        return (x,y)

def abcissa(v):
    return v[0]

def ordenada(v):
    return v[1]

def eh_vetor(arg):
    return ((type(arg[0]) == int or type(arg[0]) == float) and (type(arg[1]) == int or type(arg[1]) == float))

def eh_vetor_nulo(v):
    return (v[0] == 0 and v[1] == 0)

def vetores_iguais(v1,v2):
    return (v1[0] == v2[0] and v1[1] == v2[1])

def produto_escalar(v1,v2):
    return (abcissa(v1)*abcissa(v2)+ordenada(v1)*ordenada(v2))

v = vetor(-4,0.5)
print(abcissa(v))
print(ordenada(v))
print(eh_vetor(v))
print(eh_vetor(('a',1)))
print(eh_vetor_nulo(v))
print(eh_vetor_nulo((0,0)))
print(vetores_iguais(v,(-4,0.5)))
print(produto_escalar(v,(2,4)))

'''