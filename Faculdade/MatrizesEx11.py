#Elabore um programa que leia uma matriz 4x12. Cada coluna indica um mês do ano e cada linha uma semana do respectivo mês. Os valores armazenados representam o total de peças produzidas por uma determinada fábrica. Calcule:

# Total de peças produzidas em cada mês;
# Total de peças produzidas no ano;
# Qual foi a semana e qual o mês onde houve a maior produção.
from random import randint
mes = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
M = [0] * 4
for i in range(4):
    M[i] = [0] * 12
    for j in range(12):
        M[i][j] = randint(50, 100)
# ta = 'Total anual', tm = 'Total mês', m = 'Mês', s = 'Semana'
ta = 0
maior = 0
for j in range(12):
    tm = 0
    for i in range(4):
        tm += M[i][j]
        if M[i][j] > maior:
            maior = M[i][j]
            m = j
            s = i
    ta += tm
    print(f"Total de peças em {mes[j]} = {tm}")

print(f"Produção anual = {ta}")
print(f"Maior produção semanal foi de {maior}")
print(f"Ocorreu na {s}a. semana do mês {mes[m]}")
