from random import randint
v = 0
print('-=' * 30)
print('              VAMOS JOGAR PAR OU ÍMPAR')
print('-=' * 30)
while True:
    computador = randint(0, 10)
    jogador = int(input('Digite um valor: '))
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {total} ', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU')
    print('Vamos Jogar novamente...')
print(f'GAME OVER! Voc|Ê venceu {v} vezes.')