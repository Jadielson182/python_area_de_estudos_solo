class Publico:
    def __init__(self):
        self.public = 'Isso e Público'
        self._protected = 'Isso e protegido'
        self.__private = 'Isso e privado'

    
    def method_public(self):
        self.__method_private()
        print('Method public')
        return 'metodo público'

    def _method_protected(self):
        print('Method Protected')
        return 'Isso e protegido'


    def __method_private(self):
        print('Method Private')
        return 'Isso é privado'


    
pu = Publico()
print(pu.public)
print(pu._protected)
print(pu._method_protected())
print(pu._Publico__method_private())
print(pu.method_public())

