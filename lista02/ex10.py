class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo
    
    def aumentar_salario(self, percentual):
        if percentual > 0:
            aumento = self.salario * percentual / 100
            self.salario += aumento
            print(f"Salário de {self.nome} atualizado para R${self.salario:.2f}")
        else:
            print("O percentual de aumento deve ser maior que zero.")

nome_do_funcionario = "Douglas"
salario_do_funcionario = 1200
cargo_do_funcionario = "Desenvolvedor"
funcionario = Funcionario(nome_do_funcionario, salario_do_funcionario, cargo_do_funcionario)
percentual_de_aumento = 5
funcionario.aumentar_salario(percentual_de_aumento)