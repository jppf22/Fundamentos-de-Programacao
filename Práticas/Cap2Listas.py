''' Exercicio 2
x = eval(input("Introduza uma distância (km): "))
y = eval(input("Tempo necessário para a percorrer (m): "))

print("Velocidade Média (km/h): ", float(x/(y/60)))
print("Velocidade Média (m/s): ", float((x*1000)/(y*60)))

'''
# -----------------------------------------------

'''  Exercico 3
segs = eval(input("Escreva um número de segundos: "))
print("O seu número de dias é ", segs/(3600*24))
'''

#---------------------------------------------------

''' Exercicio 4

segs = eval(input("Escreva um número de segundos: "))
dias = segs//(3600*24)
segs = segs%(3600*24)

horas = segs//(3600)
segs = segs%(3600)

minutos = segs//60
segs = segs%60

print("dias: ", dias, "horas: ", horas, "minutos: ", minutos, "segundos: ", segs)
'''

# --------------------------------------------------------

''' Exercicio 5

from math import sqrt

values = []
num_values = int(input("Quantos números tem a sua sequência? Resposta: "))
i = 0

while i < num_values :
    values.append(float(input("Introduza um número: ")))
    i += 1

#calcular a media dos numeros
media = 0
for x in range(num_values):
    media += values[x]
media = media/num_values

#Calcular o desvio
soma_desvios = 0

for x in range(num_values):
    soma_desvios += ((values[x]-media)**2)
desvio_padrao = sqrt((1/4)*soma_desvios)

#Mostrar os resultados
print("Resultados:\nMédia: ", media, "\nDesvio padrão: ", desvio_padrao)

'''
#--------------------------------------------------------------

''' Exercicio 6

#Com conhecimento prévio
values = []
amount = int(input("Quantos números quer comparar: "))

for x in range(amount):
    values.append(float(input("Introduza um número: ")))

biggest = 0
for x in range(amount):
    if(values[x]>biggest):
        biggest = values[x]
print("The biggest of your numbers is: ", biggest)

'''
'''
#Sem conhecimento prévio
a = float(input("Introduza um número: "))
b = float(input("Introduza um número: "))
c = float(input("Introduza um número: "))


print("The biggest number is: ", end='')
if(a > b and a > c):
    print(a)
elif(b > a and b > c):
    print(b)
else:
    print(c)    
'''

#-------------------------------------------------------

''' Exercicio 7

horas = float(input("Quantas horas trabalhou esta semana (incluindo extras)?\nR:"))
salario_h= float(input("Qual é o seu salário/hora ?\nR: "))

print("Esta semana irá ganhar ", end='')
if horas <= 40:
    print(salario_h*horas, " €.")
else:
    #se trabalhar horas extra, estas são pagas a dobrar
    extra = horas - 40
    print((salario_h*(horas-extra))+(salario_h*2*extra), " €.")

'''

# -----------------------------------------------------

''' Exercicio 8

while True:
    segs = float(input("Escreva um número de segundos (negativo para terminar): "))
    if(segs < 0):
        break
    print("Esse número em dias é ", segs/(60*60*24))
'''

#-----------------------------------------------------

''' Exercicio 9

juntos = ""

while True:
    num = input("Introduza um digito (negativo para terminar): ")
    if(num[0] == '-'):
        break
    elif(len(num) > 1):
        print("Introduziu mais do que um digito. ")
        continue
    else:
        juntos += num

print("Os digitos que introduziu formam o número ", juntos)

'''
#---------------------------------------------------

''' Exercicio 10
x = int(input("Introduza um número inteiro positivo: "))

if x <=0:
    print("O seu número não é inteiro positivo.")
else:
    x = str(x) #passa para string para convertemos cada digito individualmente
    i = 0
    impares = ''
    while i < len(x):
        if(int(x[i])%2 != 0): #se for impar
            impares += x[i]
        i += 1
    print("Resultado: ", impares)

'''

#--------------------------------------------------

#''' Exercicio 11

# Matemáticamente
x = int(input("Escreva um número inteiro positivo: "))
if(x <= 0):
    print("O número que introduziu não é inteiro positivo. ")
else: 
    num = 0
    while x > 0:
        num = (num*10)+(x%10)
        x = x // 10
    print("Número inverso: ", num)

# Com Strings

#'''

#