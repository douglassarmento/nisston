import pandas as pd

df = pd.read_csv('conserto.csv')

df['DataSaida'] = pd.to_datetime(df['DataSaida'])

df_ano_2006_toinho_piloto = df[(df['DataSaida'].dt.year == 2006) & (df['Mecanico'].isin(['Toinho', 'Piloto']))]

soma_valores_servico_toinho_piloto_2006 = df_ano_2006_toinho_piloto.groupby('Mecanico')['ValorServico'].sum()

print("Os valores pagos pelos serviços realizados pelos mecânicos Toinho e Piloto em 2006 são:")
print(soma_valores_servico_toinho_piloto_2006)