import pandas as pd

df = pd.read_csv("carro.csv")

quantidade_por_ano = df['AnoFab'].value_counts()

print("Quantidade de carros por ano de fabricação:")
print(quantidade_por_ano)