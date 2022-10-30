from functools import reduce


print(list(filter(lambda x: x%2 == 0, [1,2,3,4,5,6,7,8,9])))
print([x for x in [1,2,3,4,5,6,7,8,9] if (x%2 == 0)])

def acumulador(f, lst):
    if(len(lst) == 0):
        raise ValueError("ACUMULADOR: list vazia")
    res = lst[0]
    for e in lst[1:]:
        res = f(res,e)
    return res

print(acumulador(lambda x,y: x+y, [1,2,3,4,5]))
print(reduce(lambda x,y: x+y, [1,2,3,4,5]))
