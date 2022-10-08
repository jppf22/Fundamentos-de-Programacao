
''' Exercicio 1

soma = 0
for i in range(20,0,-2):
    soma += 1
print("Soma = ", soma)

'''
''' Exercicio 2,3,4,5

# Exercicio 2

def explode(arg):
    if(type(arg) != int):
        raise ValueError("explode: argumento não inteiro")
    elif(arg <= 0):
        raise ValueError("explode: argumento não inteiro positivo")
    else:
        tuple_res = ()
        while arg > 0:
            dig = arg % 10
            tuple_res = (dig,)+tuple_res #pois os digs vão ser apresentados do final para o inicio
            arg = arg // 10
    return tuple_res

#print(explode(34500))
#print(explode(3.5))
#print(explode(-1))



# Exercicio 3
def implode(arg):
    if(type(arg)!= tuple):
        raise ValueError("implode: argumento não tuplo") 
    num = 0
    for i in arg:
        if (type(i) != int):
            raise ValueError("implode: elemento não inteiro")
        num = num * 10 + i
    return num

def implode_while(arg):
    num = 0
    i = 0
    while i < len(arg):
        if (type(i) != int):
            raise ValueError("implode: elemento não inteiro")
        num = num * 10 + arg[i]
        i+=1

    return num

#print(implode((3,4,0,0,4)))
#print(implode_while((3,4,0,0,4)))
#print(implode(34004))
#print(implode((0,'a',1)))


# Exercicio 4

def filtra_pares(arg):
    if(type(arg)!=tuple):
        raise ValueError("filtra_pares: argumento não tuplo")
    res = ()
    for i in arg:
        if(type(i)!=int or i < 0):
            raise ValueError("filtra_pares: elemento não inteiro positivo ou zero")
        if(i%2 == 0):
            res = res + (i,)
    return res

#print(filtra_pares((2,5,6,7,9,1,8,8)))
#print(filtra_pares((-1,2)))
#print(filtra_pares(('a','b')))

# Exercicio 5

def algarismos_pares(arg):
    return implode((filtra_pares(explode(arg))))
print(algarismos_pares(6643399766641))    

'''

''' Exercicio 6

def num_para_seq_cod(num):
    if(type(num) != int):
        raise ValueError("num_para_seq_cod: argumento não número inteiro")
    if(num <= 0):
        raise ValueError("num_para_seq_cod: número não inteiro positivo")
    
    res = ()
    while num > 0:
        dig = num % 10
        if(dig % 2 == 0):
            if( dig != 8):
                dig = dig + 2
            else:
                dig = 0
        else:
            if( dig != 1):
                dig = dig - 2
            else:
                dig = 9
        num //= 10
        res = (dig,) + res
    return res

print(num_para_seq_cod(1234567890))
'''

''' Exercicio 7

def amigas(arg1,arg2):
    if(len(arg1) != len(arg2)):
        return False
    else:
        occur_dif = 0
        for i in range(len(arg1)):
            if(arg1[i] != arg2[i]):
                occur_dif += 1
        return ((occur_dif/len(arg1)*100) < 10)

print(amigas("amigas","amigas"))
print(amigas("abcdefghijk","abcdefghijl"))
print(amigas("amigas","asigos"))

'''

''' Exercicio 8


def junta_ordenados(t1,t2):
    res = ()
    i1,i2 = 0,0
    while i1 < len(t1) or i2 < len(t2):
        if(i1 == len(t1)): ##já processamos um completo
            res = res + (t2[i2],)
            i2+=1
        if(i2 == len(t2)):
            res = res + (t1[i1],)
            i1+=1
        elif(t1[i1] < t2[i2]):
            res = res + (t1[i1],)
            i1+=1
        elif(t1[i1] >= t2[i2]):
            res = res + (t2[i2],)
            i2+=1
    return res

print(junta_ordenados((2,34,200,210),(1,23)))
'''

''' Exercicio 9


def reconhece(str):
    nums = ('1','2','3','4')
    letras = ('A','B','C','D')
    
    if(str[0] not in letras):
        return False

    pos = 0
    for i in range(1,len(str)):
        if(str[i] in nums):
            pos = i
            break
        elif(str[i] not in letras):
            return False
        
    if pos == 0: #ou seja, se não tiver mudado de letras para numeros
        return False
    
    for i in range(pos,len(str)):
        if(str[i] not in nums):
            return False

    return True

print(reconhece('A1'))
print(reconhece('ABBBBCDDDD23311')) 
print(reconhece('ABC12C'))   

'''
#-------------------------------------------

''' Exercicio 10
# -- a)

def codifica(str):
    pares = ""
    impares = ""
    for i in range(0,len(str)):
        if i % 2 == 0:
            pares = pares + str[i]
        else:
            impares = impares + str[i]
    return (pares + impares)

print(codifica('abcde'))
print(codifica('abcdefghijklmnop'))

# -- b)

def descodifica(str):
    len_pares = 0
    len_impares = 0
    if(len(str) % 2 == 0):
        len_pares = len(str) // 2
        len_impares = len_pares
    else:
        len_impares = len(str) // 2
        len_pares = len(str)-len_impares
        
    pares = str[0:len_pares]
    impares = str[len_pares:len(str)]
    res= ""

    i_pares = 0
    i_impares = 0
    for i in range(0,len(str)):
        if(i%2 == 0):
            if(i_pares < len_pares):
                res = res + pares[i_pares]
                i_pares += 1
        else:
            if(i_impares < len_impares):
                res = res + impares[i_impares]
                i_impares += 1
    
    return res

print(descodifica('acebd'))
print(descodifica('acegikmobdfhjlnp'))
        
'''

#---------------------------------------------- Exercicios do Livro -------------------------------------------------

''' Exercicio 1

def duplica(tp):
    res = ()
    for i in tp:
        res += (i,i)
    return res

print(duplica((1,2,3)))
print(duplica(('a',3,'2',2.0)))

'''

#''' Exercicio 2



#'''