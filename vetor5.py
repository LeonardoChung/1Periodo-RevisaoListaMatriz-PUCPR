from prettytable import PrettyTable

vetor = []

for i in range(10):
    valor = int(input(f'Digite o valor {i+1}: '))
    vetor.append(valor)

contador = 0
for valor in vetor:
    if valor % 2 == 0:
        contador += 1

tabela = PrettyTable()
tabela.field_names = ['Vetor']

for valor in vetor:
    tabela.add_row([valor])

print('Valores do vetor:')
print(tabela)
print(f'O vetor possui {contador} valores pares.')
