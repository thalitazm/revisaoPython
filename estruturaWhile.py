# -*- coding: utf-8
#Estrutura While

numero = 1
while numero < 6:
    print(numero)
    numero += 1
print('---')

numero = 5
while numero > 0:
    print(numero)
    numero -= 1
print('---')

soma = 0
numero = 1
while numero < 6:
    soma += numero
    print(soma)
    numero += 1
print(soma)

numero = -1
while numero < 1 or numero > 10:
    numero = int(input('Digite um número de 1 a 10: '))