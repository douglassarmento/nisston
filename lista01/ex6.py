n = int (input ('Digite um número:'))
num = n
v = 1
while num >= 1:
    f = v*num
    v = f
    num -= 1
print (f'O fatorial de {n} é {v}.')