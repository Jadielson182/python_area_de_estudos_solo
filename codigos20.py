
def listar(param):
    print(f'comandos: listar, desfazer, refazer')
    return input('Digite uma tarefa ou comando, para finalizar digite sair: ').lower()


def desfazer(lista1, lista2):
    if len(lista1) == 0:
        return print('Nada a desfazer')
    lista2.append(lista1[-1])
    lista1.pop()
    return lista1, lista2


def refazer(lista1, lista2):
    if len(lista2) == 0:
        return print('Nada a refazer')
    lista1.append(lista2[0])
    lista2.pop(0)
    return lista1, lista2

def adiciona_tarefa(tarefa, comando):
    tarefa.append(comando)
    return tarefa



tarefas = []
tarefas_desfeitas = []
while True:
    comando = listar('comandos')
    print()
    if comando == 'listar':
        print('TAREFAS:',*tarefas, sep='\n')
        print()
    elif comando == 'desfazer':
        print()
        desfazer(tarefas, tarefas_desfeitas)
        print('TAREFAS:',*tarefas, sep='\n')
        print()
    elif comando == 'refazer':      
        refazer(tarefas, tarefas_desfeitas)
        print()
        print('TAREFAS:',*tarefas, sep='\n')
        print()
    elif comando == 'sair':
        break
    else:
        adiciona_tarefa(tarefas, comando)


print(tarefas)
print(tarefas_desfeitas)

