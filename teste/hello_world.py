def mover(n, ori, dest, aux):
    def movimentar(ori, dest):
        print(ori, '-->', dest)
    if n == 1:
        movimentar(ori, dest)
    else:
        mover(n-1, ori, aux, dest)
        movimentar(ori, dest)
        mover(n-1, aux, dest, ori)
         
mover(3, 'E', 'D', 'C')