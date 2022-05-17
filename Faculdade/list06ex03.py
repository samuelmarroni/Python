from random import randint
L=[]
b=[]
c=[]
for i in range(5):
    L.append(randint(1,50))
    b.append(randint(1, 50))
for i in range(5):
    for j in range(i+1, 5):
        if L[i] > L[j]:
            L[i], L[j] = L[j], L[i]
for i in range(5):
    for j in range(i+1, 5):
        if b[i] > b[j]:
            b[i], b[j] = b[j], b[i]
print(f'Conjunto 1:{L}')
print(f'Conjunto 2:{b}')
for i in (len(L) + len(b)):
   if L[i] < b[i]:
       c.insert(L[i])
   else:
       c.insert(b[i])
print(c)