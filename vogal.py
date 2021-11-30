#função para verificar se a letra digitada pelo usuário é vogal ou consoante
def vogal (v):
    #O if realiza a verificação para ver se a letra digitada é vogal
    if v in "aeiouAEIOU":
        #Se a letra digitada for vogal, retornara true
        return True
    else:
        #Se a letra digitada for consoante, retornara false
        return False