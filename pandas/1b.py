import pandas as pd

df = pd.read_csv("carro.csv")

combustiveis = df['Combustivel'].unique()

print("Combustíveis cadastrados:")
for combustivel in combustiveis:
    print(combustivel)