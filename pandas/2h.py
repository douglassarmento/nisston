import pandas as pd

df = pd.read_csv('conserto.csv')

ocorrencias_oficinas = df['Oficina'].value_counts()

oficina_mais_ocorrencias = ocorrencias_oficinas.index[0]

print("A oficina com a maior ocorrência de carros é:", oficina_mais_ocorrencias)