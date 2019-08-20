'''073: Crie uma tupla preenchida com os 20 primeiros colocados
   da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação.
   Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.'''

times = ('Internacional','São Paulo','Palmeiras','Flamengo',
         'Gremio','Atlético','Cruzeiro','Corinthians',
         'America-MG','Santos','Bahia','Fluminense',
         'Atletico-PR','EC Vitoria','Botafogo','Vasco da Gama',
         'Sport Recife','Ceara SC','Chapecoense','Paraná')
print('Os 5 primeiros times são {}'.format(times[:5]))
print('Os ultimos 4 colocados são {}'.format(times[-4:]))
print('A tabela em ordem alfabetica {}'.format(sorted(times)))
print('O time da Chapecoense esta na {}ª posição'.format(times.index('Chapecoense')+1))