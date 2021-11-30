#Pedindo o valor da Largura ao usuário
largura = int(input("digite a largura: "))

#Pedindo o valor da Altura ao usuário
altura = int(input("digite a altura: "))

#Imprimi na tela "#" conforme a Largura do retângulo
print("#" * largura)

#Realiza um for para imprimir "#" na tela conforme a largura e altura
for _ in range(altura-2):
    print("#" + " " * (largura-2) + "#")

#Imprimi na tela "#" conforme a Largura do retângulo
print("#" * largura)
