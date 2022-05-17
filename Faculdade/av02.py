#Breno Ryuky Funo Nakamura	        R.A.:626953
#Evandro Horiuti Sakuma		        R.A.:567582
#Felipe Garbelini Ferreira 	        R.A.:624421
#Gabriel Gomes Batista Nunes 	    R.A.:624403
#Leonardo Kenji Funai 		        R.A.:626597
#Samuel Icaro Marroni               R.A.:623989
#Thiago De Araujo Bernardineli 	    R.A.:626198

n1 = int(input("Informe um número:"))
n2 = int(input("Informe outro número:"))

n3 = n1
n4 = n2

i = 1
s = 0

while(n3 != 0 or n4 != 0):
    s += ((n1 % (10 ** i)) + (n2 % (10 ** i)))//(10 ** i)
    i += 1
    n3 //= 10
    n4 //= 10


print(f'{s} "vai 1"')
