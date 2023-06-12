from prettytable import PrettyTable

def ler_valores():
    valores = []
    for _ in range(5):
        valor = float(input('Digite um valor: '))
        valores.append(valor)
    return valores

def calcular_estatisticas(valores):
    maior = max(valores)
    menor = min(valores)
    media = sum(valores) / len(valores)
    return maior, menor, media

def exibir_tabela(valores, maior, menor, media):
    tabela = PrettyTable()
    tabela.field_names = ['Valores', 'Maior', 'Menor', 'Média']
    tabela.add_row([valores, maior, menor, media])
    print(tabela)

valores = ler_valores()
maior, menor, media = calcular_estatisticas(valores)
exibir_tabela(valores, maior, menor, media)
