

s = int(input())

n =('h','m','s')

for i in range(len(n)):
    print(n[i], ':', s//60, end=' ')
    s = s % 60

