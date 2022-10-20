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

def isBissexto(a):
        return ((a%4 == 0 and a%100 != 0) or (a%400 == 0))

def dias_de(m,a):
        if( m in (1,3,5,7,8,10,12)):
            return 31
        elif( m in (4,6,9,11)):
            return 30
        elif(m == 2 and isBissexto(a)):
            return 29
        elif(m==2 and isBissexto(a)):
            return 28

def cria_data(d,m,a):

    if(type(d) == int and type(m) == int and type(a) == int and 0<=d<=dias_de(m,a) and 0 < m < 13):
        return {'d':d,'m':m,'a':a}

def dia(data):
    return data['d']
def mes(data):
    return data['m']
def ano(data):
    return data['a']

def eh_data(arg): #there are different date formats therefore list[arg.keys()] == ['d','m','a'] is incorrect (ex: American format)
    pass
