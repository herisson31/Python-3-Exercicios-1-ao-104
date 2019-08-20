'''O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos.
 Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.'''
import random
n1 = input('Digite o primeiro aluno: ')
n2 = input('Digite o segundo aluno: ')
n3 = input('Digite o terceiro aluno: ')
n4 = input('Digite o quarto aluno: ')
lista = [n1,n2,n3,n4]
random.shuffle(lista)
print('A ordem de apresentaçaõ')
print(lista)