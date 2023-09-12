import pandas as pd

df = pd.read_csv('conserto.csv')

servicos_realizados_pelo_piloto = df[df['Mecanico'] == 'Piloto']

top_10_servicos_piloto = servicos_realizados_pelo_piloto['Servico'].value_counts().head(10)

print("Os 10 serviços realizados pelo mecânico 'Piloto' são:")
print(top_10_servicos_piloto.index)