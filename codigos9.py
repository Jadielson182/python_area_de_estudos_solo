
from functools import partial 
from types import GeneratorType

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


produtos = [
    {'nome': 'produto 5', 'preco': 10.00},
    {'nome': 'produdo 1', 'preco': 22.32},
    {'nome': 'produto 3', 'preco': 10.11},
    {'nome': 'produto 2', 'preco': 105.87},
    {'nome': 'produto 4', 'preco': 69.90}
]


def aumenta_valor(valor, porcentagem):
    return round (valor * porcentagem, 2)


def muda_preco_de_produto(produto):
    return {**produto,'preco': porcentagem_de_aumento(produto['preco'])}

porcentagem_de_aumento = partial(aumenta_valor, porcentagem=1.2)

# novos_produtos = [
# {**p,'preco': porcentagem_de_aumento(p['preco'])} 
# if p['preco']  < 200 else {**p}  # isso e  mapeamento - map
# for p in produtos
# if p['preco'] > 0 # isso e o filtro - filter
# ]

novos_produtos = list(map(
    muda_preco_de_produto, produtos)
) 

# novos_produtos = (x for x in produtos)
# novos_produtos = [
#     {**p,'preco': aumenta_valor(p['preco'], 1.1)} 
#     if p['preco']  < 50.00 else {**p}
#     for p in produtos

# ]
print_iter(produtos)
print_iter(novos_produtos)
print(*list(novos_produtos), sep='\n')
print()
print(*list(novos_produtos), sep='\n')

print(list(map(lambda x: x * 3, [1, 2, 3, 4])))

print(hasattr(novos_produtos, '__iter__'))
print(hasattr(novos_produtos, '__next__'))
print(isinstance(novos_produtos, GeneratorType))
