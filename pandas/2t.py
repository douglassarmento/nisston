import pandas as pd

df = pd.read_csv('conserto.csv')

mecanicos_wcar = df[df['Oficina'] == 'WCAR PEÇAS E SERVIÇOS']

mecanicos_wcar_unique = mecanicos_wcar['Mecanico'].unique()

print("Os mecânicos que realizaram serviço pela oficina 'WCAR PEÇAS E SERVIÇOS' são:")
for mecanico in mecanicos_wcar_unique:
    print(mecanico)