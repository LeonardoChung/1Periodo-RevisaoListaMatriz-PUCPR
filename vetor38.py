from prettytable import PrettyTable

vetor = []
for _ in range(10):
    valor = int(input('Digite um valor numérico: '))

    posicao = 0
    while posicao < len(vetor) and valor > vetor[posicao]:
        posicao += 1

    vetor.insert(posicao, valor)

tabela = PrettyTable()
tabela.field_names = ['Valores em ordem crescente']

for valor in vetor:
    tabela.add_row([valor])

print(tabela)
