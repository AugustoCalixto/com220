# exercicio 3
# Leia uma data no passado e informe em qual dia da semana essa data caiu.
from datetime import datetime
data = datetime.strptime(input("Digite a data no formato dd/mm/aaaa :"), '%d/%m/%Y')

print(data.weekday()) # weekday retorna o dia da semana em indice
