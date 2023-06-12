from prettytable import PrettyTable

A = []
for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f'Digite o valor da posição [{i+1}][{j+1}]: '))
        linha.append(valor)
    A.append(linha)

B = []
for i in range(3):
    linha = []
    for j in range(3):
        elemento = A[i][j] ** 2
        linha.append(elemento)
    B.append(linha)

tabela = PrettyTable()
tabela.field_names = [f'Coluna {j+1}' for j in range(3)]

for linha in B:
    tabela.add_row(linha)

print('Matriz B = A^2:')
print(tabela)
