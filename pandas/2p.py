import pandas as pd

df = pd.read_csv('conserto.csv')

servicos_toinho_piloto = df[df['Mecanico'].isin(['Toinho', 'Piloto'])]

soma_valores_servico_toinho_piloto = servicos_toinho_piloto.groupby('Mecanico')['ValorServico'].sum()

print("Os valores pagos pelos serviços realizados pelos mecânicos Toinho e Piloto são:")
print(soma_valores_servico_toinho_piloto)
