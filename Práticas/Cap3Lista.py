
''' Exercicio 1

def cinco(x):
    return x==5
print(cinco(5))

'''
#---------------------------------------------------------------------------------------

''' Exercicio 2

def dias(horas):
    return round(horas)/24

#print(dias(48))
#print(dias(10))
'''
#-----------------------------------------------------------------------------------------

''' Exericio 3 e 4

def area_circulo(raio):
    return 3.14*(raio**2)

print(area_circulo(1))
print(area_circulo(2))

def area_coroa(r1,r2):
    if(r1>r2):
        raise ValueError("r1 é maior que r2")
    return area_circulo(r2)-area_circulo(r1)

print(area_coroa(1,2))

'''
#----------------------------------------------------------------------------------------

''' Exericio 5 e 6

def bissexto(ano):
    if((ano%4==0 and ano%100!=0) or ano%400==0):
        return True
    else:
        return False

#print(bissexto(1984)) # é
#print(bissexto(1100)) # nao é
#print(bissexto(2000)) # é


def dias_mes(ini,ano):
    if(ini == 'jan' or ini=='mar' or ini=='may' or ini=='jul' or ini=='aug' or ini=='oct' or ini=='dec'):
        return 31
    elif(ini=='apr' or ini=='jun' or ini=='sep' or ini=='nov'):
        return 30
    elif(ini=='feb' and bissexto(ano)):
        return 29
    elif(ini=='feb' and bissexto(ano)):
        return 28
    else:
        raise ValueError("Não corresponde a um mês, está em inglês")

print(dias_mes('jan',2017))
print(dias_mes('feb',2016))
#print(dias_mes('MAR',2017))    
'''        
#--------------------------------------------------------------------------

''' Exercicio 7
# A)

def valor(q,j,n):

    #q - quantida depositada (inteiro pos)
    #j - taxa de juros (entre 0 e 1, abertos)
    #n - número de anos (real)
    #return - valor do depósito ao fim de n anos


    # Value cheking
    if(type(q) != int):
        raise TypeError("valor: q não é um inteiro")
    if(q <= 0):
        raise ValueError("valor: q não é positivo")
    if not(0 < j < 1):
        raise ValueError("value: j não está entre 0 e 1")
    if(type(n) != float and type(n) != int):
        raise TypeError("value: n não é um real")

    return q*((1+j)**n)

print(valor(100,0.03,4))
#Erros
#valor(-1,0.01,4)
#valor(3,2,1)
#valor(4,0.05,'a')

# B)

def duplicar(q,j):
    dobro = q*2
    i=1
    while True:
        if(valor(q,j,i) >= dobro):
            return i
        i+=1

print(duplicar(100,0.03))
'''
#---------------------------------------------------------------------------

''' Exercicio 8 

def serie_geom(r,n):
    if(n < 0):
        raise ValueError("serie_geom: argumento incorrecto")
    
    soma=0
    i=0
    while n >= 0:
        soma += r**i
        n -= 1
        i+=1
    
    return soma

print(serie_geom(2,4))
print(serie_geom(100,0))
#print(serie_geom(100,-1))

'''

#------------------------------------------------------

''' Exercicio 9 (Verificado no google Calendars)
def converter_mes(mes):
    # Converte o mes normal para o que é utilizado na formula
    
    if(mes < 3): #se for janeiro ou fevereiro
        mes = mes + 12
    
    return mes

def chao(x):
    #Converte x no maior número inteiro menor ou igual que x
    
    return int(x) #não pode ser round pois ultrapassaria x

def dia_da_semana(dia,mes,ano):
    mes = converter_mes(mes)

    if(mes > 12):
        ano -= 1

    ano_seculo = ano % 100
    seculo = ano // 100

    #Calcula o resultado da formula
    h = (dia + chao((13*(mes+1))/5) + ano_seculo \
    + chao(ano_seculo/4) + chao(seculo/4) - (2*seculo)) \
    % 7

    dias_semana = ("sabado","domingo","segunda","terça","quarta","quinta","sexta")
    return dias_semana[h]

#print(dia_da_semana(18,1,2014))
#print(dia_da_semana(20,9,2017))
#print(dia_da_semana(8,10,2022))
'''

# -----------------------------------------------

''' Exercicio 10

def inverter(n):
    res = 0
    while n != 0:
        dig = n%10
        res = res*10 + dig
        n = n // 10
    
    return res

def misterio(n):
    #Error checking
    if(type(n) != int):
        raise TypeError("misterio: tipo de argumento invalido")
    if(not(100 <= n < 1000)):
        raise ValueError("misterio: inteiro com mais ou menos que 3 digitos")

    primeiro_dig = n // 100
    ultimo_dig = n % 10
    if(abs(primeiro_dig-ultimo_dig)>1):
        n_i = inverter(n)
        n_s = abs(n - n_i)
        n_si = inverter(n_s)
        return n_s + n_si
    else:
        return "Condições não verificadas"

print(misterio(246))
print(misterio(131))
#print(misterio(1001))

'''
