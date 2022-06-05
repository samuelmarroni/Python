n = float(input("Digite o valor do troco:"))
n *= 100
moedas = [100, 25, 10, 5, 1]
total = 0
qtd = []
for i in range(len(moedas)):
    num_moedas = n//moedas[i]
    num_moedas = int(num_moedas)
    qtd.append(num_moedas)
    n %= moedas[i]
    total += num_moedas
    
for i in range(len(moedas)):
    print(f"{qtd[i]} moedas de {moedas[i]}")

print(f"Total de moedas {total}")
