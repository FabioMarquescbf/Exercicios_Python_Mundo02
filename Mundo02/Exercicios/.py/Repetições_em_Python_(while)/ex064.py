print('-' * 80)
print('DIGITE NÚMEROS PARA SABER A QUANTIDADE E A SOMA DOS VALORES')
print('-' * 80)
n = 0
cont = 0
soma = 0
while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    if n == 999:
        print('FIM!!')
    else:
        cont += 1
        soma += n
print(f'Você digitou {cont} números, e a soma foi {soma}')

