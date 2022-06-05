from random import randint
m = [0] * 5
for i in range(5):
    m[i] = [0] * 5
    for j in range(5):
        m[i][j] = randint(1, 20)
        print(f'{m[i][j]:02}', end=' ')
    print()
for i in range(5):
    for j in range(5):
        if i == j:
            print(f'{m[i][j]:02}', end=' ')
        else:
            print(f'{0:02}', end=' ')
    print()