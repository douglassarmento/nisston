class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
    def detalhes(self):
        return f"Marca: {self.marca}\nModelo: {self.modelo}\nAno: {self.ano}"

marca_do_carro = "Toyota"
modelo_do_carro = "Corolla"
ano_do_carro = 2022
carro = Carro(marca_do_carro, modelo_do_carro, ano_do_carro)
informacoes_do_carro = carro.detalhes()
print(informacoes_do_carro)