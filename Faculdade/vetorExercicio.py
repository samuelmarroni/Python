from random import randint

while(True):
    x = int(input('Exercício: '))

    if x <= 0 or x > 10:
        break

    elif x == 1:

        a = []
        par = 0
        impar = 0
        for i in range(10):
            a.append(randint(1, 50))

        for i in range(10):
            if a[i] % 2 == 0:
                par += 1
            if a[i] % 2 == 1:
                impar += 1

        print(*a)
        print('Nº Par(es):', par)
        print('Nº Impar(es):', impar)
        print('<>'*20)

    elif x == 2:

        a = []
        soma = 0
        for i in range(20):
            a.append(randint(1, 50))

        for i in range(20):
            soma += a[i]

        print(*a)
        print('Média:', soma/20)
        print('<>' * 20)

    elif x == 3:

        a = []
        b = []
        for i in range(20):
            a.append(randint(1, 50))

        for i in range(20):
            if a[i] % 5 == 0:
                b.append(a[i])

        print(*a)
        print('Múltiplos de 5:', *b)
        print('<>' * 20)

    elif x == 4:
        n = int(input('Digite o número desejado:'))
        a = []
        b = []
        for i in range(20):
            a.append(randint(1, 50))

        for i in range(20):
            if a[i] % n == 0:
                b.append(a[i])

        print(*a)
        print(f'Múltiplos de {n}:', *b)
        print('<>' * 20)

    elif x == 5:
        a = []
        for i in range(10):
            a.append(randint(1, 50))

        print(*a)
        print(a[::-1])
        a.reverse()
        print(*a)
        print('<>' * 20)

    elif x == 6:
        n = int(input('Digite o número desejado:'))
        a = []
        b = []
        for i in range(10):
            a.append(randint(1, 50))
        for i in range(10):
            b.append(a[i] * n)

        print(*a)
        print(*b)
        print('<>' * 20)

    elif x == 7:
        a = []
        for i in range(10):
            a.append(randint(1, 50))

        print(*a)

        for i in range(10):
            for j in range(10):
                if a[j] > a[i]:
                    a[j], a[i] = a[i], a[j]

        print(*a)
        print('<>' * 20)

    elif x == 8:
        a = []
        b = []
        c = []
        for i in range(20):
            a.append(randint(1, 50))

        for i in range(20):
            if a[i] % 2 == 0:
                b.append(a[i])
            if a[i] % 2 == 1:
                c.append(a[i])

        print(*a)
        print('Nº Par(es):', *b)
        print('Nº Impar(es):', *c)
        print('<>'*20)

    elif x == 9:
        n = int(input('Digite o número desejado:'))
        a = []

        for i in range(10):
            a.append(randint(1, 50))

        for i in range(10):
            if a[i] == n:
                break

        if i < 10:
            print(f'O {n} está na lista')
        else:
            print(f'O {n} não está na lista')

    elif x == 10:
        a = []
        while len(a) != 10:
            num = randint(1, 20)
            if num not in a :
                a.append(num)

        print(a)
