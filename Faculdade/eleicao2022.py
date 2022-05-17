# 'n' representa o número de candidatos.
n = int(input())
l1 = []
l2 = []
for i in range(n):
    l1.append(input())
totalVotos = 0
votosValidos = 0
# 'i' representa o número de votos. Os dois últimos números representam os nulos e brancos.
for i in range(n+2):
    l2.append(int(input()))
    if i < n:
        votosValidos += l2[i]
    totalVotos += l2[i]

media = votosValidos/2

maxVotos = 0
posMaxVotos = 0
for i in range(n):
    if l2[i] > maxVotos:
        maxVotos = l2[i]
        posMaxVotos = i
if maxVotos > media:
    print(l1[posMaxVotos], "foi o vencedor da eleição")
else:
    print("Haverá segundo turno entre:")
    print(l1[posMaxVotos])
    segMaxVotos = 0
    posSegMaxVotos = 0
    for i in range(n):
        if l2[i] > segMaxVotos and l2[i] != maxVotos:
            segMaxVotos = l2[i]
            posSegMaxVotos = i
    print(l1[posSegMaxVotos])
print("Total de votos:", totalVotos)
print("Votos válidos:", votosValidos)
