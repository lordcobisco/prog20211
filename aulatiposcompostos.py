#lista = []
#print(lista)
#lista = list()
#print(lista)
#lista = ['Yago',123,1.5]
#lista = list(['Yago',123,1.5])
#exemploDelista = list(['Yago',123,1.5,['Daniel',0.3]])
#print(exemploDelista)

#print(exemploDelista[0])
#print(exemploDelista[1])
#print(exemploDelista[2])
#print(exemploDelista[3])
#print(type(exemploDelista[3]))
#print(exemploDelista[3][0])
#print(exemploDelista[3][1])

#listaMarcaCarros = ['','']
#listaMarcaCarros[0] = input('Digite uma marca de carro\n ')
#listaMarcaCarros[1] = input("Digite outra marca de carro\n")

#print(listaMarcaCarros)
#ListaCarrosEMarcas=['March', 'Tiggo', 'HB20',listaMarcaCarros]
#print(ListaCarrosEMarcas)
# listaMarcaCarros = []
# listaMarcaCarros = [listaMarcaCarros, input('Digite uma marca de carro\n')]
# print(listaMarcaCarros)
# listaMarcaCarros = [listaMarcaCarros,input('Digite uma marca de carro\n')]
# print(listaMarcaCarros)

# exemploDelista = list(['Yago',123,1.5,['Daniel',0.3]])
# print(exemploDelista[-1])
# print(exemploDelista[-2])
# print(exemploDelista[-3])
# print(len(exemploDelista))
# print(exemploDelista+[1,2,3])

#print(listaMarcaCarros)
#ListaCarrosEMarcas=['March', 'Tiggo', 'HB20',listaMarcaCarros]
#print(ListaCarrosEMarcas)
# listaMarcaCarros = []
# listaMarcaCarros = [listaMarcaCarros+[input('Digite uma marca de carro\n')]]
# print(listaMarcaCarros)
# listaMarcaCarros = [listaMarcaCarros+[input('Digite uma marca de carro\n')]]
# print(listaMarcaCarros)
# listaMarcaCarros = [input('Digite uma marca de carro\n'),
#                     input('Digite uma marca de carro\n')]

# exemploDelista = list(['Yago',123,1.5,['Daniel',0.3]]) 
# # print(exemploDelista*2 + ['Souto'])
# # print('Ytalo' in exemploDelista)

# listaDenumeros = [1,2,3,4,5,6,7,8]
# print(max(listaDenumeros))
# print(min(listaDenumeros))
# print(sum(listaDenumeros))
# print(sum(listaDenumeros)/len(listaDenumeros))

# listaMarcaCarros = []
# listaMarcaCarros.insert(0,input('Digite uma marca de carro\n'))
# print(listaMarcaCarros)
# listaMarcaCarros.insert(1,input('Digite uma marca de carro\n'))
# print(listaMarcaCarros)

# listaMarcaCarros = []
# listaMarcaCarros.append(input('Digite uma marca de carro\n'))
# print(listaMarcaCarros)
# listaMarcaCarros.append(input('Digite uma marca de carro\n'))
# print(listaMarcaCarros)

# exemploDelista = ['Yago',123,1.5,['Daniel',0.3]]
# print(exemploDelista)
# exemploDelista.remove("Yago")
# print(exemploDelista)
# listaDeNumeros = [1,2,3,4,5,6,7,8]
# print(listaDeNumeros.index(3))
# listaDeNumeros.reverse()
# print(listaDeNumeros)
# listaDeNumeros.sort()
# print(listaDeNumeros)

#listaDePalavras = ['Yago', 'Daniel', 'Souto']
# listaDePalavras.sort()
# print(listaDePalavras)
# listaDePalavras.reverse()
# listaDePalavras.append('Yago')
# print(listaDePalavras.count('Yago'))
# listaDePalavras.remove("Souto")
# print(listaDePalavras)

# tupla = (1,2,3,4)
# print(tupla)
# tupla = (1,)
# print(tupla)
# tupla = ()
# print(tupla)
# tupla = tuple()
# print(tupla)

# tuplaDeStrings = ("Maria", 'João', "Carlos")
# print(tuplaDeStrings[0])
# print(tuplaDeStrings[0:2])
# print(tuplaDeStrings[:])
# tuplaDeStrings[0] = 'Yago'
# nome = "Python"
# print(nome[0:0])
# print(nome[0:1])
# print(nome[1:2])
# print(nome[2:3])
# print(nome[3:4])
# print(nome[4:5])
# print(nome[5:6])
# print(nome[6:6])

# print(nome[:0])
# print(nome[:1])
# print(nome[:2])
# print(nome[:3])
# print(nome[:4])
# print(nome[:5])
# print(nome[:6])
# print(nome[:6])

dicionario = {}
dicionario = dict()
dicionario["bibilioteca"] = "Estantes"
# print(dicionario)
# print(dicionario['bibilioteca'])

dicionario['bibilioteca'] = {'estantes':[1,2,3,4,5,6,7,8], 'livros':[]}
print(dicionario)
print(dicionario['bibilioteca'])
print(dicionario['bibilioteca']['estantes'])
print(dicionario['bibilioteca']['estantes'][0])
print(dicionario.keys())
print(dicionario['bibilioteca'].keys())

print(dicionario['biblioteca'].items())
print(len(dicionario['biblioteca']))
print(dicionario.get('biblioteca', None))
print(dicionario.get('estantes',None))

