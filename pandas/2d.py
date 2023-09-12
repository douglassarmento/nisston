import pandas as pd

df = pd.read_csv('conserto.csv')

ocorrencias_servicos = df['Servico'].value_counts()

top_10_servicos = ocorrencias_servicos.head(10)

print("Os 10 serviços mais realizados são:\n", top_10_servicos)