# lista = []
# print(lista)
# lista = list()
# print(lista)
# lista = ['André',123,1.5]
# lista = list(['André',123,1.5])
# exemploDeLista = list(['André',123,1.5,['Felipe',0.3]])
# # print(exemploDeLista)

# print(exemploDeLista[0])
# print(exemploDeLista[1])
# print(exemploDeLista[2])
# print(exemploDeLista[3])
# print(type(exemploDeLista[3]))
# print(exemploDeLista[3][0])
# print(exemploDeLista[3][1])

# listaMarcaCarros = ['','']
# listaMarcaCarros[0] = input('Digite uma marca de carro\n')
# listaMarcaCarros[1] = input('Digite outra marca de carro\n')

# print(listaMarcaCarros)
# ListaCarrosEMarcas = ['March','Tiggo','HB20',listaMarcaCarros]
# print(ListaCarrosEMarcas)
# listaMarcaCarros = []
# listaMarcaCarros = [listaMarcaCarros,input('Digite uma marca de carro\n')]
# print(listaMarcaCarros)
# listaMarcaCarros = [listaMarcaCarros,input('Digite uma marca de carro\n')]
# print(listaMarcaCarros)

# exemploDeLista = list(['André',123,1.5,['Felipe',0.3]])
# print(exemploDeLista[-1])
# print(exemploDeLista[-2])
# print(exemploDeLista[-3])
# print(len(exemploDeLista))
# print(exemploDeLista+[1,2,3])
# listaMarcaCarros = []
# listaMarcaCarros = [listaMarcaCarros+[input('Digite uma marca de carro\n')]]
# print(listaMarcaCarros)
# listaMarcaCarros = [listaMarcaCarros+[input('Digite uma marca de carro\n')]]
# print(listaMarcaCarros)
# listaMarcaCarros = [input('Digite uma marca de carro\n'),
                    # input('Digite uma marca de carro\n')]

# exemploDeLista = list(['André',123,1.5,['Felipe',0.3]])
# # print(exemploDeLista*2 + ['Oliveira'])
# print('André' in exemploDeLista)
# print('Andre' in exemploDeLista)

# listaDeNumeros = [1,2,3,4,5,6,7,8]
# print(max(listaDeNumeros))
# print(min(listaDeNumeros))
# print(sum(listaDeNumeros))
# print(sum(listaDeNumeros)/len(listaDeNumeros))

# listaMarcaCarros = []
# listaMarcaCarros.insert(0,input('Digite uma marca de carro\n'))
# print(listaMarcaCarros)
# listaMarcaCarros.insert(1,input('Digite outras marca de carro\n'))
# print(listaMarcaCarros)

# listaMarcaCarros = []
# listaMarcaCarros.append(input('Digite uma marca de carro\n'))
# print(listaMarcaCarros)
# listaMarcaCarros.append(input('Digite outras marca de carro\n'))
# print(listaMarcaCarros)

# exemploDeLista = ['André',123,1.5,['Felipe',0.3]]
# print(exemploDeLista)
# exemploDeLista.remove('André')
# print(exemploDeLista)
# listaDeNumeros = [4,1,2,3,5,6,7,8]
# # print(listaDeNumeros.index(3))
# listaDeNumeros.reverse()
# print(listaDeNumeros)
# listaDeNumeros.sort()
# print(listaDeNumeros)

# listaDePalavras = ['André', 'Felipe', 'Oliveira', 'de', 'Azevedo', 'Dantas']
# listaDePalavras.sort()
# print(listaDePalavras)
# listaDePalavras.reverse() 
# print(listaDePalavras)
# listaDePalavras.append('André')
# print(listaDePalavras.count('André'))
# listaDePalavras.remove('Felipe')
# print(listaDePalavras)

# tupla = (1,2,3,4)
# print(tupla)
# tupla = (1,)
# print(tupla)
# tupla = ()
# print(tupla)
# tupla = tuple()
# print(tupla)

# tuplaDeStrings = ('Maria', 'João', 'Carlos') 
# print(tuplaDeStrings[0])
# print(tuplaDeStrings[0:2])
# print(tuplaDeStrings[:])
# tuplaDeStrings[0] = 'André'
# nome = "Python"
# print(nome[0:0])
# print(nome[0:1])
# print(nome[1:2])
# print(nome[2:3])
# print(nome[3:4])
# print(nome[4:5])
# print(nome[5:6])
# print(nome[6:6])

# print(nome[:1])
# print(nome[:2])
# print(nome[:3])
# print(nome[:4])
# print(nome[:5])
# print(nome[:6])

# print(nome[0:0])
# print(nome[0:1])
# print(nome[0:3])
# print(nome[0:4])
# print(nome[0:5])
# print(nome[0:6])

# print(nome[:])
# print(nome[1:])
# print(nome[2:])
# print(nome[3:])
# print(nome[4:])
# print(nome[5:])
# print(nome[6:])

# tupla = (1,2,3,4,5,6,7,8)

dicionario = {}
dicionario = dict()
#dicionario['biblioteca'] = 'Estantes'
#print(dicionario)
#print(dicionario['biblioteca'])

dicionario['nordeste'] = {'RN':[[24,240010,24004,'4ÂªREGIAODESAUDE-CAICO','2020-08-03',32,11136,46,3,3,0,'','',0],
                                [24,240010,24004,'4ÂªREGIAODESAUDE-CAICO','2020-08-03',32,11136,46,3,3,5,'','',0]],
                          'PB':[[25,250010,25011,'11ÂªREGIAO','2020-03-27',13,10234,0,0,0,0,'','',0],
                                [25,250020,25007,'7ÂªREGIAO','2020-03-27',13,5640,0,0,0,0,'','',0]]
                        }

                        #   'RN':[24,240010,24004,'4ÂªREGIAODESAUDE-CAICO','2020-08-03',32,11136,46,3,3,5,'','',0],
                        #   'RN':[24,240690,24006,'6ÂªREGIAODESAUDE-PAUDOSFERROS','2020-08-01',31,3996,5,0,0,0,'','',0],
                        #   'RN':[24,240680,24005,'5ÂªREGIAODESAUDE-SANTACRUZ','2020-12-23',52,4759,110,2,2,0,'','',0],
                        #   'PB':[25,250010,25011,'11ÂªREGIAO','2020-03-27',13,10234,0,0,0,0,'','',0],
                        #   'PB':[25,250020,25007,'7ÂªREGIAO','2020-03-27',13,5640,0,0,0,0,'','',0]}
#      
                            # 'PB':[[0,1,2,3],[0,1,2,3]],
                            # 'PI':[[0,1,2,3],[0,1,2,3]],}
# print(dicionario)
# print(dicionario['biblioteca'])
# print(dicionario['biblioteca']['estantes'])

soma=0
for lista in dicionario['nordeste'].items():
    print(lista['RN'])
    





#dicionario['nordeste']['RN'][0][1])
#print(dicionario['nordeste']['RN'])
# print(dicionario.keys())
# print(dicionario['biblioteca'].keys())

# print(dicionario['biblioteca'].items())
# print(len(dicionario['biblioteca']))
# print(dicionario.get('biblioteca',None))
# print(dicionario.get('estantes',None))
# print(dicionario['estantes'])#dá erro