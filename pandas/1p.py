import pandas as pd

df = pd.read_csv("carro.csv")

categorias_unicas = df['Categoria'].unique()

print("Tipos de categorias cadastrados:")
for categoria in categorias_unicas:
    print(categoria)