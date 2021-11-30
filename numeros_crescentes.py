#É pedido ao usuário que digite 3 número para assim saber se esta em ordem crescente 
n1 = float(input("Digite o Primeiro número: "))
n2 = float(input("Digite o Segundo número: "))
n3 = float(input("Digite o Terceiro número: "))


#Caso os 3 número estiver em ordem crescente é escrito na tela "Crescente"
if(n1 < n2 and n2 < n3):
   print("Crescente")
#Caso os 3 números digitados estejam em ordem alternadas, é impresso na tela "não esta em ordem Crescente"
else:
   print("Não está em ordem Crescente")