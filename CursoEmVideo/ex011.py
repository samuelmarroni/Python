#Faça um programa  que leia a largura e altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².

altura = float(input('Informe a altura:'))
largura = float(input('Informe a largura:'))

media = float(altura*largura)
tinta = float(media/2)

print('A parede tem uma área de {}m e precisaremos de {}l de tinta para pinta-lá.'.format(media, tinta))
