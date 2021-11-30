#Pedindo dados ao usuário
numero = int(input("Digite o valor de n: ") )

#Atribuindo valores para as variáveis
resultado=1
count=1

#Verificando se o número digitado pelo usuário é maior que 0
if numero > 0:
    #realizando o fatorial do número digitado pelo usuário
    while count <= numero:
        resultado *= count
        count += 1
#Se o número digitado pelo usuário for igual a 1, não é necessário fazer uma conta, já que o fatorial de 1 é 1
else:
    resultado = 1

#Mostrando o fatorial do número digitado pelo usuário
print(resultado)

	
