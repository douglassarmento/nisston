import pandas as pd

df = pd.read_csv("carro.csv")

carros_celta = df[df['Modelo'] == 'CELTA']

cores_carros_celta = carros_celta['Cor'].unique()

print("Cores dos carros do modelo CELTA:")
for cor in cores_carros_celta:
    print(cor)