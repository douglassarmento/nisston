class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
    
    def detalhes(self):
        return f"Título: {self.titulo}\nAutor: {self.autor}"

titulo_do_livro = "Dom Quixote"
autor_do_livro = "Miguel de Cervantes"
livro = Livro(titulo_do_livro, autor_do_livro)
informacoes_do_livro = livro.detalhes()
print(informacoes_do_livro)