from random import randint

I = []
L = []
while len(L) < 5:
    n1 = randint(1, 10)
    if n1 not in L:
        L.append(n1)
print(L)
I.append(L)

T = []
while len(T) < 5:
    n2 = randint(1, 10)
    if n2 not in T:
        T.append(n2)
print(T)


for n in range(5):
    if T[n] not in L:
        I.append(T[n])
print(I)
