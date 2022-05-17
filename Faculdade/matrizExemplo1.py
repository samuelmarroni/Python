from random import randint

M = [0] * 5
for i in range(5):
    M[i] = [0] * 5
    for j in range(5):
        M[i][j] = randint(1, 20)
        print(f'{M[i][j]:2}', end=' ')
    print()

print('Diagonal Principal')
for i in range(5):
    print(M[i][j])
