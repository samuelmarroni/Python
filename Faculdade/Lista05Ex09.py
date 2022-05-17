from random import randint

L = []

for i in range(10):
    L.append(randint(1, 50))
print(L)

num = int(input('Informe o número que deseja encontrar: '))

if num in L:
    print(f'O {num} está na lista.')
else:
    print(f'O {num} não está na lista.')
