def ehPalindromo(string):
    count = int(string.__len__() - 1)  # quantidade de letras da string
    for letra in string:
        if(letra != string[count]):
            return 'Não é palindromo'
        count = count - 1
    return 'É palindromo'


string = input('Digite uma string: ')
print(ehPalindromo(string))
