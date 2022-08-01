from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    nac = int(input('Em que ano a {} pessoa nasceu? '.format(pess)))
    idade = atual - nac
    if idade >=21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tívemos {} pessoas maiores de idade'.format(totmaior))
print('Ao todo tivemos {} pessoas menores de idade'.format(totmenor))
