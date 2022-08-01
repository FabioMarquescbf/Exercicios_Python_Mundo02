print('-' * 52)
print('DIGITE UM VALOR PARA SABER A QAUNTIDADE E A SOMA!')
print('-' * 52)
quant = soma = 0
while True:
    n = int(input('Digite um valor [999 para parar): '))
    if n == 999:
        break
    quant += 1
    soma += n
print(f'A soma dos {quant} valores foi {soma}!')

