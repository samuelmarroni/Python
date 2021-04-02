#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

valor = (input("Digite algo: "))

print("O tipo primitivo desse valor é {}".format(type(valor)))
print("Só tem espaços? {}".format(valor.isspace()))
print("É um número? {}".format(valor.isnumeric()))
print("É alfabético? {}".format(valor.isalpha()))
print("É alfanumérico? {}".format(valor.isalnum()))
print("Esta em maiúsculas? {}".format(valor.isupper()))
print("Esta em minúsculas? {}".format(valor.islower()))
print("Esta capilatizado? {}".format(valor.istitle()))
