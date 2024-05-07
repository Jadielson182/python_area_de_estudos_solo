
import random
# random.seed(2) 
#-> sedd inicializa o gerador do random( por isso "números pseudoaleatorios")
# pode usar o modulo time para importa time e ver os microsegundos e ver qual elemento vai ser chamado no random

# random.randrange(início, fim, passo)
#   -> Gera um número inteiro aleatório dentro de um intervalo específico
r_range = random.randrange(10, 20, 2)
# print(r_range)

# random.randint(início, fim)
#   -> Gera um número inteiro aleatório dentro de um intervalo "sem passo"
r_int = random.randint(10, 20)
# print(r_int)

# random.uniform(início, fim)
#   -> Gera um número flutuante aleatório dentro de um intervalo "sem passo"
r_uniform = random.uniform(10, 20)
# print(r_uniform)

#random.shuffle(SequenciaMutável) -> embaralha a lista original
nomes = ['Luiz', 'Maria', 'Helena', 'Joana' ]
nova_lista = []
for nome in nomes:
    nova_lista.append(nome)
random.shuffle(nova_lista)
print(nomes)
print(nova_lista)

# random.sample(Iterável, K=N) Escolhe elementos do iterável e retorna outro iterável(não repete)
nomes = ['Luiz', 'Maria', 'Helena', 'Joana' ]
novos_nomes = random.sample(nomes, k=3) #sample pega elementos aleatorio da lista, k=representa o numero de elementos 
print(nomes)
print(novos_nomes)

#random.choices(Iterável) -> Escolhe elementos do iterável e retorna outro iterável(repete valores)
nomes = ['Luiz', 'Maria', 'Helena', 'Joana' ]
novos_nomes = random.choices(nomes, k=3)
print(nomes)
print(novos_nomes)



#random.choice(Iterável)-> escolhe um elemento do iterável
nomes = ['Luiz', 'Maria', 'Helena', 'Joana' ]
print(random.choice(nomes))