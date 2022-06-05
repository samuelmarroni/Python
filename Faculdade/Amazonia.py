floresta = ['.'] * 20
for i in range(20):
    floresta[i] = ['.'] * 20

i, j = input().split()
i = int(i)
j = int(j)
while True:
    entrada = input()
    if entrada == 'F':
        break
    if entrada == 'A':
        floresta[i][j] = '#'
    else:
        direcao, k = entrada.split()
        k = int(k)
        if direcao == 'N':
            for p in range(i,i-k-1,-1):
                if floresta[p][j] != '#':
                    floresta[p][j] = '+'
            i -= k

        if direcao == 'S':
            for p in range(i,i+k+1):
                if floresta[p][j] != '#':
                    floresta[p][j] = '+'
            i += k

        if direcao == 'L':
            for p in range(j,j+k+1):
                if floresta[i][p] != '#':
                    floresta[i][p] = '+'
            j += k

        if direcao == 'O':
            for p in range(j,j-k-1,-1):
                if floresta[i][p] != '#':
                    floresta[i][p] = '+'
            j -= k

for i in range(20):
    for j in range(20):
        print(floresta[i][j], end=' ')
    print()
