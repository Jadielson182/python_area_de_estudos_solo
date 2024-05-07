# Implemente uma classe chamada TempoDeExecucaoContexto que pode ser usada como um gerador 
# de contexto para medir o tempo de execução de um bloco de código.

import time

class TempoDeExecucaoContexto:
    def __enter__(self):
        self.inicio = time.time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.fim = time.time()
        tempo_total = self.fim - self.inicio
        print(f"Tempo de execução: {tempo_total} segundos")

# Exemplo de uso:
with TempoDeExecucaoContexto():
    # Código a ser medido
    time.sleep(3)
