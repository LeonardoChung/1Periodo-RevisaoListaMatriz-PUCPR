from prettytable import PrettyTable

matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input('Digite o valor da posição [{0}][{1}]: '.format(i+1, j+1)))
        linha.append(valor)
    matriz.append(linha)

soma = 0
for i in range(3):
    soma += matriz[i][2-i]

tabela = PrettyTable()
tabela.field_names = ['Coluna {0}'.format(j+1) for j in range(3)]

for linha in matriz:
    tabela.add_row(linha)

print('Matriz:')
print(tabela)
print('Soma da diagonal secundária: {0}'.format(soma))
