#Pedindo o valor da Largura ao usuário
largura = int(input("Entre com a largura: "))

#Pedindo o valor da Altura ao usuário
altura = int(input("Entre com a altura: ")) 

#Atribuindo valores para "a"
a=1

#while para imprimir na tela "#" conforme a Altura do retângulo
while(a <= altura):
    #Atribui 1 a variável "l"
    l = 1
    #while para imprimir na tela "#" conforme a Largura do retângulo
    while(l <= largura):
        print("#",end="")
        #Acrescer 1 a variável "l"
        l += 1
    
    print('')
    #Acrescer 1 a variável "a"
    a += 1
