# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preço = float(input('Qual o preço do produto?'))

novo = preço - (preço * 5 / 100)

print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar {:.2f}'.format(preço, novo))
