from pathlib import Path

FILE_LOG = Path(__file__).parent / 'Log.txt'

class Log:
    def _log(self, msg):
        raise NotImplementedError ('Implemente o método log')

    def log_error(self, msg):
        return self._log(f'Error: {msg}')

    def log_success(self, msg):
        return self._log(f'Success: {msg}')

class LogFileMixin(Log):
    def _log(self, msg):
        msg_formatada = f'{msg} ({self.__class__.__name__})'
        print('Salvando no log...', msg_formatada)
        with open(FILE_LOG, 'a') as arquivo:
            arquivo.write(msg_formatada)
            arquivo.write('\r\n')


class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')


if __name__ == '__main__':
    log_file = LogFileMixin()
    log_file.log_error('Falha no log')
    log_file.log_success('Log Success')

    log_print = LogPrintMixin()
    log_print.log_error('Falha no Log Print')
    log_print.log_success('Success Log Print')