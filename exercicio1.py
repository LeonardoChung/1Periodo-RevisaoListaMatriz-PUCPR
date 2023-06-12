from prettytable import PrettyTable
a = [1, 0, 5, -2, -5, 7]

soma = a[0] + a[1] + a[5]
print('-' * 65)
print('A soma entre o primeiro, o segundo e ultimo valor é igual a {}.'.format(soma))
print('-' * 65)

a[4] = 100
tabela = PrettyTable()
tabela.field_names = ['Valores']

for valor in a:
    tabela.add_row([valor])

print(tabela)
