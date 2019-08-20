'''101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento
   de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO
   nas eleições.'''

def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'com {idade} anos: Não Vota'
    elif 16 >= idade < 18:
        return f'com {idade} anos: Voto é Opcional'
    else:
        return f'com {idade} anos: O voto é Obrigatorio'

nasc = int(input('Em que ano vc nasceu?: '))
print(voto(nasc))