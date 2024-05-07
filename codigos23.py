import os
import json

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
    with open('codigos23.json', 'w+', encoding='utf8') as arquivo:
        json.dump(tarefa, arquivo, ensure_ascii=False, indent=2)
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
    # with open('codigos23.json', 'w+', encoding='utf8') as arquivo:
        # json.dump(tarefa, arquivo, ensure_ascii=False, indent=2)
    print(f'{comando} adicionada a lista de tarefas')
    return 


def ler(tarefas, caminho_arquivo):
    dados = []
    try:
        with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        print('Arquivo não existe')
        salvar(tarefas, caminho_arquivo)
    return dados

def salvar(tarefas, caminho_arquivo):
    dados = tarefas
    with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
        dados = json.dump(tarefas, arquivo, indent= 2, ensure_ascii= False)
    return dados


CAMINHO_ARQUIVO = 'codigos23.json'
tarefas = ler([], CAMINHO_ARQUIVO)
tarefas_desfeitas = []


while True:
    print(f'comandos: listar, desfazer, refazer')
    comando = input('Digite uma tarefa ou comando, para finalizar digite sair: ').lower()


    comandos = {
        'listar': lambda: listar(tarefas),
        'desfazer': lambda: desfazer(tarefas, tarefas_desfeitas),
        'refazer': lambda: refazer(tarefas, tarefas_desfeitas),
        'cls':lambda: os.system('cls'),
        'adiciona_tarefa': lambda: adiciona_tarefa(tarefas, comando),
    }

    tarefa = comandos.get(comando) if comandos.get(comando) is not None else comandos['adiciona_tarefa']

    tarefa()
    salvar(tarefas, CAMINHO_ARQUIVO)

    # with open('codigos23.json', 'w', encoding='utf8') as arquivo:
    #     json.dump(ffffff, arquivo, ensure_ascii=False, indent=2)