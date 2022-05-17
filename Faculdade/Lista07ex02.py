# Faça um programa em Python que gere uma matriz 10 x 10 de inteiros aleatórios entre 1 e 50, imprima a matriz e a média de todos os elementos.

from random import randint
from termcolor import colored
media = 0
M = [0] * 10
soma = 0
for i in range(10):
    M[i] = [0] * 10
    for j in range(10):
        M[i][j] = randint(1, 50)
        print(colored(f'{M[i][j]:02}'), end=' ')
        soma += M[i][j]
    print()
tm = len(M) * len(M[i])
media = soma / tm
print(f'A média de todos os elementos da matriz é igual a {media}')
print(f'Tamanho da matriz {tm}')
