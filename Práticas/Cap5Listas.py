
'''Exericio 1
def lista_codigos(string):
    return [ord(string[x]) for x in range(0,len(string))]

print(lista_codigos("bom dia"))

'''

#-------------------------------------------------------------------------------------

''' Exercicio 2

def remove_multiplos(lst,num):
    res = []
    for x in lst:
        if x%num != 0:
            res.append(x)
    return res

print(remove_multiplos([2,3,5,9,12,33,34,45],3))
'''

#----------------------------------------------------------------------

''' Exercicio 3

def soma_cumulativa(lst1):
    for i in range(1,len(lst1)):
        lst1[i] = lst1[i]+lst1[i-1]
    return lst1

print(soma_cumulativa([1,2,3,4,5]))
'''

#--------------------------------------------------------------------

'''Exercicio 4

def elemento_matriz(mtrz,row,col):
    if(row >= len(mtrz)):
        raise ValueError("elemento matriz: indice invalido, linha", row)
    if(col >= len(mtrz[row])):
        raise ValueError("elemento matriz: indice invalido, coluna", col)
    return mtrz[row][col]

m = [[1,2,3],[4,5,6]]
#print(elemento_matriz(m,0,0))
#print(elemento_matriz(m,0,3))

'''
#------------------------------------------------------------------

'''Exercicio 5

def repr_matriz(mtr1):
    for i in range(len(mtr1)):
        for j in range(len(mtr1[i])):
            mtr1[i][j] = str(mtr1[i][j])
        print("\t".join(mtr1[i]))

#repr_matriz(m)

'''
#------------------------------------------------------------------

'''Exercicio 6

def soma_mat(mtr1,mtr2):
    for i in range(len(mtr1)):
        for j in range(len(mtr1[i])):
            mtr1[i][j] = str(mtr1[i][j]+mtr2[i][j])
    return mtr1

m1 = [[1,2,3],[4,5,6],[7,8,9]]
m2 = [[1,2,3],[4,5,6],[7,8,9]]
#repr_matriz(soma_mat(m1,m2))

'''

#-----------------------------------------------------------------

''' Exercicio 7
def multiplica_mat(mtr1,mtr2):
    if(len(mtr1[0]) != len(mtr2)):
        raise ValueError("multiplica_mat: o número de colunas de 1 precisa de ser igual ao número de linhas de 2")

    res = []
    i = 0
    while i < len(mtr1):
        linha_temp = []
        j = 0
        while j < len(mtr2[0]):
            n=0
            sum = 0
            while n < len(mtr1):
                sum += (mtr1[i][n]*mtr2[n][j])
                n+=1
            linha_temp.append(sum)
            j+=1
        res.append(linha_temp)
        i+=1
    return res

repr_matriz(multiplica_mat(m1,m2))

#Nota: esta programa só funciona para matrizes com colunas e linhas iguais
'''
#---------------------------------------------------------------

# Exericio 8 - Sequencia de Racamán

def seq_racaman(n):
    res = []
    i=0
    while len(res) < n:
        if(i==0):
            res.append(0)
        elif(res[i-1] > i and (res[i-1]-i) not in res):
            res.append(res[i-1]-i)
        else:
            res.append(res[i-1]+i) 
        i+=1
    return res

print(seq_racaman(15))

#------------------------------------------------------------

# Exercicio 9 

def numero_occ_lista(lista,num):
    occ = 0
    currlist = lista
    for i in range(len(lista)):
        if(type(currlist[i]) == list):
            currlist = currlist[i]
        elif(type(currlist[i]) == int):
            occ += (currlist[i] == num)
        elif num in currlist:
            occ += currlist.count(num)
        else:
            currlist = lista
            i+=1
    return occ

print(numero_occ_lista([1,2,3,4,3],3))
print(numero_occ_lista([1, [[[1]], 2], [[[2]]], 2], 2))
        
            
