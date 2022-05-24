from random import randint
inicio = 1
final = 15
A = [0] * 5
for i in range(5):
    j = 0
    A[i] = [0] * 5
    while j < 5:
        num = randint(inicio, final)
        if (num not in A[i]):
            A[i][j] = num
            j += 1
    inicio += 15
    final += 15

for i in range(5):
    for j in range(5):
        print(f'{A[j][i]:2}', end=' ')
    print()
