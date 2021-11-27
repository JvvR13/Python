s = input("Esse programa é para transformar segundos em minutos e horas, informe um valor")

hr = float(s) // 3600
temp = float(s) % 3600

min = float(temp) // 60
seg = float(temp) % 60

print(hr)
print(min)
print(seg)






