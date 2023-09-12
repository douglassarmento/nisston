import pandas as pd

df = pd.read_csv('conserto.csv')

df['DataSaida'] = pd.to_datetime(df['DataSaida'])

df_ano_2006 = df[df['DataSaida'].dt.year == 2006]

ocorrencias_responsaveis_2006 = df_ano_2006['Responsavel'].value_counts()

responsavel_com_maior_ocorrencia_2006 = ocorrencias_responsaveis_2006.index[0]

print("O responsável com maior ocorrência em 2006, com base na Data de Saída, foi:", responsavel_com_maior_ocorrencia_2006)