#Esse arquvio contém as questões da lista contextualizada 5

'''
QUESTÃO 1 - A)Realize o download dos dados de forma manual e crie uma lista e uma tupla 
com as informações disponíveis no documento CSV (coloque pelo menos 1 linha por estado e 10 
regiões de saúde diferentes, algo próximo de umas 40 linhas).
'''
# Criação da LISTA:
'''As informações serão inseridas na seguinte ordem: Região, Estado, Mmunicípio, Código da UF, Código do município, código da Regiao 
de Saúde, Nome Regiao Saude, Data, Semana, População, Casos Acumulados, Casos Novos, Óbitos Acumulados e Óbitos Novos.'''


Lista1COVID = [
    'Norte','RO','Cujubim',11,110094,11001,'VALE DO JAMARI','31/07/2020',31,25215,168,-1,5,0,
    'Norte','RO','Governador Jorge Teixeira',11,110100,11003,'CENTRAL','31/07/2020',31,7767,49,0,0,0,
    'Norte','TO','Alvorada',17,170070,17005,'ILHA DO BANANAL','31/07/2020',31,8412,171,1,2,1,
    'Norte','AC','Assis Brasil',12,120005,12001,'ALTO ACRE','31/07/2020',31,7417,316,0,6,0,
    'Norte','PA','Placas',15,150565,15002,'BAIXO AMAZONAS','31/07/2020',31,30982,277,13,4,0,
    'Norte','PA','Prainha',15,150600,15002,'BAIXO AMAZONAS','31/07/2020',31,29866,323,4,12,9,
    'Norte','RR','Cantã',14,140017,14001,'CENTRO NORTE','31/07/2020',31,18335,725,6,7,0,
    'Norte','RR','Iracema',14,140028,14002,'SUL','31/07/2020',31,11950,188,3,4,0,
    'Nordeste','MA','Afonso Cunha',21,210010,21005,'CAXIAS','31/07/2020',31,6524,131,0,2,0,
    'Nordeste','MA', 'Água Doce do Maranhão',21,210015,21006,'CHAPADINHA','31/07/2020',31,12571,569,2,5,0,
    'Nordeste','PI','Palmeirais',22,220750,22004,'ENTRE RIOS','31/07/2020',31,14539,43,7,2,0,
    'Nordeste','CE','Farias Brito',23,230430,23020,'20ª REGIÃO CRATO','31/07/2020',31,19450,606,11,8,0,
    'Nordeste','RN','Mossoró',24,240800,24002,'2ª REGIÃO DE SAÚDE - MOSSORÓ','31/07/2020',31,297378,5061,73,179,0,
    'Nordeste','PB','Damião',25,250535,25004,'4ª REGIAO','31/07/2020',31,5330,17,4,1,0,	
    'Nordeste','PE','Capoeiras',26,260380,26004,'GARANHUNS','31/07/2020',31,20048,191,8,3,0,
    'Nordeste','BA','Casa Nova',29,290720,29016,'JUAZEIRO','31/07/2020',31,71969,259,2,6,0,
    'Nordeste','AL','Dois Riachos',27,270250,27009,'9ª REGIÃO DE SAÚDE','31/07/2020',31,11075,110,3,0,0,
    'Sudeste','MG','Caputira',31,311290,31059,'MANHUACU','31/07/2020',31,9298,9,2,0,0,
    'Sudeste','ES','Brejetuba',32,320115,32002,'METROPOLITANA','31/07/2020',31,12404,304,6,0,0,
    'Sudeste','ES','Cachoeiro de Itapemirim',32,320120,32004,'SUL','31/07/2020',31,208972,3528,167,105,2,
    'Sudeste','RJ','Angra dos Reis',33,330010,33001,'BAHIA DA ILHA GRANDE','31/07/2020',31,203785,3817,26,115,0,
    'Sudeste','RJ','Araruama',33,330020,33002,'BAIXADA LITORÂNEA','31/07/2020',31,132400,618,12,42,0,
    'Sudeste','SP','Adamantina',35,350010,35091,'ADAMANTINA','31/07/2020',31,35068,144,0,6,0,
    'Sudeste','SP','Adolfo',35,350020,35156,'JOSE BONIFÁCIO','31/07/2020',31,3562,40,0,3,0,
    'Sul','PR','Mallet',41,411390,41004,'4ª RS IRATI','31/07/2020',31,13630,29,0,2,0,
    'Sul','PR','Mandaguari',41,411420,41015,'15ª RS MARINGA','31/07/2020',31,34400,88,2,4,0,
    'Sul','SC','Irani',42,420780,42010,'ALTO URUGUAI CATARINENSE','31/07/2020',31,10419,64,1,1,0,
    'Sul','SC','Irati',42,420785,42002,'OESTE','31/07/2020',31,1930,16,0,1,0,
    'Sul','RS','Barra Funda',43,430195,43020,'REGIÃO 20','31/07/2020',31,2539,15,0,0,0,
    'Sul','RS','Boa Vista das Missões',43,430215,43020,'REGIÃO 20','31/07/2020',31,2098,3,0,0,0,
    'Sul','RS','Vera Cruz',43,432270,43028,'REGIÃO 28','31/07/2020',31,26863,15,0,0,0,
    'Sul','RS','Viadutos',43,432290,43016,'REGIÃO 16','31/07/2020',31,4756,10,0,1,0,
    'Centro-Oeste','MT','Cocalinho',51,510310,51006,'MEDIO ARAGUAIA','31/07/2020',31,5700,22,1,0,0,
    'Centro-Oeste','MT','Colniza',51,510325,51008,'NOROESTE MATOGROSSENSE','31/07/2020',31,38582,30,4,0,0,
    'Centro-Oeste','MT','Guiratinga',51,510420,51013,'SUL MATOGROSSENSE','31/07/2020',31,15141,44,0,0,0,
    'Centro-Oeste','GO','Formosa',52,520800,52003,'ENTORNO NORTE','31/07/2020',31,121617,677,37,16,2,
    'Centro-Oeste','GO','Formoso',52,520810,52008,'NORTE','31/07/2020',31,4248,16,0,0,0,
    'Centro-Oeste','DF','Brasí­lia',53,530010,53001,'DISTRITO FEDERAL','11/06/2020',24,3015268,20507,1074,274,18,
    'Centro-Oeste','DF','Brasi­lia',53,530010,53001,'DISTRITO FEDERAL','07/07/2020',28,3015268,62694,2311,767,41,
    'Centro-Oeste','DF','Brasí­lia',53,530010,53001,'DISTRITO FEDERAL','31/07/2020',31,3015268,106292,1850,1469,25
    ]

