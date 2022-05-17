#Faça  um  programa  em Python que  gere  uma  matriz  10  x  10  de  inteirosentre  1  e  50, imprima a matriz e o menor elemento de cada linha
from random import randint
M = [0] * 10
for i in range(10):
    M[i] = [0] * 10
    for j in range(10):
        M[i][j] = randint(1, 50)
        print(f'{M[i][j]:02}', end=' ')
    print()
print('='*30)
for i in range(10):
    menor = M[0][i]
    for j in range(10):
        if M[j][i] < menor:
            menor = M[j][i]
    print(f'{M[i][j]:02}', end=' ')
