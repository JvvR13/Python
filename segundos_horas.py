#Pedido ao usuário que digite um valor em segundos para transformar em horas
s = input("Esse programa é para transformar segundos em minutos e horas, informe um valor")

#O valor digitado pelo usuário é dividido por 60, transformando em horas, e o resto da conta é transformada em minutos 
hr = float(s) // 3600
temp = float(s) % 3600

#O resto da divisão é dividida por 60, transformando em minutos, e o resto da divisão são os segundos 
min = float(temp) // 60
seg = float(temp) % 60

#Imprimindo ao usuário 
print(hr, ":" ,min , ":", seg)







