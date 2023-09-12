import pandas as pd

df = pd.read_csv("carro.csv")

carros_honda = df[df['Marca'] == 'HONDA']

instrutores_honda = carros_honda['idinstrutor'].unique()

print("idinstrutor com carros da marca Honda:")
print(instrutores_honda)