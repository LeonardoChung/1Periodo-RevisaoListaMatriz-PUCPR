from prettytable import PrettyTable

valores = []

for _ in range(5):
    valor = float(input('Digite um valor: '))
    valores.append(valor)

maior = max(valores)
menor = min(valores)
media = sum(valores) / len(valores)

tabela = PrettyTable()
tabela.field_names = ['Valores', 'Maior', 'Menor', 'Média']

tabela.add_row([valores, maior, menor, media])

print(tabela)
