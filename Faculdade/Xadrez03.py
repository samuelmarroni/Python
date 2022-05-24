#Elabore um algoritmo que em uma matriz 8x8, leia as coordenadas iniciais 
# de um Cavalo do Xadrez e mostre os possíveis movimentos. 
# Para isso, crie a matriz toda zerada e coloque o valor 1 nos lugares possíveis de seus movimentos.
A = [0]*8
for i in range(8):
    A[i] = [0] * 8

L = int(input("Digite a linha onde o cavalo está:"))
C = int(input("Digite a coluna onde o cavalo está:"))

for i in range(8):
    for j in range(8):
        if (((i==L-2) or (i==L+2)) and ((j==C-1) or (j==C+1)) or ((i==L-1) or (i==L+1)) and ((j==C-2) or (j==C+2))):
            A[i][j] = 1
        print(f'{A[i][j]:2}', end=' ')
    print()
    