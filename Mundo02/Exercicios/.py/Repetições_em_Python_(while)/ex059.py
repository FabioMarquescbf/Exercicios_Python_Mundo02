from time import sleep
v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))
opç = 1
while opç != 5:
        print('''        [ 1 ] Somar
        [ 2 ] Multiplicar
        [ 3 ] maior
        [ 4 ] novos números
        [ 5 ] sair do programa''')
        opç = int(input('>>>> Qual é a sua opção? '))
        if opç == 1:
                print('A soma entre {} + {} é {}'.format(v1, v2, v1 + v2))
        elif opç == 2:
                print('O resultado de {} x {} é {}'.format(v1, v2, v1 * v2))
        elif opç == 3:
                if v1 > v2:
                        print('entre {} e {} o maior valor é {}'.format(v1, v2, v1))
                elif v2 > v1:
                        print('entre {} e {} o maior numero é {}'.format(v1, v2, v2))
        elif opç == 4:
                print('Informe os números novamente:')
                v1 = int(input('Primeiro número: '))
                v2 = int(input('Segundo número: '))
        elif opç == 5:
                print('finalizando...')
                sleep(2)
                print('Fim do programa! Volte sempre!')
        else:
                print('Opção invalida tente novamente')
        print('=-=' * 8)
        sleep(2)

