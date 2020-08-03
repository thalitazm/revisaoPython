# -*- coding: utf-8
#Exercício 01:

#for
nota = media = soma = 0
print(nota, media, soma)

for _ in range(1,6):
    nota = float(input('Digite a nota: '))
    soma += nota
print(soma)

media = soma/5
print('A media é: ', media)
print()

#mesmo exercício com while:
nota = soma = 0
numero = 1
while numero <=5:
    nota = float(input('Informe a nota: '))
    soma += nota
    numero += 1
print('A media é ', soma / 5)
print()

#Exercício 02:
#for

for i in range(1, 11):
    print('3 x {}'.format(i, 3 * i))

#while:
numero = 1
while numero <= 10:
    print('3 x {} = {}'.format(numero, 3 * numero))
    numero += 1