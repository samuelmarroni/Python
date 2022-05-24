#Elabore um algoritmo que em uma matriz 8x8, leia as coordenadas iniciais de uma Rainha do Xadrez
#  e mostre os possíveis movimentos. Para isso, crie a matriz toda zerada e coloque o valor 1 nos lugares
#  possíveis de seus movimentos.
A = [0]*8
for i in range(8):
    A[i] = [0] * 8

L = int(input("Digite a linha onde a rainha está:"))
C = int(input("Digite a coluna onde a rainha está:"))

for i in range(8):
    for j in range(8):
        if ((i==L) or (j==C) or (i+j==L+C) or (i-j==L-C)):
            A[i][j] = 1
        print(f'{A[i][j]:2}', end=' ')
    print()
