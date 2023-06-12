from prettytable import PrettyTable

valores = []

for i in range(6):
    valor = int(input('Digite um valor inteiro par: '))
    while valor % 2 != 0:
        valor = int(input('Digite um valor inteiro par: '))
    valores.append(valor)

tabela = PrettyTable()
tabela.field_names = ['Valores lidos na ordem inversa']

for valor in reversed(valores):
    tabela.add_row([valor])

tabela.reversesort = True

print(tabela)
