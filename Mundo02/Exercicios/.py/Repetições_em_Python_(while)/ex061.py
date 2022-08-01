print('Gerenciador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razâo = int(input('Razâo da PA: '))
termo = 1
cont = 1
while cont <=10:
    print('{} -> '.format(termo), end='')
    termo += razâo
    cont += 1
print('FIM')