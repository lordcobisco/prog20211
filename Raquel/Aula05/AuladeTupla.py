#criação de tuplas

tupla = (1,2,3,4)
print(tupla)
tupla = (1,)
print(tupla)
tupla = ()
print (tupla)
tupla =  tuple ()
print(tupla)

tuplaDeStrings = ('Maria','João','Carlos')
print(tuplaDeStrings[0])
print(tuplaDeStrings[0:2])
# forma de acesso varios elementos
print(tuplaDeStrings[:])
#tuplaDeStrings[0] = 'Raquel'

nome = "Python"
print(nome [0:0])
print(nome [0:1])
print(nome [1:2])
print(nome [2:3])
print(nome [3:4])
print(nome [4:5])
print(nome [5:6])
print(nome [6:6])

print(nome [:0])
print(nome [:1])
print(nome [:2])
print(nome [:3])
print(nome [:4])
print(nome [:5])
print(nome [:6])

# tamanho len ((1,2,3))

tupla = (1,2,3,4,5,6,7,8)
 
 # Formas de dicionario

dicionario = {}
dicionario = dict ()
 
dicionario['biblioteca'] = 'Estantes'
print (dicionario['biblioteca'])
dicionario ['biblioteca']= {'estantes':[1,2,3,4,5,6,7,8],'Livros':[]}
print(dicionario)
print(dicionario['biblioteca'])
print(dicionario['biblioteca']['estantes'])
print(dicionario['biblioteca']['estantes'][0])
print(dicionario.keys())
print(dicionario['biblioteca'].keys())


print(dicionario['biblioteca'].items())
print(len(dicionario['biblioteca']))
print(dicionario.get('biblioteca',None))
print(dicionario.get('estantes', None))
#print(dicionario['estantes']) dá erro


