
class CallMe:
    def __init__(self, phone):
        self.phone = phone

    
    def __call__(self, name):
        print(name, 'está chamando', self.phone)
        return 1254


call_1 = CallMe('92584553')
retorno = call_1('Luiz Otávio')
print(retorno)


