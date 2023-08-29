from random import choice
j = int (input ('[1] PEDRA - [2] PAPEL - [3] TESOURA: '))
pedra = 1; papel = 2; tesoura = 3
lista = [pedra, papel, tesoura]
c = choice (lista)
if j == 1 and c == 3 or j == 2 and c == 1 or j == 3 and c == 2:
    print (f'{j} > {c}. VOCÊ GANHOU.')
elif j == 1 and c == 1 or j == 2 and c == 2 or j == 3 and c == 3:
    print (f'{j} = {c}. EMPATE.')
else:
    print (f'{j} < {c}. VOCÊ PERDEU.')