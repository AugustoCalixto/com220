string = input('Digite uma string: ')
count = int(string.__len__() - 1)  # quantidade de letras da string
palindromo = True  # condição inicial do palindromo

for letra in string:
    if(letra != string[count]):
        palindromo = False
    count = count - 1

print(palindromo)
