''' 069: Crie um programa que leia a idade e o sexo de várias pessoas.
    A cada pessoa cadastrada, o programa deverá perguntar se o usuário
    quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos. '''
maior18 = cadhomens = menor20 = cont = mulher = homem = 0
while True:
    print('-'*20)
    print('Dados Cadastrais')
    print('-'*20)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if idade > 18:
        maior18 += 1
        #print(f'{cont} pessoas tem mais de 18 anos')
    if idade < 20 and sexo == 'F':
        menor20 += 1
    if sexo == 'M':
        homem += 1
    perg = ' '
    if perg not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if resp == 'N':
            break
print(f'{maior18} pessoas tem mais de 18 anos')
print(f'Temos um total de {menor20} mulheres com menos de 20 anos')
print(f'Temos um total de {homem} homens cadastrados')
print('Acabou!!!')

