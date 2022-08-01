print('-' * 53)
print('            TABUADA DE VARIOS NÚMEROS')
print('-' * 53)
n = 1
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    print('-' * 53)
    for c in range(1, 11):
        print(f'{n} x {c} = {c * n}')
    print('-' * 53)
print('PROGRAMA FINALIZADO')
