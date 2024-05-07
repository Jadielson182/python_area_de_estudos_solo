from abc import ABC, abstractmethod

class Notificacao(ABC):
    def __init__(self, mensagem):
        self.mensagem = mensagem

    @abstractmethod
    def enviar(self)-> bool: ...


class NotificacaoEmail(Notificacao):
    def enviar(self)-> bool:
        print('Email: enviando -', self.mensagem)
        return True


class NotificacaoSms(Notificacao):
    def enviar(self)-> bool:
        print('SMS: enviando - ',self.mensagem )
        return False


def notificar(mensagem:Notificacao):
    notiicacao_enviada = mensagem.enviar()
    if notiicacao_enviada:
        print('Notificação enviada')
    else:
        print('Notificação Nâo enviada')


notificacao_email = NotificacaoEmail('Testando Email')
notificar(notificacao_email)

notificacao_sms = NotificacaoSms('Testando SMS')
notificar(notificacao_sms)