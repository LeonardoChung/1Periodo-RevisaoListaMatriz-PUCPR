from prettytable import PrettyTable

def ler_matriz():
    matriz = []
    for i in range(3):
        linha = []
        for j in range(3):
            valor = int(input(f'Digite o valor da posição [{i+1}][{j+1}]: '))
            linha.append(valor)
        matriz.append(linha)
    return matriz

def calcular_quadrado_matriz(matriz):
    matriz_quadrado = []
    for i in range(3):
        linha = []
        for j in range(3):
            elemento = matriz[i][j] ** 2
            linha.append(elemento)
        matriz_quadrado.append(linha)
    return matriz_quadrado

def exibir_matriz(matriz, nome):
    tabela = PrettyTable()
    tabela.field_names = [f'Coluna {j+1}' for j in range(3)]
    for linha in matriz:
        tabela.add_row(linha)
    print(f'Matriz {nome}:')
    print(tabela)

matriz_a = ler_matriz()
matriz_b = calcular_quadrado_matriz(matriz_a)
exibir_matriz(matriz_b, 'B = A^2')
