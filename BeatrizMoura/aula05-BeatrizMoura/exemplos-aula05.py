#lista = []
#print(lista)
# um . faz com que possamos ver todos os itens da lista

#lista = list() # essa linha eh igual  linha 1
#print(lista)

#lista = ["Beatriz", 123, 1.5]
#print(lista)
#lista = list(["Beatriz", 123, 1.5, ["Beatriz", 0.3]])
#print(lista)
#print(lista[0])
#print(lista[3])
#print(lista[0][0])

#listaMarcaCarros = ['','']
#listaMarcaCarros[0]= input('Digite uma marca de carro\n')
#listaMarcaCarros[1]= input('Digite outra marca de carro\n')
#print(listaMarcaCarros)
#listaCarros = ['March','Liggo','HB20', listaMarcaCarros]
#print(listaCarros)

#lista = list(["Beatriz", 123, 1.5, ["Beatriz", 0.3]])
#print(lista)
#print(lista[-1])
#print(len(lista))
#print(lista + [1,2,3])
#print('Beatriz' in lista)

#listaNumeros = [1,2,3,4,5,6,7,8]
#print(max(listaNumeros))
#print(min(listaNumeros))
#print(sum(listaNumeros))
#print(sum(listaNumeros)/len(listaNumeros))

#listaMarcaCarros = []
#listaMarcaCarros.insert(0, input('Digite uma marca de carro \n'))
#print(listaMarcaCarros)
#listaMarcaCarros.insert(1, input('Digite uma marca de carro \n'))
#print(listaMarcaCarros)

#lista = list(["Beatriz", 123, 1.5, ["Beatriz", 0.3]])
#print(lista)
#lista.remove('Beatriz')
#print(lista)
#listaNumeros = [1,2,3,4,5,6,7,8]
#print(listaNumeros.index(4))
#listaNumeros.reverse()
#print(listaNumeros)
#listaNumeros.sort()
#print(listaNumeros)

#listaPalavras = ['Beatriz', 'do', 'Nascimento', 'P', 'Moura']
#listaPalavras.sort()
#print(listaPalavras)
#listaPalavras.reverse()
#print(listaPalavras)
#listaPalavras.append('Bea')
#print(listaPalavras.count('Bea'))

#tupla = (1,2,3,4)
#print(tupla)
#tupla = (1,)
#print(tupla)
#tupla = tuple()
#print(tupla)

#tuplaString = ('Maria', 'Joao', 'Carlos')
#print(tuplaString[0])
#print(tuplaString[0:2])
#print(tuplaString[:])

#nome = 'Python'
#print(nome[0:0])
#print(nome[0:1])
#print(nome[1:2])
#print(nome[2:3])
#print(nome[3:4])
#print(nome[4:5])
#print(nome[5:6])

#print(nome[:0])
#print(nome[:1])
#print(nome[:2])
#print(nome[:3])
#print(nome[:4])
#print(nome[:5])
#print(nome[:6])

dicionario = {}
dicionario = dict()
dicionario['biblioteca'] = 'estantes'
print(dicionario)
print(dicionario['biblioteca'])
dicionario['biblioteca'] = {'estantes':[1,2,3,4,5], 'livros':[]}
print(dicionario)
print(dicionario['biblioteca'])
print(dicionario['biblioteca']['estantes'])
print(dicionario['biblioteca']['estantes'][0])
print(dicionario.keys())
print(dicionario['biblioteca'].keys())
print(dicionario['biblioteca'].items())
print(len(dicionario['biblioteca']))
print(dicionario.get('biblioteca', None))