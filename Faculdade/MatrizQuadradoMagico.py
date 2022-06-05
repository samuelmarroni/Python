'''
Quadrado Mágico é uma tabela quadrada de lado , onde a soma dos números das
linhas, das colunas e das diagonais é constante, sendo que nenhum destes números se
repete.
'''
n = 0
while n<3:
    n = int(input("Escolha o tamanho da sua matriz quadrada -> "))
    if n<3:
        print("Para o quadrado mágico, tem que ser no mínimo 3x3. Por favor, digite novamente")

qm = []
for i in range(n):
    qm.append([])
    for j in range(n):
        qm[i].append(int(input("[{}][{}] -> ".format(i,j))))

for i in range(n):
    for j in range(n):
        print("{:2}".format(qm[i][j]),end=" ")
    print()

S = (n+n**3)/2
qtd = n*2+2

cont = 0
DP = 0
DS = 0
for i in range(n):
    CL = 0
    CC = 0
    DP += qm[i][i]
    DS += qm[i][n-1-i]
    for j in range(n):
        CL += qm[i][j]
        CC += qm[j][i]
    if CL == S:
        cont += 1
    else:
        break
    if CC == S:
        cont += 1
    else:
        break
if DP == S:
    cont += 1
if DS == S:
    cont += 1

if cont==qtd:
    print("Quadrado Mágico")
else:
    print("Não é quadrado mágico")
