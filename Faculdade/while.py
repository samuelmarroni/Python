n = 1
while n <= 10:
    print(n, end=' ')
    n += 1
print('')
print('=' * 31)

resp = 'S'

while resp == 'S':

    num = int(input('Número: '))

    if num % 2 == 0:
        print('PAR')
    else:
        print('ÍMPAR')

    resp = input('Deseja continuar? [S/N]')

print('=' * 31)

num = 0
while num < 1 or num > 10:
    num = int(input('Informe um número de 1 a 10:'))
    if num < 1 or num > 10:
        print('Número inválido, digite novamente...')
    print(f'Número {num}, válido.')