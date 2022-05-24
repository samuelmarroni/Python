from random import randint
n = int(input("Informe um número maior que dois:"))
S = 0
linha = 0
coluna = 0
diagonal = 0
A = [0] * n
for i in range(n):
    A[i] = [0] * n
    for j in range(n):
        A[i][j] = int(input())
        linha += A[i][j]
        coluna += A[j][i]
        if i == j:
            diagonal += A[i][j]
    if (linha == (n + n**3) / 2) and (coluna == (n + n**3) / 2) and (diagonal == (n + n**3) / 2):
        print("É um quadrado mágico")
