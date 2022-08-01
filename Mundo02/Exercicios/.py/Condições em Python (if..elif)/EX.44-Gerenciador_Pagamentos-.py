# Elabore um programa que calcule o valor a ser pago por um produto.
# considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal 
# – 3x ou mais no cartão: 20% de juros


print('=' * 11, end='')
print('LOJAS BRUNOS', end='')
print('=' * 11)

valor = float(input('Preço das compras R$ '))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
print('-'* 30)
cartão_avista = valor - (valor * 5/100)
opção = int(input('Qual é a sua opção? '))

# à vista dinheiro/cheque
if opção == 1:
    total = valor - (valor * 10/100)
    print(f'Sua compra de {valor} vai custar {total} no final.')
# à vista cartão
elif opção == 2:
    total = valor - (valor * 5/100)
    print(f'Sua compra de {valor} vai custar {total} no final')
# 2x no cartão
elif opção == 3:
    total = valor
    parcela = total / 2
    print(f'Sua compra será parcelada em 2x de R${parcela:.2f}')
    print(f'Sua compra de {valor} vai custar {valor} no final')
# 3x ou mais no cartão
elif opção == 4:
    total = valor + (valor * 20/100)
    totparcela = int(input('Quantas parcelas? '))
    parcela = total / totparcela
    print(f'Sua compra será parcelada em {totparcela} de R${parcela}')
    print(f'Sua compra de {valor} vai custar {total} no final')
# opç Invalida.
else:
    total = 0
    print('OPÇÃO INVÁLIDA DE PAGAMENTO')
