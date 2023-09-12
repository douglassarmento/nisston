import pandas as pd

df = pd.read_csv("carro.csv")

contagem_por_instrutor = df['idinstrutor'].value_counts()

codigo_instrutor_mais_ocorrencias = contagem_por_instrutor.idxmax()
quantidade_mais_ocorrencias = contagem_por_instrutor.max()

print(f"O código de instrutor com mais ocorrências é '{codigo_instrutor_mais_ocorrencias}' com {quantidade_mais_ocorrencias} ocorrências.")