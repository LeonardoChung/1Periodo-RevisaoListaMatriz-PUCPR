from prettytable import PrettyTable

def ler_valores():
    valores = []
    for i in range(6):
        valor = int(input(f'Digite o valor {i + 1}: '))
        valores.append(valor)
    return valores

def exibir_tabela(valores):
    tabela = PrettyTable()
    tabela.field_names = ['Valores lidos:']
    for valor in reversed(valores):
        tabela.add_row([valor])
    print(tabela)

valores = ler_valores()
exibir_tabela(valores)
