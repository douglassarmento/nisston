nomes = []
for x in range(5):
    nome = input('Digite um nome: ').strip().lower()
    if nome.startswith('a'):
        nomes.append(nome)
        nomes_formatados = ', '.join(nomes)
print(f'Os nomes que começam com "A" são: {nomes_formatados}.')