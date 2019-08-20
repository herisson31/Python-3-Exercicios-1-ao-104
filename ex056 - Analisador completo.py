'''056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
   No final do programa, mostre: a média de idade do grupo,
    qual é o nome do homem mais velho e
    quantas mulheres têm menos de 20 anos.'''

media = totalmedia = MaiorIdade = nomemaisVelho = menosVinte = 0
for c in range(1,5):
    print('Digite os dados da {:-^}ª pessoa'.format(c))
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo: ')
    media += idade
    totalmedia = media / 4
    if c == 1 and sexo in 'Mm':
        MaiorIdade = idade
        nomemaisVelho = nome
    if sexo in 'Mm' and idade > MaiorIdade:
        MaiorIdade = idade
        nomemaisVelho = nome
    if sexo in 'Ff' and idade < 20:
        menosVinte += 1
print('A média da idade do Grupo é {} '.format(totalmedia))
print('O home mais velho se chama {} tem {} anos'.format(nomemaisVelho,MaiorIdade))
print('Tem o total de {} mulheres com menos de 20 anos'.format(menosVinte))