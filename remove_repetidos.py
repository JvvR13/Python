#Essa função realiza a retirada de números repetidos de uma determinada lista
def remove_repetidos(lista):
    #Criação de variável de uma lista
    l = []
    #O for realiza a verificação de quais número são repetidos ou não
    for i in lista:
        if i not in l:
            l.append(i)
    l.sort()
    return l

	