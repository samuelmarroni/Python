p = input("Digite uma palavra:")
inv = p[::-1]
print(f"Palavra = {p}")
print(f"Invertida = {inv}")
if p == inv:
    print("São palídromos!")
else:
    print("Não são palídromos!")
