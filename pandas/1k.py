import pandas as pd

df = pd.read_csv("carro.csv")

carros_combustivel_diesel = df[df['Combustivel'] == 'Diesel']

print("Carros cadastrados com combustível Diesel:")
print(carros_combustivel_diesel)