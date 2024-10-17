# Deque - Trabalhando com LIFO e FIFO
# deque - Double-ended queue
#
# Lifo  e fifo
# pilha e fila

# LIFO (Last In First Out)
# Pilha (stack)
# Significa que o último item a entrar será o primeiro a sair (list)
# Artigo:
# https://www.otaviomiranda.com.br/2020/pilhas-em-python-com-listas-stack/
# Vídeo:
# https://youtu.be/svWVHEihyNI
# Para tirar itens do final: O(1) Tempo constante
# Para tirar itens do início: O(n) Tempo Linear


from collections import deque

fila_correta: deque[int] = deque()
fila_correta.append(3)
fila_correta.append(4)
fila_correta.append(5)
fila_correta.appendleft(2)
fila_correta.appendleft(1)
fila_correta.appendleft(0)
print(fila_correta)
fila_correta.pop()
fila_correta.popleft()
print(fila_correta)
