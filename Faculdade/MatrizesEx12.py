# Elabore um algoritmo que leia uma matriz 5x5 e verifique se ela é ou não uma matriz identidade.  Uma matriz é identidade se todos os elementos da diagonal principal são 1s e os demais 0s.
A = [0] * 5
for i in range(5):
    A[i] = [0] * 5
    for j in range(5):
        A[i][j] = int(input())

id = True
for i in range(5):
    for j in range(5):
        if ((i == j and A[i][j] != 1) or (i != j and A[i][j] != 0)):
            id = False
            break

if id:
    print("Matriz é identidade!")
else:
    print("Matriz não é identidade!")
