class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def falar(self):
        print(f"Olá, meu nome é {self.nome}.")

nome_da_pessoa = "Alice"
idade_da_pessoa = 30
pessoa = Pessoa(nome_da_pessoa, idade_da_pessoa)
pessoa.falar()