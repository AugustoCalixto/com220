x = float(input("digite um numero: "))
count = 0
soma = x
while(x != 0.0):
    x = float(input("digite um numero: "))
    soma = soma + x  # soma de  todos numeros digitados
    count = count + 1

print(soma/count)
