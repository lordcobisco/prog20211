### LISTAS ###

# 1ª forma de criar uma lista
lista = []
  print (lista)
  #só identa de for tomada de decisão. Se for instrução, não identa.
  
# 2ª forma de criar uma lista vazia
  lista = list () # criando a lista
  print (lista) # mostrar a lista
lista = ['Thiago', 123, 1.5] #conteúdo da lista separados por vírgula= 'Thiago', 123, 1.5
print(lista)

# 3ª forma de criar uma lista vazia
  lista = list () # criando a lista
  print (lista) # mostrar a lista
lista = list (['Thiago', 123, 1.5]) #conteúdo da lista separados por vírgula= 'Thiago', 123, 1.5
print(lista)

# Criar uma lista dentro de outra lista
  lista = list () # criando a lista
  print (lista) # mostrar a lista
ExemploDeLista = list (['Thiago', 123, 1.5 ['Paloma', 0.3]]) #conteúdo da lista separados por vírgula= 'Thiago', 123, 1.5
print(ExemploDeLista)

print(ExemploDeLista [0]) # Se quiser acessar apenas a primeira camada da lista. Para acessar a primeira função, precisa necessariamente começar da posição 0. Toda essa parte é saída.
print(ExemploDeLista [1]) # Se quiser acessar apenas a segunda camada da lista.Toda essa parte é saída.
print(ExemploDeLista [2]) # Se quiser acessar apenas a terceira camada da lista. Toda essa parte é saída.
print(type(ExemploDeLista [3])) # Se quiser acessar apenas a terceira camada da lista. Toda essa parte é saída.
print(ExemploDeLista [3][0])
print(ExemploDeLista [3][1])

