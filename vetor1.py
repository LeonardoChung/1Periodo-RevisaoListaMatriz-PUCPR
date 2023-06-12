from prettytable import PrettyTable

def calcular_soma(valores):
    soma = valores[0] + valores[1] + valores[-1]
    return soma

def substituir_valor(valores, indice, novo_valor):
    valores[indice] = novo_valor
    return valores

def exibir_tabela(valores):
    tabela = PrettyTable()
    tabela.field_names = ['Valores']
    for valor in valores:
        tabela.add_row([valor])
    print(tabela)

a = [1, 0, 5, -2, -5, 7]

soma = calcular_soma(a)
print('-' * 65)
print('A soma entre o primeiro, o segundo e o último valor é igual a {}.'.format(soma))
print('-' * 65)

a = substituir_valor(a, 4, 100)

exibir_tabela(a)
