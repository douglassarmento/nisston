n1 = 0
n2 = 1
n3 = 0
fibonnaci = []

n = int(input('Digite um número: '))

if n == 0:
    fibonnaci = [0]
elif n == 1:
    fibonnaci = [0, 1]
else:
    fibonnaci = [0, 1]
    while n3 <= n:
        n3 = n1 + n2
        if n3 <= n:
            fibonnaci.append(n3)
        n1 = n2
        n2 = n3

print(f'A sequência de Fibonacci é: {fibonnaci}.')