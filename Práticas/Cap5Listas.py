from re import X



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

#'''Exercicio 4

def elemento_matriz(mtrz,row,col):
    if(row >= len(mtrz)):
        raise ValueError("elemento matriz: indice invalido, linha", row)
    if(col >= len(mtrz[row])):
        raise ValueError("elemento matriz: indice invalido, coluna", col)
    return mtrz[row][col]

m = [[1,2,3],[4,5,6]]
#print(elemento_matriz(m,0,0))
#print(elemento_matriz(m,0,3))


#------------------------------------------------------------------

#Exercicio 5

def repr_matriz(mtr1):
    for i in range(len(mtr1)):
        for j in range(len(mtr1[i])):
            mtr1[i][j] = str(mtr1[i][j])
        print(" ".join(mtr1[i]))

#repr_matriz(m)


#------------------------------------------------------------------

#'''Exercicio 6

def soma_mat(mtr1,mtr2):
    for i in range(len(mtr1)):
        for j in range(len(mtr1[i])):
            mtr1[i][j] = str(mtr1[i][j]+mtr2[i][j])
    return mtr1

m1 = [[1,2,3],[4,5,6],[7,8,9]]
m2 = [[1,2,3],[4,5,6],[7,8,9]]
repr_matriz(soma_mat(m1,m2))

#'''

#-----------------------------------------------------------------

