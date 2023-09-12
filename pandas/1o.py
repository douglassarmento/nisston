import pandas as pd

df = pd.read_csv("carro.csv")

contagem_por_veiculo = df['Veiculo'].value_counts()

veiculo_mais_ocorrencias = contagem_por_veiculo.idxmax()
quantidade_mais_ocorrencias = contagem_por_veiculo.max()

print(f"O veículo com mais ocorrências é '{veiculo_mais_ocorrencias}' com {quantidade_mais_ocorrencias} ocorrências.")