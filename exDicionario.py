# -*- coding: utf-8
#Ex. Dicionário:

alunos = {}
for _ in range(1, 4):
    nome = input('Digite o nome: ')
    nota = float(input('Digite a nota: '))
    alunos[nome] = nota
print(alunos)

soma = 0
for nota in alunos.values():
    #print(nota)
    soma += nota
print('Media: ', soma / 3)

