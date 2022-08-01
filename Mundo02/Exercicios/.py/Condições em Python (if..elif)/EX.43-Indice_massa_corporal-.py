# Desenvolva uma lógica que leia o peso e a altura de uma pessoa.
# calcule seu Índice de Massa Corporal (IMC).
# e mostre seu status, de acordo com a tabela abaixo:

peso = float(input('Qual é seu peso? (Kg) '))
altura = float(input('Qual é sua altura> (m) '))
imc = peso / (altura ** 2)
if imc <= 18.5:
    print('ABAIXO DO PESO!!')
elif imc > 18.5 and imc <= 25:
    print('PESO IDEIAL!!')
elif imc > 25 and imc <= 30:
    print('SOBREPESSO!!')
elif imc >= 30 and imc < 40:
    print('OBESIDADE!!')
elif imc >= 40:
    print('OBESIDADE MÔRDIDA')
