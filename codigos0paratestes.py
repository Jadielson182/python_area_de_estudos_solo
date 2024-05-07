# from pathlib import Path

# LOG_FILE = path(__file__).parent

# class Log:
#     def _log(self, msg):
#         raise NotImplementedError('Implemente o método log')


#     def log_error(self, msg):
#         return self._log(f'Falha: {msg}')

#     def log_success(self, msg):
#         return self._log(f'Success: {msg}')


# class LogFileMixin(Log):
#     def _log(self, msg):
#         print(msg)


# class LogPrintMixin(Log):
#     def _log(self, msg):
#         print(f'{msg} ({self.__class__.__name__})')



# if __name__ == '__main__':
#     l = LogPrintMixin()
#     l.log_error('Error no Log')
#     l.log_success('Log Success')
#     print(LOG_FILE)

from contextlib import contextmanager


@contextmanager
def my_open(caminho_arquivo, modo):
    try:
        print('Abrindo arquivo')
        arquivo = open(caminho_arquivo, modo, encoding='utf8')
        yield arquivo
    except Exception as e:
        print('Ocorreu erro', e)
    finally:
        print('Fechando arquivo')
        arquivo.close()


with my_open('aula150.txt', 'w') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n', 123)
    arquivo.write('Linha 3\n')
    print('WITH', arquivo)