from random import randint
L = []
for i in range(10):
    L.append(randint(1, 50))
print(L)
while True:
    op = int(input('1. Ordem gerada\n2. Ordem inversa\n3. Sair'))
    if op == 1:
        for elem in L:
            print(f'{elem:02}', end=' ')
        print()

        # print(*L)
    elif op == 2:
        for i in range(9,-1, -1):
            print(f'{L[i]:02}', end=' ')
        print()

        # print(L[::-1])
    elif op == 3:
        break
    else:
        print('Opção inválida!!')
