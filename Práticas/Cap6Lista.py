# Exercicio 1 ----------------------------------------------------

def apenas_digitos_impares(n):
    if(n == 0):
        return 0
    elif((n % 10) % 2 != 0):
        return (n%10) + apenas_digitos_impares(n // 10)*10
    else:
        return apenas_digitos_impares(n // 10)

print(apenas_digitos_impares(123456789))

def apenas_digitos_imparesCAUDA(n):

    def aux(n, res):
        if(n == 0):
            return n
        elif((n%10)%2 != 0):
            return ()
    if(n == 0):
        return 0
    elif((n % 10) % 2 != 0):
        return (n%10) + apenas_digitos_impares(n // 10)*10
    else:
        return apenas_digitos_impares(n // 10)