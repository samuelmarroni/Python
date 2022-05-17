from random import randint
L = []
for i in range(10):
    L.append((randint(1, 10)))
print(L)
# BubbleSort
for i in range(10):
    for j in range(i+1, 10):
        if L[i] > L[j]:
            L[i], L[j] = L[j], L[i]
# Outra Opção
L.sort()
print(L)