# Criação da TUPLA:

Tupla1COVID = (
    'Norte','RO','Cujubim',11,110094,11001,'VALE DO JAMARI','31/07/2020',31,25215,168,-1,5,0,
    'Norte','RO','Governador Jorge Teixeira',11,110100,11003,'CENTRAL','31/07/2020',31,7767,49,0,0,0,
    'Norte','TO','Alvorada',17,170070,17005,'ILHA DO BANANAL','31/07/2020',31,8412,171,1,2,1,
    'Norte','AC','Assis Brasil',12,120005,12001,'ALTO ACRE','31/07/2020',31,7417,316,0,6,0,
    'Norte','PA','Placas',15,150565,15002,'BAIXO AMAZONAS','31/07/2020',31,30982,277,13,4,0,
    'Norte','PA','Prainha',15,150600,15002,'BAIXO AMAZONAS','31/07/2020',31,29866,323,4,12,9,
    'Norte','RR','Cantã',14,140017,14001,'CENTRO NORTE','31/07/2020',31,18335,725,6,7,0,
    'Norte','RR','Iracema',14,140028,14002,'SUL','31/07/2020',31,11950,188,3,4,0,
    'Nordeste','MA','Afonso Cunha',21,210010,21005,'CAXIAS','31/07/2020',31,6524,131,0,2,0,
    'Nordeste','MA', 'Água Doce do Maranhão',21,210015,21006,'CHAPADINHA','31/07/2020',31,12571,569,2,5,0,
    'Nordeste','PI','Palmeirais',22,220750,22004,'ENTRE RIOS','31/07/2020',31,14539,43,7,2,0,
    'Nordeste','CE','Farias Brito',23,230430,23020,'20ª REGIÃO CRATO','31/07/2020',31,19450,606,11,8,0,
    'Nordeste','RN','Mossoró',24,240800,24002,'2ª REGIÃO DE SAÚDE - MOSSORÓ','31/07/2020',31,297378,5061,73,179,0,
    'Nordeste','PB','Damião',25,250535,25004,'4ª REGIAO','31/07/2020',31,5330,17,4,1,0,	
    'Nordeste','PE','Capoeiras',26,260380,26004,'GARANHUNS','31/07/2020',31,20048,191,8,3,0,
    'Nordeste','BA','Casa Nova',29,290720,29016,'JUAZEIRO','31/07/2020',31,71969,259,2,6,0,
    'Nordeste','AL','Dois Riachos',27,270250,27009,'9ª REGIÃO DE SAÚDE','31/07/2020',31,11075,110,3,0,0,
    'Sudeste','MG','Caputira',31,311290,31059,'MANHUACU','31/07/2020',31,9298,9,2,0,0,
    'Sudeste','ES','Brejetuba',32,320115,32002,'METROPOLITANA','31/07/2020',31,12404,304,6,0,0,
    'Sudeste','ES','Cachoeiro de Itapemirim',32,320120,32004,'SUL','31/07/2020',31,208972,3528,167,105,2,
    'Sudeste','RJ','Angra dos Reis',33,330010,33001,'BAHIA DA ILHA GRANDE','31/07/2020',31,203785,3817,26,115,0,
    'Sudeste','RJ','Araruama',33,330020,33002,'BAIXADA LITORÂNEA','31/07/2020',31,132400,618,12,42,0,
    'Sudeste','SP','Adamantina',35,350010,35091,'ADAMANTINA','31/07/2020',31,35068,144,0,6,0,
    'Sudeste','SP','Adolfo',35,350020,35156,'JOSE BONIFÁCIO','31/07/2020',31,3562,40,0,3,0,
    'Sul','PR','Mallet',41,411390,41004,'4ª RS IRATI','31/07/2020',31,13630,29,0,2,0,
    'Sul','PR','Mandaguari',41,411420,41015,'15ª RS MARINGA','31/07/2020',31,34400,88,2,4,0,
    'Sul','SC','Irani',42,420780,42010,'ALTO URUGUAI CATARINENSE','31/07/2020',31,10419,64,1,1,0,
    'Sul','SC','Irati',42,420785,42002,'OESTE','31/07/2020',31,1930,16,0,1,0,
    'Sul','RS','Barra Funda',43,430195,43020,'REGIÃO 20','31/07/2020',31,2539,15,0,0,0,
    'Sul','RS','Boa Vista das Missões',43,430215,43020,'REGIÃO 20','31/07/2020',31,2098,3,0,0,0,
    'Sul','RS','Vera Cruz',43,432270,43028,'REGIÃO 28','31/07/2020',31,26863,15,0,0,0,
    'Sul','RS','Viadutos',43,432290,43016,'REGIÃO 16','31/07/2020',31,4756,10,0,1,0,
    'Centro-Oeste','MT','Cocalinho',51,510310,51006,'MEDIO ARAGUAIA','31/07/2020',31,5700,22,1,0,0,
    'Centro-Oeste','MT','Colniza',51,510325,51008,'NOROESTE MATOGROSSENSE','31/07/2020',31,38582,30,4,0,0,
    'Centro-Oeste','MT','Guiratinga',51,510420,51013,'SUL MATOGROSSENSE','31/07/2020',31,15141,44,0,0,0,
    'Centro-Oeste','GO','Formosa',52,520800,52003,'ENTORNO NORTE','31/07/2020',31,121617,677,37,16,2,
    'Centro-Oeste','GO','Formoso',52,520810,52008,'NORTE','31/07/2020',31,4248,16,0,0,0,
    'Centro-Oeste','DF','Brasí­lia',53,530010,53001,'DISTRITO FEDERAL','11/06/2020',24,3015268,20507,1074,274,18,
    'Centro-Oeste','DF','Brasi­lia',53,530010,53001,'DISTRITO FEDERAL','07/07/2020',28,3015268,62694,2311,767,41,
    'Centro-Oeste','DF','Brasí­lia',53,530010,53001,'DISTRITO FEDERAL','31/07/2020',31,3015268,106292,1850,1469,25
    )


