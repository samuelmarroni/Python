from random import randint

valorAp = float(input("Valor em reais da aposta >>"))
numAp = int(input("Número apostado >>"))
if numAp < 1 or numAp > 36:
    print("Número inválido!!")
else:
    numSt = randint(1,36)
    print(f"Número sorteado >> {numSt}")
    if numAp == numSt:
        print(f"Você acertou o número e ganhou R$ {valorAp*5:.2f}")
    elif (numAp-1)//12 == (numSt-1)//12:
        print(f"Você acertou o número e ganhou R$ {valorAp * 3:.2f}")
    elif numAp%2 == numSt%2:
        print(f"Você acertou o número e ganhou R$ {valorAp * 2:.2f}")
    else:
        print("Você perdeu o valor apostado!!")