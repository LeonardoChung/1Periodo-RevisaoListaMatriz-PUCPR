from prettytable import PrettyTable

valores = []

for i in range(6):
    valor = int(input(f'Digite o valor {i + 1}: '))
    valores.append(valor)

tabela = PrettyTable()
tabela.field_names = ['Valores lidos:']

for valor in valores:
    tabela.add_row([valor])
print(tabela)
