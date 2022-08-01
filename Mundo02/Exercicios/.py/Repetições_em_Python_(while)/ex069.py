total = 0
homens = 0
mulheres = 0
print('-=' * 25)
print('            CADASTRO DE PESSOAS')
print('-=' * 25)
continuar = str(input('Quer Continuar? [S/N] '))
while continuar not in 'SsNn':
    continuar = str(input('Quer continuar? [S/N] '))
while continuar not in 'Nn':
        print('-=' * 25)
        print('            CADASTRE UMA PESSOA')
        print('-=' * 25)
        idade = int(input('Idade: '))
        sexo = ' '
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
        while sexo not in 'MF':
            sexo = str(input('Sexo: [M/F] '))
        print('-' * 50)
        continuar = str(input('Quer continuar? [S/N] '))
        while continuar not in 'SsNn':
            continuar = str(input('Quer continuar? [S/N] '))
        if sexo in 'MmFf':
            if idade >= 18:
                total += 1
        if sexo in 'Mm':
            homens += 1
        if sexo in 'Ff':
            if idade <= 20:
                mulheres += 1
print('====== FIM DO PROGRAMA ======')
print(f'Total de pessoas com mais de 18 anos: {total}')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {mulheres} mulheres com menos de 20 anos')