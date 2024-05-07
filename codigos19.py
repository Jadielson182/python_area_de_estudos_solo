

def adiciona_clientes(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista


cliente1 = adiciona_clientes('Jhon')
adiciona_clientes('maria', cliente1)
adiciona_clientes('veveta', cliente1)
cliente1.append('marcos')

cliente2 = adiciona_clientes('naldo')
adiciona_clientes('mario', cliente2 )
cliente2.append('marino')
cliente2.append('maritinha')

cliente3 = adiciona_clientes('defena')
cliente3.append('marinovaldo')
cliente3.append('tantinha')


print(cliente1)
print(cliente2)
print(cliente3)