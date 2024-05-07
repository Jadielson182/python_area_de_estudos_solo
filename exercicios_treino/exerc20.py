
# Crie uma metaclass chamada SingletonMeta que permita que uma classe tenha apenas uma instância.

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class MinhaClasse(metaclass=SingletonMeta):
    pass

# Exemplo de uso:
instancia1 = MinhaClasse()
instancia2 = MinhaClasse()
print(instancia1 is instancia2)  # Saída esperada: True
