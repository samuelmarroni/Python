'''
Elabore um programa em Python que gere uma SURPRESINHA, ou seja, uma aposta para
a MEGASENA, com 6 números entre 1 e 60, sem repetição, armazenando em um vetor.
Faça a validação.
'''
from random import randint

surpresinha = []
while len(surpresinha) != 6:
    n = randint(1,60)
    if n not in surpresinha:
        surpresinha.append(n)
surpresinha.sort()
print("Surpresinha gerada >>",*surpresinha)

megasena = []
i = 1
print("Informe os números que sairam na Megasena")
while len(megasena) != 6:
    n = int(input(f"{i}º >> "))
    if n < 1 or n > 60:
        print("Número inválido. Digite um valor entre 1 e 60...")
    else:
        if n not in megasena:
            megasena.append(n)
            i += 1
        else:
            print("Número já informado. Digite outro...")
megasena.sort()
print("Consurso da Megasena >>",*megasena)

acertos = []
for i in range(6):
    if surpresinha[i] in megasena:
        acertos.append(surpresinha[i])
qt = len(acertos)
print(f"Você acertou {qt} números")
if qt > 0:
    print("Números certos >>",*acertos)
    if qt == 4:
        print("QUADRA!!")
    elif qt == 5:
        print("QUINA!!")
    elif qt == 6:
        print("SENA!!!!!!!!!!!!!")
