s = 0
q = 0
for n in range (0, 5):
    n = int (input ())
    if n%2 == 0:
        s += n
        q += 1
        print ('Este número é par.')
    else:
        print ('Este número é ímpar.')
print (f'A média dos números pares é {s/q}.')