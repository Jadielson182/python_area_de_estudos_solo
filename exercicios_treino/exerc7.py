# Crie uma classe Agenda que permita adicionar contatos,
#  remover contatos e listar todos os contatos. Cada contato deve ter um nome e um número de telefone.



class Contato:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone
        

class Agenda(Contato):
    def __init__(self):
        # super().__init__(nome, telefone)
        self.lista_contato = []
    
    def adiciona_contato(self, *contato):
        self.lista_contato.append(*contato)


    def remover_contato(self, nome):
        deletar = nome
        if deletar in self.lista_contato:
            self.lista_contato.remove(nome)

            
    
    def listar_contatos(self):
        for contato in self.lista_contato:
            print(f'{contato.nome!r} - {contato.telefone!r}')

    def __repr__(self):
        class_name = type(self).__name__
        formatacao = f'{self.nome!r}, {self.telefone!r}'
        return f'{class_name}, ({formatacao})'


if __name__ == '__main__':
    agenda = Agenda()
    contato_1 = Contato('Jadielson', '8195241546') 
    contato_2 = Contato('Joao', '8145675878')   
    contato_3 = Contato('Helena', '8136498754')   
    contato_4 = Contato('Carlos', '8154895627')   
    contato_5 = Contato('Maria', '8154872354') 
    agenda.adiciona_contato(contato_1)
    agenda.adiciona_contato(contato_2)
    agenda.adiciona_contato(contato_3)
    agenda.adiciona_contato(contato_4)
    agenda.adiciona_contato(contato_5)
    agenda.remover_contato(contato_1)
    agenda.remover_contato(contato_2)

    agenda.listar_contatos()