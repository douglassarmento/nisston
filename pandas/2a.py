import pandas as pd

df = pd.read_csv('conserto.csv')

num_linhas = df.shape[0]

print("O arquivo 'conserto.csv' possui", num_linhas, "linhas.")