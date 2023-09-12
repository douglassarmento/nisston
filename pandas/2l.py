import pandas as pd

df = pd.read_csv('conserto.csv')

df['DataSaida'] = pd.to_datetime(df['DataSaida'])

df_ano_2004 = df[df['DataSaida'].dt.year == 2004]

df_ano_2004['Mes'] = df_ano_2004['DataSaida'].dt.month

faturamento_por_mes_2004 = df_ano_2004.groupby('Mes')['ValorServico'].sum()

print("O faturamento por mês com base na Data de Saída do ano de 2004 é:\n", faturamento_por_mes_2004)