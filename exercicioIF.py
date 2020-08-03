# -*- coding: utf-8
#Exercício 01:

idade = int(input('Digite sua idade:'))
print('Você tem', idade, 'anos')

if idade >= 0 and idade <= 12:
    print('E de acordo com a sua idade, você é uma criança')
elif idade > 12 and idade <= 18:
    print('E de acordo com a sua idade, você é um adolescente')
elif idade > 18:
    print('E de acordo com a sua idade, você é um adulto')
else:
    print('Idade inválida')

#Exercício 02:
m1 = float(input('Digite a nota da media1: '))
m2 = float(input('Digite a nota da media2: '))
m3 = float(input('Digite a nota da media3: '))

media = (m1 + m2 + m3) / 3
print('Sua media foi de: ', media)

if media >= 0.0 and media <= 4.0:
    print('Infelizmente você foi reprovado')
elif media >= 4.1 and media <= 6.0:
    exame = float(input('Digite a sua nota de exame:'))
    if exame >= 6.0:
        print('Aprovado no exame!')
    else:
        print('Infelizemente você foi reprovado no exame!')
else:
    print('Infelizmente você foi reprovado!!!')
