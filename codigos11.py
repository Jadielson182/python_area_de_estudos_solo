from functools import reduce

produtos = [
    {'nome': 'produto 5', 'preco': 10.00},
    {'nome': 'produto 1', 'preco': 22.32},
    {'nome': 'produto 3', 'preco': 10.18},
    {'nome': 'produto 2', 'preco': 105.87},
    {'nome': 'produto 4', 'preco': 69.95},
]

def funcao_do_reuce(acumulador, produto):
    # print('acumulador é', acumulador)
    # print('produto é', produto)
    # print()
    return round(acumulador + produto['preco'], 2)


total = reduce(funcao_do_reuce, produtos, 0)

total2 = reduce(lambda acumulador, produto: acumulador + produto['preco'], produtos, 0)

total3 = 0
for produto in produtos:
    total3 += produto['preco']
    
print('total', total)
print('total2',total2)
print('total3', total3)