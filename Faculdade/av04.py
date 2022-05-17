num = int(input('Digite o número:'))
valorMin = (10**(num-1))
valorMax = (10**num)
listSushi = []
for n in range(valorMin, valorMax):
    x = n
    pont = 0
    while x != 0 and x != 1 :
        p = 2
        for i in range(2, (x // 2) + 1):
            if (x % i) == 0:
                p += 1
                break
        if p == 2:
            pont += 1
        x //= 10
    if pont == num:
        listSushi.append(n)

print(listSushi)

