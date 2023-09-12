import pandas as pd

df = pd.read_csv('conserto.csv')

df['DataSaida'] = pd.to_datetime(df['DataSaida'])

df_ano_2004 = df[df['DataSaida'].dt.year == 2004]

ocorrencias_por_mes_2004 = df_ano_2004['DataSaida'].dt.month.value_counts()

mes_com_maior_ocorrencia_2004 = ocorrencias_por_mes_2004.index[0]

print("O mês com maior ocorrência de registros em 2004, com base na Data de Saída, foi o mês", mes_com_maior_ocorrencia_2004)