n = int(input('Digite um número para calcular: '))
print('-=' * 12)
for i in range(1, 11):
    print('{} * {} = {}'.format(n, i, n * i))
print('=-' * 12)