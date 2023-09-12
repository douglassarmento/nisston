import pandas as pd

df = pd.read_csv("carro.csv")

contagem_por_combustivel = df['Combustivel'].value_counts()

combustivel_mais_carros = contagem_por_combustivel.idxmax()
quantidade_mais_carros = contagem_por_combustivel.max()

print(f"O tipo de combustível com mais carros cadastrados é '{combustivel_mais_carros}' com {quantidade_mais_carros} carros.")