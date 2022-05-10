# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = float(input('Digite um número:'))

dobro = float(n + n)
triplo = float(n * 3)
raiz = float(n ** (1 / 2))

print('O número é {}, seu dobro {}, triplo {} e sua raiz quadrada {}'.format(n, dobro, triplo, raiz))

# Outra maneira:
# n = float(input('Digite um número:'))
# print('O dobro de {} vale {}.'.format(n, (n+2)))
# print('O triplo de {} vale {}. \nA raiz qaudrada de {} é igual a {}.'.format(n, (n*3), n, pow(n, (1/2))))
