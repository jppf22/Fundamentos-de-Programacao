# Exercicio 1 ----------------------------------------------------
'''
def apenas_digitos_impares(n):
    if(n == 0):
        return 0
    elif((n % 10) % 2 != 0):
        return (n%10) + apenas_digitos_impares(n // 10)*10
    else:
        return apenas_digitos_impares(n // 10)

#print(apenas_digitos_impares(123456789))

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

'''
# Exercicio 2 -----------------------------------------
'''
def junta_ordenadas(lst1,lst2):
    if(len(lst1) == 0 or len(lst2)==0):
        return lst1+lst2
    elif(lst1[0] > lst2[0]):
        return [lst2[0]] + junta_ordenadas(lst1,lst2[1:])
    else:
        return [lst1[0]] + junta_ordenadas(lst1[1:],lst2) 

#print(junta_ordenadas([2,5,90],[3,5,6,12]))
'''

# Exercicio 3 --------------------------------------------


def conta_sublistas(lista):
    if(type(lista) != list or len(lista) == 0):
        return 0
    elif(len(lista) == 1):
        return 1 + conta_sublistas(lista[0])
    elif(len(lista) == 2):
        return conta_sublistas(lista[0]) + conta_sublistas(lista[1])
    else:
        return conta_sublistas(lista[0]) + conta_sublistas(lista[1:])

    '''
    We use a condition for len() == 2 because if we sliced with list[1:] instead of checking the list in position 1 we would be
    creating a list with the list on position 1

    Ex:
    list = [0,[1]]
    we know list[1] = [1]
    However:

    print(list[1:]) = [[1]]
    print(list[1]) = [1]

    The difference would cause len() == 1 to add 2 ocurrences of sublist (the main list and sublist itself) instead of only 1
    '''

    
#print(conta_sublistas([[1],2,[3]]))

# Exercicio 4 ---------------------------------------------------


