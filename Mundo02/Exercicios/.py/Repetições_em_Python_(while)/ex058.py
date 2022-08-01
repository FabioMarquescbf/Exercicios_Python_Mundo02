import random
print('sou seu computador')
print('''Acabei de pensar em um número entre 0 e 10.
será que você consegue adivinhar qual foi?''')
computador = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,)
computador = random.choice(computador)
acertou = 0
palpite = int(input('Qual seu palpite? '))
while palpite != computador:
    acertou += 1
    if computador > palpite:
        print('Mais.. Tente novamente')
        palpite = int(input('Qual seu palpite?'))
    elif computador < palpite:
        print('menos... Tente novamente')
        palpite = int(input('Qual seu palpite?'))
if palpite == computador:
        print('Você acertou com {} palpites. Parabéns!'.format(acertou))
