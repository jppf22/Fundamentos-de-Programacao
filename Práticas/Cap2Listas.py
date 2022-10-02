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
num_values = float(input("Quantos números tem a sua sequência? Resposta: "))
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

#Forma não suposta ainda
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
'''
#Forma suposta

num_final = 0

while True:
    x = int(input("Escreva um dígito: "))
    if(x == -1):
        break
    else:
        num_final = num_final*10 + x

print("O número final é ", num_final)
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

''' Exercicio 11

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

'''

#-------------------------------------------------

''' Exercicio 12

 #Solução pessoal
def fatorial(n):
    fat = 1
    while n != 1:
        fat *= n
        n -= 1
    return fat


x = int(input("Introduza um valor x: "))
n = int(input("Introduza um valor n: "))
i=1
soma = 1

while i <= n:
    soma += ((x**i)/fatorial(i))
    i += 1

print("O valor da soma é: ", soma)
 

#Solução suposta
x = int(input("Introduza um valor x: "))
n = int(input("Introduza um valor n: "))
i=1
soma = 1
termo_anterior = 1

while i<= n:
    termo_anterior = termo_anterior*(x/i) #o proximo termo anterior será o termo atual 
    soma += termo_anterior
    i+=1

print("O valor da soma é: ", soma)

'''

# -----------------------------------------------

''' #Exercicio 13

num = int(input("Escreva um número para eu escrever a tabuada da multiplicação\n\
Num -> "))

i=1
while i <= 10:
    print(num, " x ",i, " = ", num*i)
    i+=1
'''

# -----------------------------------------------

''' Exercicio 14

x = int(input("Introduza um número inteiro: "))
soma = 0

while x != 0:
    soma += x%10
    x = x // 10

print("A soma dos seus dígitos é ", soma)


'''
#-------------------------------------------------

''' Exercicio 15

num = 0
dig = int(input("Introduza um dígito: "))

while dig > -1:
    num = num*10 + dig
    dig = int(input("Introduza um dígito: "))

print("O número inteiro formado por esses dígitos é: ", num)
'''

#---------------------------------------------------

''' Exercicio 16
metade1 = int(input("Escreva um número\n-> "))
res = metade1

while(metade1 > 0):
    digito = metade1%10
    res = res*10 + digito
    metade1 = metade1 // 10

print(res)

'''

#----------------------------------------------------

''' Exercicio 17 (Nota: Não era claro no enunciado se o conjunto de números 
inteiros era suposto ser separado, assim, ou um inteiro muito grande em que cada digito era um nota)


nota = 0
num_positivas = 0

alunos = int(input("Quantos alunos tem a turma?\nResposta: "))
i=0

while i<alunos:
    nota = int(input("Introduza um nota: "))
    if nota >= 10:
        num_positivas+=1
    i+=1

print("Dos ", alunos, " alunos ", num_positivas," tiveram nota positiva\n\
    Percentagem de notas positivas: ", (num_positivas/alunos)*100)

'''
#------------------------------------------------------------------------------------

''' Exercicio 18

num = int(input("Escreva um número inteiro: "))
zeros = 0

prev_dig = num % 10
num = num // 10

while num != 0:
    dig = num % 10
    if prev_dig == 0 and dig == 0:
        zeros += 1
    prev_dig = dig
    num = num // 10

print("O numero tem ", zeros, " zeros seguidos")

'''
#------------------------------------------------------------------------------------------------

''' Exercicio 19 -- Para se fazer sem array com nomes teria que fzr cada iteração sem usar while

euros = float(input("Introduza uma quantia de dinheiro: "))
euros = int(round(euros * 100,2))


#A passagem é sempre 50,20,10,5,2,1 em euros e centimos
quant50 = 5000
quant20 = 2000
quant10 = 1000

nomes50=["Notas de 50e","Notas de 5e", "Moedas de 50c", "Moedas de 5c"]
nomes20=["Notas de 20e","Moedas de 2e","Moedas de 20c", "Moedas de 2c"]
nomes10=["Notas de 10e","Moedas de 1e","Moedas de 10c", "Moedas de 1c"]
i = 0


print("A sua quantia equivale a ")
while euros != 0: #funciona bem
    
    if((euros // quant50) != 0):
        print(euros//quant50, nomes50[i])
    euros = euros % quant50
    quant50 = quant50//10

    if((euros // quant20) != 0):
        print(euros//quant20, nomes20[i])
    euros = euros % quant20
    quant20 = quant20//10

    if((euros // quant10) != 0):
        print(euros//quant10, nomes10[i])
    euros = euros % quant10
    quant10 = quant10 // 10

    i+=1


'''
#-------------------------------------------------------------------------------------

#'''  Exercicio 20

i=1
j = 0
while i<=9:
    j+=i
    print(j, " x 8 + ",i," = ", j*8+i)
    j *= 10
    i+=1


#'''