from prettytable import PrettyTable

def multiplicar_matrizes(matriz1, matriz2):
    matriz_resultado = []
    for i in range(len(matriz1)):
        linha = []
        for j in range(len(matriz2[0])):
            soma = 0
            for k in range(len(matriz2)):
                soma += matriz1[i][k] * matriz2[k][j]
            linha.append(soma)
        matriz_resultado.append(linha)
    return matriz_resultado

matriz_a = []
print('Digite os elementos da matriz A:')
for _ in range(3):
    linha = []
    for _ in range(3):
        valor = float(input('Digite um valor: '))
        linha.append(valor)
    matriz_a.append(linha)

matriz_b = []
print('Digite os elementos da matriz B:')
for _ in range(3):
    linha = []
    for _ in range(3):
        valor = float(input('Digite um valor: '))
        linha.append(valor)
    matriz_b.append(linha)

matriz_c = multiplicar_matrizes(matriz_a, matriz_b)

tabela = PrettyTable()
tabela.field_names = ['Matriz C']

for linha in matriz_c:
    tabela.add_row(linha)

print(tabela)
