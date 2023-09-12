import pandas as pd

df = pd.read_csv('conserto.csv')

oficina_uchoa = df[df['Oficina'] == 'MECANICA UCHOA']

faturamento_uchoa = oficina_uchoa['ValorServico'].sum()

print("O faturamento da oficina 'MECANICA UCHOA' foi de R$", faturamento_uchoa)