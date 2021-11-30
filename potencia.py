#É pedido um número ao usuário para saber a potência do mesmo
n = int(input("Digite um número para saber sua potência: "))
i = 0
#O while, com o laço de repetição realiza a conta de todas as potências
while i<21:
   #Impresso as potências do número digitado pelo usuário
   print(n, "^", i, " = ", n ** i)
   i += 1