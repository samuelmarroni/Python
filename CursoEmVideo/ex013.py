# Faça um algortimo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input('Informe o seu salário: R$'))

nsalario = salario + (salario * 15/100)

print('Seu salário de R${:.2f}, com um aumento de 15% vai para R${:.2f}'.format(salario, nsalario))
