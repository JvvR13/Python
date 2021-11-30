#Pedindo valores ao usuário para saber se ele é Impar ou Par
n = int(input("Digite um número para saber se ele é Impar ou Par: "))

#Verificando se o número digitado pelo usuário é mod de 2, sendo assim, é par
if(n % 2 == 0):
   #Mostrando que o número é Par
   print("Seu número é Par")
#Caso não, o número é impar
else:
   #Mostrando que o número é Impar
   print("Seu número é Impar")
	 
