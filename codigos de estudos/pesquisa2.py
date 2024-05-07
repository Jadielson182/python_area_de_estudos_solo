import time

def tempo_de_execucao(funcao):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = funcao(*args, **kwargs)
        fim = time.time()
        print(f"A função {funcao.__name__} levou {fim - inicio:.5f} segundos para ser executada.")
        return resultado
    return wrapper

@tempo_de_execucao
def exemplo_demorado():
    # Código demorado
    time.sleep(2)
    return "Concluído"

exemplo_demorado()


#


def decorador_log(funcao):
    def wrapper(*args, **kwargs):
        print(f"Executando {funcao.__name__} com argumentos {args} e kwargs {kwargs}.")
        resultado = funcao(*args, **kwargs)
        print(f"{funcao.__name__} retornou {resultado}.")
        return resultado
    return wrapper

@decorador_log
def multiplicacao(a, b):
    return a * b

# Teste
print(multiplicacao(3, 4))


#

def no_space(x):
    x = x.replace(" ", "")
    print(x)
     
no_space("8 j 8   mBliB8g  imjB8B8  jl  B")
no_space("8 8 Bi fk8h B 8 BB8B B B  B888 c hl8 BhB fd")
no_space("8aaaaa dddd r     ")