listaMarcaCarros = ['', '']
listaMarcaCarros[0] = input(digite o valor da marca do carro\n')
listaMarcaCarros[1] = input(digite outra marca de carro\n')

print(listaMarcaCarros)
ListaCarrosEMarcas = ['March', 'Tiggo', 'HB20', listaMarcaCarros]
print(ListaCarrosEMarcas)
                            
listaMarcaCarros = []
listaMarcaCarros = [listaMarcaCarros,input(digite uma marca de carro\n')] #está juntando nada com alguma coisa, o que vai escrever.
print (listaMarcaCarros)
listaMarcaCarros = [listaMarcaCarros,input(digite uma marca de carro\n')]
print (listaMarcaCarros)
                                           
ExemploDeLista = list(['Thiago', 123, 1.5 ['Paloma', 0.3]])
print(ExemploDeLista[-1])
print(ExemploDeLista[-2])
print(ExemploDeLista[-3])                  

print(len(ExemploDeLista)) #len significa length.
print(ExemploDeLista+[1,2,3])
                                           
listaMarcaCarros = [listaMarcaCarros+[input(digite uma marca de carro\n')]]
print(listaMarcaCarros)
                                            
listaMarcaCarros = [input(digite uma marca de carro\n')]
                    input(digite uma marca de carro\n')
                          
ExemploDeLista = list (['Thiago', 123, 1.5,['Paloma', 0.3]])
print (ExemploDeLista*2 + ['Oliveira'])

print('Thiago' in ExemploDeLista)
print('Thiagoo' in ExemploDeLista)
                          
listaDeNumeros = [1,2,3,4,5,6,7,8]
print(max(listaDeNumeros))
print(min(listaDeNumeros))
print(sum(listaDeNumeros)) #'sum' quer dizer 'soma'.
print(sum(listaDeNumeros)/len(listaDeNumeros))
                          
listaMarcaCarros = []
listaMarcaCarros.isert(0,input((digite uma marca de carro\n'))
print(listaMarcaCarros)
listaMarcaCarros.isert(1,input((digite uma marca de carro\n'))
print(listaMarcaCarros)
                                
listaMarcaCarros = []
listaMarcaCarros.append(0,input((digite uma marca de carro\n')) 
print(listaMarcaCarros) #append é pra concatenar.
listaMarcaCarros.append(1,input((digite uma marca de carro\n'))
print(listaMarcaCarros)
                                 
ExemploDeLista = list(['Thiago', 123, 1.5 ['Paloma', 0.3]])
print(ExemploDeLista)
ExemploDeLista.remove ('Thiago')
print(ExemploDeLista)
listaDeNumeros = [1,2,3,4,5,6,7,8]
print(ExemploDeLista.index(3))

listaDeNumeros.reverse() #reverso é pra inverter a ordem.
print(listaDeNumeros)
listaDeNumeros.sort() # o sort vai colocar na ordem crescente.
print(listaDeNumeros)
                                 
ListadePalavras = ['Thiago', 'Andreson', 'Brito', 'de', 'Araújo']
ListadePalavras.sort()
print(ListadePalavras)

ListadePalavras.reverse()
print(ListadePalavras)

ListadePalavras.append('Thiago')
print(ListadePalavras.count('Thiago'))
                                 
ListadePalavras.remove('Paloma')
...
                                 
# A == B: um conteúdo é IGUAL ao outro conteúdo.
# A is B: is= isso É aquilo.
                                 
### TUPLAS ###
# Uma tupla é uma lista imutável que restringe a adição, alteração e remoção de elementos.
# na tupla, usa parenteses, enquanto na lista não usa parenteses.

tupla = (1,2,3,4)
print(tupla)

tupla = ()
print(tupla)

tupla = tupla()
print(tupla)
                                 
tuplaDeStrings = ('Maria', 'João', 'Carlos')
print(tuplaDeStrings[0])
print(tuplaDeStrings[0:2])
print(tuplaDeStrings[:])
#tuplaDeString[0] = 'Thiago': Na lista, poderia sobrescrever a posição 0.
                                 
nome = "python"
print(nome[0:1]) # funciona tanto pra string, quanto pra lista, qunato pra tupla.
print(nome[1:2]) # funciona tanto pra string, quanto pra lista, qunato pra tupla.
print(nome[2:3]) # funciona tanto pra string, quanto pra lista, qunato pra tupla.
print(nome[3:4]) # funciona tanto pra string, quanto pra lista, qunato pra tupla.
print(nome[4:5]) # funciona tanto pra string, quanto pra lista, qunato pra tupla.
print(nome[5:6]) # funciona tanto pra string, quanto pra lista, qunato pra tupla.
print(nome[6:6]) # funciona tanto pra string, quanto pra lista, qunato pra tupla.

print(nome[:1]) # funciona tanto pra string, quanto pra lista, qunato pra tupla.
print(nome[:2]) # funciona tanto pra string, quanto pra lista, qunato pra tupla.
print(nome[:3]) # funciona tanto pra string, quanto pra lista, qunato pra tupla.
print(nome[:4]) # funciona tanto pra string, quanto pra lista, qunato pra tupla.
print(nome[:5]) # funciona tanto pra string, quanto pra lista, qunato pra tupla.
print(nome[:6]) # funciona tanto pra string, quanto pra lista, qunato pra tupla.

print(nome[0:1]) # funciona tanto pra string, quanto pra lista, qunato pra tupla.
print(nome[0:2]) # funciona tanto pra string, quanto pra lista, qunato pra tupla.
print(nome[0:3]) # funciona tanto pra string, quanto pra lista, qunato pra tupla.
print(nome[0:4]) # funciona tanto pra string, quanto pra lista, qunato pra tupla.
print(nome[0:5]) # funciona tanto pra string, quanto pra lista, qunato pra tupla.
print(nome[0:6]) # funciona tanto pra string, quanto pra lista, qunato pra tupla.

print(nome[0:]) # funciona tanto pra string, quanto pra lista, qunato pra tupla.
print(nome[1:0]) # funciona tanto pra string, quanto pra lista, qunato pra tupla.
print(nome[2:0]) # funciona tanto pra string, quanto pra lista, qunato pra tupla.
print(nome[3:0]) # funciona tanto pra string, quanto pra lista, qunato pra tupla.
print(nome[4:0]) # funciona tanto pra string, quanto pra lista, qunato pra tupla. 
print(nome[5:0]) # funciona tanto pra string, quanto pra lista, qunato pra tupla.
print(nome[6:0]) # funciona tanto pra string, quanto pra lista, qunato pra tupla.
                                 

### DICIONÁRIOS ###                                

                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 



                                 
