# sys.argv - Executando arquivos com argumentos no sistema
# Fonte = Fira Code
import sys

argumentos = sys.argv
qtd_argumentos = len(argumentos)
print(qtd_argumentos)
if qtd_argumentos  <= 1:
    print('Você não passou argumentos')
else:
    try:
        print(f"mais de um argumento {argumentos[1:]}")
        print(f"mais de um argumento {argumentos[1]}")
        print(f"mais de um argumento {argumentos[2]}")
    except IndexError:
        print('faltam argumentos')




#venv\scripts\python codigos103.py "listar" "cantar"