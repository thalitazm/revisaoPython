# -*- coding: utf-8
#Estrutura For:

print(1)
print(2)
print(3)
print(4)
print(5)
print('---')
print('---')



for numero in range(1,6): #i n range = na faixa de
    print(numero)
    print('---')
    print('---')

#imprime ao contrário:
for numero in range(5, 0, -1):
    print(numero)

soma = 0
for numero in range(1, 6):
    soma = soma + numero
    print(soma) #valor parcial da soma
print(soma)
print('---')
print('---')



palavra = 'sorvete'
for letra in palavra:
    #print(letra)
    if letra == 'v':
        print('Achou a letra v')
        print('---')
        print('---')


# for aninhado:
for i in range (0,5):
    print(i)
    print('---')
    for j in range(0,3):
        print(j)
    print()