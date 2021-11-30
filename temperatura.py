#É solicitado ao usuário que digite a temperatura em Fahrenheit 
tempF = input("Digite uma temperatura em Fahrenheit para saber em Celsius: ")
#Realizado o calculo para saber a temperatura em Celsius
tempC = (float(tempF) - 32) * 5 / 9

#Impresso ao usuário a temperatura em Celsius
print("A temperatura em Celsius é de ", tempC) 