''' # Maior que 2
num = eval(input("Introduz um número: "))
num2 = eval(input("Introduz um  outro número: "))

if num > num2:
    print("O primeiro número é maior.")
elif num2 > num:
    print("O segundo número é maior. ")
else:
    print("Os dois números são iguais")

'''

''' # Par, ímpar, negativo e positivo
num = eval(input("Introduza um número: "))

if num % 2 == 0:
    print("O número é par ", end='') 
else:
    print("O número é ímpar ", end='')

if num > 0 :
    print("e positivo. ")
elif num < 0:
    print(" é negativo. ")
else:
    print(" é igual a 0. ")
'''

''' # Soma de números
soma = 0
x = eval(input("Introduza um número (negativo termina): "))

while x > 0:
    soma += x
    x = eval(input("Introduza um número (negativo termina): "))

print("A soma dos números é ", soma)
'''

''' # Soma de números (pares e ímpares)
soma = 0
soma_pares = 0
soma_impares = 0
x = 0

while True:
    soma += X
    x = eval(input("Introduza um número (negativo termina): "))

    if x < 0:
        break
    elif x % 2 == 0:
        soma_pares += x
    else:
        soma_impares += x
    
print("A soma dos numeros é ", soma, "\nA soma dos pares é ", soma_pares, "\nA soma dos impares é ", soma_impares)    
'''

''' Soma de digitos de um numero

soma = 0
num = int(input("Introduza um número: "))

while num != 0:
    dig = num % 10
    soma += dig #se fizessemos 10*soma aqui os números trocavam de ordem.
    num = num // 10

print("Soma:", soma)

'''

# ''' Cálculo factores primos de inteiro

x = int(input("Introduza um inteiro: "))
divisor = 2

print("Divisores primos: ", end='')

while x != 1:
    if x%divisor == 0: #é divisor
        x = x//divisor
        print(divisor, ' ', end='')
    else:
        divisor += 1



# '''

#

