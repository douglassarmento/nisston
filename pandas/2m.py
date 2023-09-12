import pandas as pd

df = pd.read_csv('conserto.csv')

df['DataSaida'] = pd.to_datetime(df['DataSaida'])

oficina_penha_2004 = df[(df['Oficina'] == 'OFICINA NOSSA SENHORA DA PENHA') & (df['DataSaida'].dt.year == 2004)]

oficina_penha_2004['Mes'] = oficina_penha_2004['DataSaida'].dt.month

faturamento_por_mes_penha_2004 = oficina_penha_2004.groupby('Mes')['ValorServico'].sum()

print("O faturamento por mês da oficina 'OFICINA NOSSA SENHORA DA PENHA' no ano de 2004 é:\n", faturamento_por_mes_penha_2004)