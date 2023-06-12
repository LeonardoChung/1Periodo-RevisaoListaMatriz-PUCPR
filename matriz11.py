from prettytable import PrettyTable

def ler_matriz():
    matriz = []
    for i in range(3):
        linha = []
        for j in range(3):
            valor = int(input('Digite o valor da posição [{0}][{1}]: '.format(i+1, j+1)))
            linha.append(valor)
        matriz.append(linha)
    return matriz

def calcular_soma_diagonal_secundaria(matriz):
    soma = 0
    for i in range(3):
        soma += matriz[i][2-i]
    return soma

def exibir_matriz(matriz):
    tabela = PrettyTable()
    tabela.field_names = ['Coluna {0}'.format(j+1) for j in range(3)]
    for linha in matriz:
        tabela.add_row(linha)
    print('Matriz:')
    print(tabela)

matriz = ler_matriz()
soma_diagonal_secundaria = calcular_soma_diagonal_secundaria(matriz)
exibir_matriz(matriz)
print('Soma da diagonal secundária: {0}'.format(soma_diagonal_secundaria))