'''
QUESTÃO 1 - B) Mande printar na tela o número de casos acumulados para o estado do rio de janeiro 
tanto para a tupla quanto para a lista.
'''
CasosL = 0
for X in range(1, len(Lista1COVID)-1, 14):
    if Lista1COVID[X] == 'RJ':
        CasosL = CasosL + Lista1COVID[X + 9]

print('LISTA:\n','O número de óbitos no RJ é:\n', CasosL)

CasosT = 0
for X in range(1, len(Tupla1COVID)-1, 14):
    if Tupla1COVID[X] == 'RJ':
        CasosT = CasosT + Tupla1COVID[X + 9]

print('TUPLA:\n','O número de óbitos no RJ é:\n', CasosT)


'''
QUESTÃO 1 - C) Apresente na tela todos os óbitos acumulados mostrando os casos apenas para os estados 
(sem mostrar regiões de saúde, etc..).
'''

Estados = ('TO','ES','RJ','SP','MG','PA','MA','RO','RR','PI','CE','RN','PE','BA','MT','GO','DF','PR','RS','AC','SC','PB')


for Y in range(0, len(Estados)-1, 1):
    ÓbitosL = 0
    for X in range(1, len(Lista1COVID)-1, 14):
         if Lista1COVID[X] == Estados[Y]:
            ÓbitosL = ÓbitosL + Lista1COVID[X + 11]

    print('Os óbitos acumulados no estado', Estados[Y], 'são:', ÓbitosL)

    
