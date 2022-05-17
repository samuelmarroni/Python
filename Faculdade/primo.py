N = int(input('Entre com um número para saber se é primo >>'))
primo = True
if - 1 <= N <= 1:
    primo = False
else:
    for div in range(2,N//2-1):
        if N % div == 0:
            primo = False
            break

if primo:
    print(f'{N} é um número primo')
else:
    print(f'{N} não é um número primo')