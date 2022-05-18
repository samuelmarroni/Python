#Elabore um algoritmo que em uma matriz 8x8, leia as coordenadas iniciais de uma Torre do Xadrez e  mostre os possíveis movimentos. Para isso, crie a matriz toda zerada e coloque o valor 1 nos lugares possíveis de seus movimentos.
A = [0]*8
for i in range(8):
    A[i] = [0] * 8

L = int(input("Digite a linha onde a torre está:"))
L -= 1
C = int(input("Digite a coluna onde a torre está:"))
C -= 1

for i in range(8):
    for j in range(8):
        if i == L or j == C:
            A[i][j] = 1
        print(f'{A[i][j]:2}', end=' ')
    print()
