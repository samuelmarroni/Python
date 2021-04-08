#Crie um programa que leia o quanto de dinheiro uma pessoa tem na carteira e mostre quantos dólares e euros ela pode comprar.
#Considere US$1.00 = R$5.55
#Considere 1.00€ = R$6.61

real = float(input('Informe quanto de dinheiro você tem: R$'))

dolar = real/5.55
euro = real/6.61

print('Com R${:.2f} você consegue comprar US${:.2f} e {:.2f}€.'.format(real, dolar, euro))
