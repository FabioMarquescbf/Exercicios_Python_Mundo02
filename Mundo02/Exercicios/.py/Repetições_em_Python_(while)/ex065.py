print('-' * 80)
print('DIGITE VALORES PARA SABER A QUANTIDADE, A MÉDIA, O MENOR E O MAIOR VALOR.')
print('-' * 80)
resp = 'S'
soma = quant = media = maior = menos = 0
while resp in 'Ss':
    n = int(input('Digite um número: '))
    soma += n
    quant += 1
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior =  n
        if n < menor:
            menor = n
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma / quant
print('Você digitou {} números e a média foi {}.'.format(quant, media))
print('O maior valor foi {} e o menor valor foi {}'.format(maior, menor))
print('FIM!')
