
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco



class Carrinho:
    def __init__(self):
        self._produtos = []


    def total(self):
        return sum([p.preco for p in self._produtos])

    
    def inserir_produtos(self, *produtos):
        # self._produtos += produtos
        # self._produtos.extend(produtos)
        for produto in produtos:
            self._produtos.append(produto)


    def listar_produtos(self):
        for produto in self._produtos:
            print(produto.nome, produto.preco)


carrinho = Carrinho()
produto_1, produto_2 = Produto('caneta', 1.20), Produto('camiseta', 20)
carrinho.inserir_produtos(produto_1, produto_2)
carrinho.listar_produtos()
print(carrinho.total())