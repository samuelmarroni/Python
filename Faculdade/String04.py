f = input("Informe uma frase:")
sigla = []

L = f.split(" ")
for i in range(len(L)):
    sigla.append(L[i][0])
print(*sigla)
