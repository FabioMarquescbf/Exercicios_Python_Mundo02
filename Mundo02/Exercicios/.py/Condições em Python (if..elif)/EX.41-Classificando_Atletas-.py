# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta.
# e mostre sua categoria, de acordo com a idade:

from datetime import date

atual = date.today().year
ano = int(input('Ano de nascimento: '))
idade = atual - ano

print(f'O atleta tem {idade} anos.')
if idade <= 9:
    print('Classificação: MIRIM')
elif idade > 9 and idade <= 14:
    print('Classificação: INFANTIL')
elif idade > 14 and idade <= 19:
    print('Classificação: JÚNIOR')
elif idade > 19 and idade <= 25:
    print('Classificação: SÊNIOR')
elif idade > 25:
    print('Classificação: MASTER')