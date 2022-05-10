# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.

metros = float(input('Informe a quantidade de metros:'))

cent = float(metros * 100)
mili = float(metros * 1000)

print('{}m são {:.0f}cm e {:.0f}mm.'.format(metros, cent, mili))
