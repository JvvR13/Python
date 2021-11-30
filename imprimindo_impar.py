#Pedindo valores ao usuário
x = int(input("Digite o valor de n: "))

#Variável "cont" recebe 0 como valor
cont = 0

#Variável "x" é subtraido 1
x -= 1

#Se o número digitado pelo usuário for Impar é impresso na tela
while cont <= x * 2:

        cont +=1

        if cont % 2 != 0:

                print(cont)
