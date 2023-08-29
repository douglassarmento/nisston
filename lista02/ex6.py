class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
    
    def calcular_total(self):
        return self.preco * self.quantidade

nome_do_produto = "Camiseta"
preco_do_produto = 25.99
quantidade_do_produto = 3
produto = Produto(nome_do_produto, preco_do_produto, quantidade_do_produto)
total_do_produto = produto.calcular_total()
print(f"O total do produto '{nome_do_produto}' é R${total_do_produto:.2f}")