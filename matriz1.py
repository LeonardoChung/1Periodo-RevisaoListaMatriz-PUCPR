from prettytable import PrettyTable

matriz = []
for i in range(4):
    linha = []
    for j in range(4):
        valor = int(input(f'Digite o valor da posição [{i+1}][{j+1}]: '))
        linha.append(valor)
    matriz.append(linha)

contador = 0
for linha in matriz:
    for valor in linha:
        if valor > 10:
            contador += 1

tabela = PrettyTable()
tabela.field_names = [f'Coluna {j+1}' for j in range(4)]

for linha in matriz:
    tabela.add_row(linha)

print('Matriz:')
print(tabela)
print(f'A matriz possui {contador} valores maiores que 10.')
