class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        return self.base * self.altura

base_do_retangulo = 8
altura_do_retangulo = 5
retangulo = Retangulo(base_do_retangulo, altura_do_retangulo)
area_do_retangulo = retangulo.calcular_area()
print(f"A área do retângulo é {area_do_retangulo}")