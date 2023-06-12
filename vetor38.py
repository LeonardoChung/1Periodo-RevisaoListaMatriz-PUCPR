from prettytable import PrettyTable

def ler_valores():
    valores = []
    for _ in range(10):
        valor = int(input('Digite um valor numérico: '))
        valores.append(valor)
    return valores

def ordenar_valores(valores):
    vetor = []
    for valor in valores:
        posicao = 0
        while posicao < len(vetor) and valor > vetor[posicao]:
            posicao += 1
        vetor.insert(posicao, valor)
    return vetor

def exibir_tabela(valores):
    tabela = PrettyTable()
    tabela.field_names = ['Valores em ordem crescente']
    for valor in valores:
        tabela.add_row([valor])
    print(tabela)

valores = ler_valores()
valores_ordenados = ordenar_valores(valores)
exibir_tabela(valores_ordenados)
