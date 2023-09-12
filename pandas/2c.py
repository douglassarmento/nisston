import pandas as pd

df = pd.read_csv('conserto.csv')

df['DataEntrada'] = pd.to_datetime(df['DataEntrada'])

df_ano_2006 = df[df['DataEntrada'].dt.year == 2006]

ocorrencias_mecanicos_2006 = df_ano_2006['Mecanico'].value_counts()

mecanico_mais_ocorrencias_2006 = ocorrencias_mecanicos_2006.index[0]

print("O mecânico com maior ocorrência em 2006 foi:", mecanico_mais_ocorrencias_2006)