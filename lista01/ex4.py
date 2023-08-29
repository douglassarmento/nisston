maior = 0
menor = 0
for n in range (0, 5):
    n = float (input ())
    if n > maior:
        maior = n
        if menor == 0:
            menor = n
        else:
            menor = menor
    elif n > menor:
        if menor == 0:
            menor = n
        else:
            menor = menor
    else:
        menor = n       
print (f'O maior número é {maior}. O menor número é {menor}.')