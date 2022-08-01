from math import factorial
n = int(input('Digite um número para  calcular seu Fatorial: '))
f  = factorial(n)
print('O fatorial de {} é {}.'.format(n, f))

print('=-' * 15)

n = int(input('Digite um númeor para calcular seu Fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c != 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('O fatorial de {} é {}.'.format(n, f))