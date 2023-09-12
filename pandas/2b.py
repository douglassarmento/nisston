import pandas as pd

df = pd.read_csv('conserto.csv')

ocorrencias_mecanicos = df['Mecanico'].value_counts()

top_10_mecanicos = ocorrencias_mecanicos.head(10)

print("Os 10 mecânicos com maior ocorrência são:\n", top_10_mecanicos)