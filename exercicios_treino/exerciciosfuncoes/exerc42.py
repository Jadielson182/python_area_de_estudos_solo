# Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais:
#  taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto.
#  A função “altera” o valor de custo para incluir o imposto sobre vendas.

def somaImposto(nome, taxa, custo):
    imposto = (custo / 100) * taxa
    valor_final = custo + imposto
    print(f'{nome} custa R${custo:.2f} a vista e R${valor_final:.2f} parcelado com taxa de {taxa}%.')


somaImposto('Bicicleta', 10, 1500)



