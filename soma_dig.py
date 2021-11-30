#Pedido ao usuário que digite um número inteiro para soma dos dígitos
n = int(input("Digite um número inteiro:"))

res = 0

#Dentro do laço de repetição do While, é realiza a divisão dos números por 10 para que seja possível pegar apenas 1 dos números  
while (n != 0):
    x = (n % 10)
    n = n // 10
    res += x  
#Impresso ao usuário o resultado da soma dos digitos
print(res)
