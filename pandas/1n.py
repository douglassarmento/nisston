import pandas as pd

df = pd.read_csv("carro.csv")

carros_ano_2004 = df[df['AnoFab'] == 2004]

print("Carros com ano de fabricação igual a 2004:")
print(carros_ano_2004)