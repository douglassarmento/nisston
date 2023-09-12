import pandas as pd

df = pd.read_csv("carro.csv")

carros_ano_2005 = df[df['AnoFab'] == 2005]

quantidade_carros_ano_2005 = len(carros_ano_2005)

print(f"Quantidade de carros com ano de fabricação igual a 2005: {quantidade_carros_ano_2005}")