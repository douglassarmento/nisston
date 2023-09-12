import pandas as pd

df = pd.read_csv("carro.csv")

cores = df['Cor'].unique()

print("Cores cadastradas:")
for cor in cores:
    print(cor)