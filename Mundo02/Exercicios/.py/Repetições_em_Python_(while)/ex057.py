sexo = 1
sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos. Por favor, informe seu sexo corretamente: ')).strip().upper()[0]
print('Sexo {} registrado com secesso.'.format(sexo))