'''
QUESTÃO 1 - D) Assuma que os dados de óbitos novos para o estado da paraíba estejam errados em 10 unidades para menos. 
Sobrescreva a informação tanto na lista quanto na tupla, corrigindo os dados. 
'''

for X in range(1, len(Lista1COVID)-1, 14):
    if Lista1COVID[X] == 'PB':
        Lista1COVID[X + 12] =  Lista1COVID[X + 12] + 10
        PBAtual = Lista1COVID[X + 12]

print('O número atualizado de óbitos novos na PB é: ',PBAtual)

# for X in range(1, len(Tupla1COVID)-1, 14): # Operação com erro! Não é possível executar sobrescrição em TUPLAS!
#     if Tupla1COVID[X] == 'PB': # Operação com erro! Não é possível executar sobrescrição em TUPLAS!
#         Tupla1COVID[X + 12] =  Tupla1COVID[X + 12] + 10 # Operação com erro! Não é possível executar sobrescrição em TUPLAS!
#         PBAtual = Tupla1COVID[X + 12] # Operação com erro! Não é possível executar sobrescrição em TUPLAS!

# print('O número atualizado de óbitos novos na PB é: ',PBAtual) # Operação com erro! Não é possível executar sobrescrição em TUPLAS!


'''
QUESTÃO 1 - E) As duas operações foram possíveis (lista e tupla)? Justifique.
RESPOSTA: As duas operações não foram possíveis. Tendo em vista que a TUPLA é um vetor imutável que restringe as operações de adição, 
alteração e remoção de elementos, apenas foi possivel realizar a sobrescrição do número de óbitos novos na PB no vetor lista. Essa operação não é permitida na TUPLA, 
conforme evidenciado na saída de erro declarado pelo programa:
ERRO DE EXECUSSÃO DA OPEÇÃO NA TUPLA:
Tupla1COVID[X + 12] =  Tupla1COVID[X + 12] + 10
TypeError: 'tuple' object does not support item assignment
'''

