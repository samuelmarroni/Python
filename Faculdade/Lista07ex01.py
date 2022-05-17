# Faça  um  programa  em Python que  leia  uma  matriz  2  x  3  de  inteiros,  imprima  a  matriz  e  a soma de todos os elementos.
from random import randint
from termcolor import colored
M = [0] * 2
soma = 0
for i in range(2):
    M[i] = [0] * 3
    for j in range(3):
        M[i][j] = randint(1, 20)
        print(colored(f'{M[i][j]:02}', 'grey', 'on_magenta', attrs=['underline']), end=' ')
        soma += M[i][j]
    print()
print(f'Soma de todos os elementos da matriz é igual a {soma}')
