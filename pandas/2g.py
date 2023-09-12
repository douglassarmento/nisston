import pandas as pd

df = pd.read_csv('conserto.csv')

df['DataSaida'] = pd.to_datetime(df['DataSaida'])

df_ano_2005 = df[df['DataSaida'].dt.year == 2005]

media_por_mes_2005 = df_ano_2005.groupby(df_ano_2005['DataSaida'].dt.month)['ValorServico'].mean()

print("A média por mês dos valores pagos no ano de 2005, com base na Data de Saída, é:\n", media_por_mes_2005)