'''
QUESTÃO 1 - F) Crie uma nova lista com apenas dados de 1 estado e todos os municípios e 
adicione essa lista nova a lista já existente (append ou insert).
'''

# A lista será criada com a mesma sequência de dados da "Lista1COVID"

DadosDoRN = [
    'Nordeste','RN','Acari',24,240010,24004,'4ª REGIAO DE SAUDE - CAICO','31/07/2020',31,11136,45,0,3,0,
    'Nordeste','RN','Açu',24,240020,24008,'8ª REGIAO DE SAUDE - AÇU','31/07/2020',31,58017,883,37,41,1,
    'Nordeste','RN','Afonso Bezerra',24,240030,24003,'3ª REGIAO DE SAUDE - JOAO CAMARA','31/07/2020',31,11035,65,2,6,0,
    'Nordeste','RN','Água Nova',24,240040,24006,'6ª REGIAO DE SAUDE - PAU DOS FERROS','31/07/2020',31,3252,7,0,0,0,
    'Nordeste','RN','Alexandria',24,240050,24006,'6ª REGIAO DE SAUDE - PAU DOS FERROS','31/07/2020',31,13577,29,0,3,0,
    'Nordeste','RN','Almino Afonso',24,240060,24006,'6ª REGIAO DE SAUDE - PAU DOS FERROS','31/07/2020',31,4735,17,0,0,0,	
    'Nordeste','RN','Alto do Rodrigues',24,240070,24008,'8ª REGIAO DE SAUDE - AÇU',	'31/07/2020',31,14529,278,4,11,0,
    'Nordeste','RN','Angicos',24,240080,24008,'8ª REGIAO DE SAUDE - AÇU','31/07/2020',31,11714,87,0,3,0,	
    ]

#Lista1COVID.append(DadosDoRN)
#print(Lista1COVID)


'''
QUESTÃO 1 - G) Remova da lista os dados das regiões de saúde.
'''
Lista1COVID.extend(DadosDoRN )
Região=[]
for X in range(6, len(Lista1COVID)-1, 14):
    Região.append(Lista1COVID[X])

for X in range(0, len(Região),1):
   Lista1COVID.remove(Região[X])
print(Lista1COVID)

'''
QUESTÃO 1 - H) Verifique se a soma dos dados dos municípios na data de 18/08/2020 é 
igual ao dado da lista, mostrando na tela apenas se for verdadeiro.
'''




'''
QUESTÃO 1 - I) Retorne o tamanho total da lista.
'''
print(len(Lista1COVID))

'''
QUESTÃO 1 - J) Verifique qual é o maior valor numérico de óbitos novos e o menor valor numérico de óbitos novos.
'''
Óbitos = []
for X in range(12, len(Lista1COVID)-1, 13):
    Óbitos.append(Lista1COVID[X])

print('O total de óbitos novos é:',Óbitos)
print('O maior valor numérico de óbitos novos é:', max(Óbitos))
print('O menor valor numérico de óbitos novos é:', min(Óbitos))


'''
QUESTÃO 1 - K) Crie um dicionário de forma que seja possível encontrar os municípios associados a um estado 
específico e extrair os dados de casos novos em apenas um comando.
'''




'''
QUESTÃO 1 - L) Extraia os dados de Teresina/PI apresentando os casos novos com um print. 
'''






