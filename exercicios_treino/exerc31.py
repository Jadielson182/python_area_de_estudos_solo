# Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:

# Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
# tipoCombustivel.
# valorLitro
# quantidadeCombustivel
# Possua no mínimo esses métodos:
# abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi colocada no veículo
# abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo cliente.
# alterarValor( ) – altera o valor do litro do combustível.
# alterarCombustivel( ) – altera o tipo do combustível.
# alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.
# OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba.

class BombaDeCombustivel:
    def __init__(self, tipo_combustivel, valor_litro, quantidade_combustivel):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel

    
    def valor_do_abastecimento(self, valor):
        """
        método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi colocada no veículo
        """
        abastecimento = valor / self.valor_litro
        return f'O valor a ser abastecido é de R${valor:.2f}\nSera abastecido {abastecimento:.1f} litros de {self.tipo_combustivel}.'
        

    def abastecer_por_litro(self, quantidade):
        """
        método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo cliente.
        """
        valor_total = quantidade * self.valor_litro
        self.quantidade_combustivel -= quantidade
        return f'A quantidade informada foi {quantidade} litros de {self.tipo_combustivel}\nO valor do abastecimento sera R${valor_total:.2f}'

    def alterar_preco(self, valor):
        """
        altera o valor do litro do combustível.
        """
        self.valor_litro = valor

    def tipo_combustivel(self, tipo):
        """
        altera o tipo do combustível.
        """
        self.tipo_combustivel = tipo

    
    def quantidade_de_combustivel_bomba(self):
        """
        altera a quantidade de combustível restante na bomba.
        """
        print(f'Temos {self.quantidade_combustivel} litros de {self.tipo_combustivel} na Bomba.')
        
    
bomba_1 = BombaDeCombustivel('Gasolina', 5.60, 100 )
bomba_2 = BombaDeCombustivel('Diesel', 5.70, 100)
print(bomba_1.abastecer_por_litro(50))
bomba_1.quantidade_de_combustivel_bomba()
print()
print(bomba_2.abastecer_por_litro(45))
bomba_2.quantidade_de_combustivel_bomba()
