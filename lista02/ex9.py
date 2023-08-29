class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    
    def calcular_perimetro(self):
        return self.lado1 + self.lado2 + self.lado3

lado1_do_triangulo = 5
lado2_do_triangulo = 7
lado3_do_triangulo = 9
triangulo = Triangulo(lado1_do_triangulo, lado2_do_triangulo, lado3_do_triangulo)
perimetro_do_triangulo = triangulo.calcular_perimetro()
print(f"O perímetro do triângulo é {perimetro_do_triangulo}")