# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input('Valor da casa: R$ '))
salario = float(input('Salário do comprador: R$ '))
anos = int(input('Quantos anos de financiamento: R$ '))
prestação = casa / (anos * 12)
psalario = salario * 30 / 100
if prestação <= psalario:
    print(f'Para pagar uma casa de R${casa} em {anos} anos a prestação será de R${prestação}')
    print('Empréstimo CONCEDIDO!')
else:
    print(f'Para pagar uma casa de R${casa} em {anos} anos a prestação será de R${prestação}')
    print('Emprestimo pode ser NEGADO!')

# Teste