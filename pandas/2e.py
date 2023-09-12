import pandas as pd

df = pd.read_csv('conserto.csv')

df['DataSaida'] = pd.to_datetime(df['DataSaida'])

df_ano_2006 = df[df['DataSaida'].dt.year == 2006]

ocorrencias_servicos_2006 = df_ano_2006['Servico'].value_counts()

top_5_servicos_2006 = ocorrencias_servicos_2006.head(5)

print("Os 5 serviços mais realizados em 2006, com base na Data de Saída, são:\n", top_5_servicos_2006)