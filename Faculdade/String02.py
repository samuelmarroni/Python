from calendar import c


p = input("Informe uma palavra:")
l = input("Informe uma letra:")

c = 0
for i in p:
    if i == l:
        c += 1

print(c)
