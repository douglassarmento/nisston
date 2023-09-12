import pandas as pd

df = pd.read_csv('conserto.csv')

df['DataSaida'] = pd.to_datetime(df['DataSaida'])

anos_presentes = df['DataSaida'].dt.year.unique()

print("Os anos presentes no arquivo com base na Data de Saída são:", anos_presentes)