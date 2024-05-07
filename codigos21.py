import os

def listar(tarefas):
    if not tarefas:
        print('Nenhuma tarefa para listar')
    print()
    print('TAREFAS:')
    print()
    for tarefa in tarefas:
        print(f'\t{tarefa}')
    print()


def desfazer(tarefas, tarefas_desfazer):
    if not tarefas:
        print()
        print('Nenhuma tarefa para desfazer')
        print()
        return 
    tarefa = tarefas.pop()
    print(f'{tarefa} removida da lista de tarefas')
    tarefas_desfazer.append(tarefa)
    print(f'{tarefas}')
    return 
    print()


def refazer(tarefas, tarefas_refazer):
    if not tarefas_refazer:
        print()
        print('Nenhuma tarefa para refazer')
        print()
        return 
    tarefa = tarefas_refazer.pop(0)
    print(f'{tarefa} adicionada a lista de tarefas')
    tarefas.append(tarefa)
    return


def adiciona_tarefa(tarefa, comando):
    print()
    # tarefa = tarefa.strip()g

    if not comando:
        print('Você não digitou uma tarefa.')
        return
    tarefa.append(comando)
    print(f'{tarefa} adicionada a lista de tarefas')
    return 



tarefas = []
tarefas_desfeitas = []
while True:
    print(f'comandos: listar, desfazer, refazer')
    comando = input('Digite uma tarefa ou comando, para finalizar digite sair: ').lower()
    if comando == 'listar':
        listar(tarefas)
        continue
    elif comando == 'desfazer':
        desfazer(tarefas, tarefas_desfeitas)
        listar(tarefas)
        continue
    elif comando == 'refazer':      
        refazer(tarefas, tarefas_desfeitas)
        listar(tarefas)
        continue
    elif comando == 'cls':
        os.system('cls')
        continue
    elif comando == 'sair':
        break
    else:
        adiciona_tarefa(tarefas, comando)
        listar(tarefas)
        continue

