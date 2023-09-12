import pandas as pd

df = pd.read_csv('conserto.csv')

troca_de_pneus_mecanicos = df[df['Servico'] == 'Troca de Pneus']

mecanicos_troca_de_pneus = troca_de_pneus_mecanicos['Mecanico'].unique()

print("Os mecânicos que realizaram o serviço de 'Troca de Pneus' são:")
for mecanico in mecanicos_troca_de_pneus:
    print(mecanico)
