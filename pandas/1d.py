import pandas as pd

df = pd.read_csv("carro.csv")

ano_fabricacao_mais_antigo = df['AnoFab'].min()

print("Ano de fabricação mais antigo:", ano_fabricacao_mais_antigo)