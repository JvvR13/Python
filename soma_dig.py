n = int(input("Digite um número inteiro:"))
res = 0
while (n != 0):
    x = (n % 10)
    n = n // 10
    res += x  
print(res)
