
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

def filtra_preco(produto):
    return produto['preco'] > 10

#alternativas para fazer o filtro

# 1-
novos_produtos = filter(
    filtra_preco, produtos
)

#2-
# novos_produtos = filter(
#     lambda produto: produto['preco'] > 10, produtos

# )
#3- o list comprehension
# novos_produtos  = [
#     produto for produto in produtos
#     if produto['preco'] > 10
# ]

print_iter(produtos)
print_iter(novos_produtos)