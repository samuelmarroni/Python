#Elabore um algoritmo para gerar a seguinte matriz 5x5:
from random import randint
M = [0] * 5
for i in range(5):
    M[i] = [0] * 5
    for j in range(5):
        if i==j or i+j==4:
            M[i][j]= 1

print("Matriz resposta:")
for i in range(5):
    print(*M[i])
