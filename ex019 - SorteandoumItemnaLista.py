'''Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele,
 lendo o nome dos alunos e escrevendo na tela o nome do escolhido.'''

import random
a1 = input('Digite o primeiro aluno:')
a2 = input('Digite o segundo aluno:')
a3 = input('Digite o terceiro aluno: ')
a4 = input('Digite o quarto aluno: ')
lista = [a1,a2,a3,a4]
escolhido = random.choice(lista)
print('O computador sorteou o aluno {} para apagar o quadro'.format(escolhido))
