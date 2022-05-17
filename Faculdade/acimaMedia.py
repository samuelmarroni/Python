C = int(input())
for i in range(C):
    L = input().split()
    soma = 0
    for i in range(1, len(L)):
        L[i] = int(L[i])
        soma += L[i]
    N = int(L[0])
    media = soma/N
    acima = 0
    for i in range(1,len(L)):
        if L[i] > media:
            acima += 1
    per = (acima / N) * 100
    print(f'{per:.3f}%')
