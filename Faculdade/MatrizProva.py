from random import randint
from secrets import choice
prova = ['A', 'B', 'C', 'D']
A = [0] * 5
for i in range(5):
    A[i] = [0] * 10
    for j in range(10):
        n = randint(0, 3)
        A[i][j] = prova[n]

S = [0] * 10
for i in range(10):
    S[i] = choice(prova)
print(f'O gabarito da prova é {S}')
print()

nota = 0
for i in range(5):
    for j in range(10):
        if A[i][j] == S[j]:
            nota += 1
    print(f'O aluno {i+1} tirou {nota}')
    nota = 0
    print()
