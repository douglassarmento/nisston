import pandas as pd

df = pd.read_csv("carro.csv")

carros_celta = df[df['Modelo'] == 'CELTA']

anos_fabricacao_carros_celta = carros_celta['AnoFab'].unique()

print("Anos de fabricação dos carros do modelo CELTA:")
for ano in anos_fabricacao_carros_celta:
    print(ano)