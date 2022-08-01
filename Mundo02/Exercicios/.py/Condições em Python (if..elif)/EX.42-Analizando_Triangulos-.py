# Refaça o DESAFIO 35 dos triângulos.
# acrescentando o recurso de mostrar que tipo de triângulo será formado:

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print('Os seguimentos acima podem forma um triângulo ', end='')
    if r1 == r2 == r3:
       print('EQUILATERO!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Os seguimentos acima NÃO PODEM FORMA Triângulo!')
