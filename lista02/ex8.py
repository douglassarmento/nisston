class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas
    
    def calcular_media(self):
        if len(self.notas) > 0:
            media = sum(self.notas) / len(self.notas)
            return media
        else:
            return 0

nome_do_aluno = "Douglas"
notas_do_aluno = [8.5, 7.2, 9.0, 6.8]
aluno = Aluno(nome_do_aluno, notas_do_aluno)
media_do_aluno = aluno.calcular_media()
print(f"A média do aluno {nome_do_aluno} é {media_do_aluno:.2f}")