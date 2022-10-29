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

'''
def soma_n_vezes(a,b,n):
    if(n == 0):
        return b
    else:
        return a + soma_n_vezes(a,b,n-1)

print(soma_n_vezes(3,2,5))
'''

# Exercicio 5 -----------------------------------

'''
def soma_els_atomicos(tp):
    if(type(tp) != tuple):
        return tp
    elif(len(tp) == 0):
        return 0
    #elif(len(tp) == 1):
    #    return soma_els_atomicos(tp[0])
    # This condition is not need since a single element tuple isn't really single it has a second element ()
    else:
        return soma_els_atomicos(tp[0]) + soma_els_atomicos(tp[1:])

print(soma_els_atomicos((3, ((((((6, (7, ))), ), ), ), ), 2, 1)))
print(soma_els_atomicos(((((),),),)))
'''

# Exercicio 6 -----------------------------------------

'''
def inverte(lista):
    if(len(lista) == 1):
        return [lista[0]]
    return [lista[-1]] + inverte(lista[:len(lista)-1])

print(inverte([3,4,7,9]))
print(inverte([1,2,3,4,5,6,7,8,9,10]))
'''

# Exercicio 7  --------------------------------------------

'''
def pertence(lista,ele):
    if(len(lista) == 1):
        return (ele == lista[0])
    elif(len(lista) == 0):
        return False
    else:
        return pertence(lista[1:],ele)

print(pertence([1,2,3,4,5],5))
print(pertence([1,2,3,4],5))
print(pertence([],5))
'''

# Exercicio 8 -----------------------------------------------

'''
def subtrai(lista1,lista2):
    if(len(lista2) == 0 or len(lista1) == 0):
        return lista1
    elif(lista2[0] in lista1 and lista1.count(lista2[0]) > 1): #more than 1 occurrence of lista2[0] in lista1
        lista1.remove(lista2[0])
    elif(lista2[0] in lista1 and lista1.count(lista2[0]) == 1): #only 1 occurrence of lista2[0] in lista1
        lista1.remove(lista2[0])
        lista2.pop(0)
    else: # no occurences of lista2[0] in lista1
        lista2.pop(0)
    
    return subtrai(lista1,lista2)

print(subtrai([2,2,3,3,4,5],[2,3]))
print(subtrai([2, 3, 4, 5], [6, 7]))
print(subtrai([],[2,4]))
print(subtrai([2],[2,4]))
'''

# Exercicio 9 ---------------------------------------------------

'''
def parte(lista,num):
    def aux(lista,num,isBigger):
        def compare(isBigger,num1,num2):
            if(isBigger == True):
                return (num1 >= num2)
            else:
                return (num1 < num2)

        if(len(lista) == 1):
            return ([lista[0]] if compare(isBigger,lista[0],num) else [])
        else:
            return ([lista[0]] if compare(isBigger,lista[0],num) else []) + aux(lista[1:],num,isBigger)
    return [aux(lista,num,False),aux(lista,num,True)]

print(parte([3,5,1,4,5,8,9],4))
print(parte([1,2],1))
print(parte([1,2],3))
'''

# Exercicio 10 ----------------------------------------------------

'''
def maior(lista):
    def aux(ele,maior):
        return (ele if ele > maior else maior)
    
    if(len(lista) == 1):
        return lista[0]
    elif(len(lista) == 2):
        return aux(lista[1],lista[0])
    else:
        return aux(maior(lista[:2]),maior(lista[2:]))

print(maior([1,2,7,8,6,4,2.5]))
'''