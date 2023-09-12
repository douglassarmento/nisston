import pandas as pd

df = pd.read_csv("carro.csv")

ano_fabricacao_mais_novo = df['AnoFab'].max()

print("Ano de fabricação mais novo:", ano_fabricacao_mais_novo)