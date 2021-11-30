linha = 1
coluna = 1
#O While realiza o laço para multiplicação dos números que compoem a tabuada
while linha <= 10:
	while coluna <= 10:
		#Imprimindo ao usuário a tabuada
		print(linha, " x ", coluna, " = ", linha * coluna)
		coluna += 1
	linha += 1
	print(end = "\t")
	coluna = 1