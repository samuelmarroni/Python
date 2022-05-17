a = []
while True:
    n = len(a)
    valor = int(input('Digite o Número:'))
    if valor == 0:
        break
    elif n == 0 or a[n-1] < valor:
        a.append(valor)
    else:
        cont = 0
        while a[cont] < valor:
            cont += 1
        a.insert(cont, valor)

    print(a)
    print('='*20)

print(a)
