from prettytable import PrettyTable

def ler_valores():
    vetor = []
    for i in range(10):
        valor = int(input(f'Digite o valor {i+1}: '))
        vetor.append(valor)
    return vetor

def contar_valores_pares(vetor):
    contador = 0
    for valor in vetor:
        if valor % 2 == 0:
            contador += 1
    return contador

def exibir_tabela(vetor):
    tabela = PrettyTable()
    tabela.field_names = ['Vetor']

    for valor in vetor:
        tabela.add_row([valor])

    print('Valores do vetor:')
    print(tabela)

vetor = ler_valores()
contador = contar_valores_pares(vetor)
exibir_tabela(vetor)
print(f'O vetor possui {contador} valores pares.')
