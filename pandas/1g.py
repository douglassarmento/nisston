import pandas as pd

df = pd.read_csv("carro.csv")

quantidade_por_cor = df['Cor'].value_counts()

print("Quantidade de carros por cor:")
print(quantidade_por_cor)