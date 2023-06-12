from prettytable import PrettyTable

def ler_valores():
    valores = []
    for i in range(6):
        valor = int(input('Digite um valor inteiro par: '))
        while valor % 2 != 0:
            valor = int(input('Digite um valor inteiro par: '))
        valores.append(valor)
    return valores

def exibir_tabela(valores):
    tabela = PrettyTable()
    tabela.field_names = ['Valores lidos na ordem inversa']

    for valor in reversed(valores):
        tabela.add_row([valor])

    print(tabela)

valores = ler_valores()
exibir_tabela(valores)
