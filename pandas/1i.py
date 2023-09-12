import pandas as pd

df = pd.read_csv("carro.csv")

contagem_por_marca = df['Marca'].value_counts()

marca_mais_carros = contagem_por_marca.idxmax()
quantidade_mais_carros = contagem_por_marca.max()

print(f"A marca com mais carros cadastrados é '{marca_mais_carros}' com {quantidade_mais_carros} carros.")