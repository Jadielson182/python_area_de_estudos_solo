from itertools import combinations, permutations, product


def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


pessoas = ['Joao', 'Joana', 'Luiz', 'Letícia']


camisetas = [ ['preta', 'branca'],
              ['p', 'm', 'g'],
              ['masculino', 'feminino', 'unisex'],
              ['algodao', 'poliéster']
]

# print_iter(combinations(pesoas, 2))
# print_iter(permutations(pessoas, 2))
print_iter(product(*camisetas))