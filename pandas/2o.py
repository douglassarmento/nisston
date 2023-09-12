import pandas as pd

df = pd.read_csv('conserto.csv')

oficina_penha_mecanicos = df[df['Oficina'] == 'OFICINA NOSSA SENHORA DA PENHA']

mecanicos_penha = oficina_penha_mecanicos['Mecanico'].unique()

print("Os mecânicos da oficina 'OFICINA NOSSA SENHORA DA PENHA' são:")
for mecanico in mecanicos_penha:
    print(mecanico)
