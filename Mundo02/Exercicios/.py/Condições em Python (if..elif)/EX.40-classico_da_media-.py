# Crie um programa que leia duas notas de um aluno e calcule sua média.
# mostrando uma mensagem no final, de acordo com a média atingida:

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
print(f'Tirando {n1} e {n2}, a media do aluno é {media}')
if media < 5:
    print('O aluno está REPROVADO')
elif 7 > media >= 5 :
    print('O aluno está em RECUPERAÇÃO')
elif media > 7:
    print('O aluno está APROVADO')