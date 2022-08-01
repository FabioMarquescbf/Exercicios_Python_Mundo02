print('-' * 40)
print('          LOJA SUPER BARATÃO')
print('-' * 40)
total = totmil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço do produto: R$'))
    total += preço
    cont += 1
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if preço > 1000:
        totmil += 1
    if cont == 1:
        menor = preço
        barato = produto
    if preço < menor:
        menor = preço
        barato = produto
    elif continuar == 'N':
        break
print('---------- FIM DO PROGRAMA ----------')
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')
