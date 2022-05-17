from random import randint

L = []
while len(L) != 5:
    n1 = randint(1, 10)
    if n1 not in L:
        L.append(n1)
L.sort()
print(*L)

T = []
while len(T) != 5:
    n2 = randint(1, 10)
    if n2 not in T:
        T.append(n2)
T.sort()
print(*T)

I = []
for n in L:
    if n in T:
        I.append(n)
print(*I)
