# Aula de tipos compostos
lista = []
print (lista)

#outra forma
#forma de definir a lista vazia

lista = list()
print (lista)

#forma para mosta o conteudo
lista = ['Raquel',123,1.5]
lista = list (['Raquel',123,1.5])
print(lista)

#forma de colocar uma lista dentro de outra lista
exemplodeLista = list (['Raquel',123,1.5,['Felipe',0.3]])
#print(exemplodeLista)

print(exemplodeLista[0])
print(exemplodeLista[1])
print(exemplodeLista[2])
print(exemplodeLista [3])
print(type(exemplodeLista[3]))
print(exemplodeLista[3][0])
print(exemplodeLista [3][1])


listaMarcaCarros = ['','']
listaMarcaCarros [0]= input('digite uma marca de carro\n')
listaMarcaCarros[1]= input('digite outra marca de carro\n')

print(listaMarcaCarros)
listaCarrosEMarcas = ['March','Tiggo','HB20', listaMarcaCarros]
print(listaCarrosEMarcas)

listaMarcacarros = []
listaMarcaCarros = [listaMarcaCarros,input('Digite uma marca de carro\n')]
print(listaMarcaCarros)
listaMarcaCarros = [listaMarcacarros, input ('Digite uma marca de carro\n')]
print (listaMarcaCarros)


exemplodeLista = list (['Raquel',123,1.5,['Felipe',0.3]])
#0 1 2... 127 -127 -126... -1
#print(exemplodeLista [-1])

print(exemplodeLista[-1])
print(exemplodeLista[-2])
print(exemplodeLista[-3])

print(len(exemplodeLista))
print(exemplodeLista + [1,2,3])

# Somar uma lista com outra
listaMarcaCarros = [input('Digite uma marca de carro\n')]
input('digite uma marca de carro\n')

exemplodeLista = list (['Raquel',123,1.5 ['Felipe',0.3]])
print(exemplodeLista*2 + ['Oliveira'])

#verifica um elemento dentro da lista 
print ('Raquel' in exemplodeLista)
print ('Raquel' in exemplodeLista)

listaDeNumeros = [1,2,3,4,5,6,7,8]
print(max(listaDeNumeros))
print(min(listaDeNumeros))
print(sum(listaDeNumeros))
print(sum(listaDeNumeros)/len(listaDeNumeros))

listaMarcaCarros =[]
listaMarcaCarros.insert(0,input('Digite uma marca de carro\n'))
print(listaMarcaCarros)


listaMarcaCarros = []
listaMarcaCarros.append(input('digite uma marca de carro\n'))
print(listaMarcaCarros)

exemplodeLista = ('Raquel',123,1.5, ['Felipe',0.3])
print(exemplodeLista)
exemplodeLista.remove('Raquel')
print(exemplodeLista)
listaDeNumeros = [4,1,2,3,4,5,6,7,8]
print(listaDeNumeros.index(3))
listaDeNumeros.reverse()
print(listaDeNumeros)
listaDeNumeros.sort()
print(listaDeNumeros)

listaDePalavras = ['Raquel','Emanuela','de', 'Medeiros']
listaDePalavras.sort()
print(listaDePalavras)
listaDePalavras.reverse()
print(listaDePalavras)

listaDePalavras.append('Raquel')
print(listaDePalavras.count('Raquel'))
listaDePalavras.remove('Emanuela')
print(listaDePalavras)


