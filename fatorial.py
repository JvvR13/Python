numero = int(input("Digite o valor de n: ") )

resultado=1
count=1

if numero > 0:
    while count <= numero:
        resultado *= count
        count += 1
else:
    resultado = 1

print(resultado)

	
