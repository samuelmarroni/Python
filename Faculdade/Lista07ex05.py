#Faça  um  programa  em Python que  gere  uma  matriz  10  x  10  de  inteiros entre  1  e  50, imprima a matriz e o menor elemento de cada coluna.
from random import randint
M = [0] * 10
for i in range(10):
    M[i] = [0] * 10
    menor = 50
    for j in range(10):
        M[i][j] = randint(1, 50)
        print(f'{M[i][j]:02}', end=' ')
    print()
