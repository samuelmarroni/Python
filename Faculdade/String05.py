f = input("Informe uma frase:")
p = input("Informe a palavra:")

L = f.split(" ")
L.remove(p)
frase = ' '.join(L)
print(frase)
