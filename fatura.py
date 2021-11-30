#Pedindo ao usuário o nome do cliente
nome = input("Digite o nome do cliente: ")
#Pedindo ao usuário o dia do vencimento da fatura
dvenc = input("Digite o dia de vencimento: ")
#Pedindo ao usuário o mês do vencimento da fatura
mvenc = input("Digite o mês de vencimento: ")
#Pedindo ao usuário o valor da fatura
fat = input("Digite o valor da fatura: ")

#Mostrando ao usuário o nome do cliente, vencimento e valor da fatura
print("Olá, ", nome)
print("A sua fatura com vencimento em ", dvenc, " de ", mvenc, " no valor de R$ ", fat," está fechada.")
