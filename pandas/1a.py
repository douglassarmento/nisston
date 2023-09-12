import pandas as pd

df = pd.read_csv("carro.csv")

total_carros = len(df)

print("Quantidade de carros cadastrados:", total_carros)