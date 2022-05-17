from random import randint
L = []
while len(L) != 10:
    num = randint(1, 50)
    if num not in L:
        L.append(num)
print(L)
