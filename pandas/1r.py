import pandas as pd

df = pd.read_csv("carro.csv")

carros_verde = df[df['Cor'] == 'VERDE']

print("Carros da cor Verde:")
print(carros_verde)