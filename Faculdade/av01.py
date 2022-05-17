#Breno Ryuky Funo Nakamura	        R.A.:626953
#Evandro Horiuti Sakuma		        R.A.:567582
#Felipe Garbelini Ferreira 	        R.A.:624421
#Gabriel Gomes Batista Nunes 	    R.A.:624403
#Leonardo Kenji Funai 		        R.A.:626597
#Samuel Icaro Marroni               R.A.:623989
#Thiago De Araujo Bernardineli 	    R.A.:626198

print("Informe os valores:")
x1 = float(input("x1 = "))
y1 = float(input("y1 = "))
x2 = float(input("x2 = "))
y2 = float(input("y2 = "))

dist = (((x2 - x1)**2)+((y2 - y1)**2))**(0.5)

print(f"A distancia entre p1({x1}, {y1}) e p2({x2}, {y2}) é igual a {dist :0.4f}")
