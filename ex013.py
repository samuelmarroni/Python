salario = float(input('Informe o seu salário: R$'))

nsalario = salario + (salario * 15/100)

print('Seu salário de R${:.2f}, com um aumento de 15% vai para R${:.2f}'.format(salario, nsalario))
