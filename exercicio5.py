#exercicio 5
x = int(input("Quantos nomes você deseja armazenar?\n"))
lista_nome = []

while (x > 0):
    print("Faltam {0} nomes".format(x))
    x = x - 1
    lista_nome.append(input("Digite um nome: "))

print(lista_nome)
    