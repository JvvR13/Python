#Essa função realiza a soma dos elementos de uma lista
def soma_elementos(l):
    n = 0
    #Esse For, pega cada um dos itens da lista e soma em uma variável
    for e in l:
        n += e
    #Aqui é retornado ao usuário o valor da soma dos elementos da lista
    return n
