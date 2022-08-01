print('Gerenciador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razâo = int(input('Razâo da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razâo
        cont += 1
    print('pausa')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão realizada com {} termos mostrados.'.format(total))
