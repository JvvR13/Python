def maior_primo(n):
    cont = 1
    maior = 0
    while cont <= n:
        if primo(cont):
            if cont > maior:
                maior = cont
        cont += 1
    return maior

def primo(n):
    if n == 2:
        return True

    if not n & 1:
        return False

    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True
