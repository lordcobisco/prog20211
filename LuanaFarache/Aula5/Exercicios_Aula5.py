'''
Exercícios da aula 5, referente a tipos compostos.
'''
# Exemplos de formas de declarar listas vazias:
    #lista = []
    #print(lista)

    #lista = list()
    #print(lista)

# Exemplos de listas com elementos definidos:
    #lista = ['Luana', 123, 1.5]
    #print(lista)

#Lista dentro de listas:
# lista = list(['Luana', 123, 1.5,['João', 'Maria', 2,20], 90])
# print(lista) - Vai printar a lista completa
# Para printar elementos específicos de uma lista, declareos entre [], considere  aposição do elemento na lista. EX:
#print(lista[0])
#print(lista[3][1])

'''
Para criar um lista que será preenchida depois com seus respectivos elementos, 
é necessário definir antes, obrigatoriamente, quantas posições essa lista possui. 
Essa operação pode ser feita com uma função, porém existe essa forma "manual" de realizar essa opreção.
Segue abaixo o exemplo de como criar ess lista vazia para realizar entrada de dados:
'''
# ListaMarcaCarros = ['', ''] #Aqui temos uma lista vazia que possui duas posições que serão preenchidas por strings

# ListaMarcaCarros[0] = input("Digite uma marca de carro \n")
# ListaMarcaCarros[1] = input("Digite outra marca de carro \n")
# print(ListaMarcaCarros)

'''
Para criar uma lista quando não sabemos quantas posições de memória iremos utilizar, basta utilizar o sinal
de =, como se estabelessecemos uma igualdade entre as variáveis para acrescentar elementos novos.
Uma igualdade aditiva. EX:
'''
# lista2 = []
# lista2 = [lista2, input("Digite o elemento novo da sua lista: \n")]
# print(lista2)

# exercício = list(['Luana', 123, 1.5,['João', 'Maria', 2,20], 90])
# print(len(exercício)) #operação para saber o tamanho da lista (número de elementos da lista) - Resposta = 5
# print(len(exercício[3])) #Para saber tamanho da lista dentro de outra lista, acessa pela posição na lista externa - Resposta = 4

# Soma de listas
# exercício = list(['Luana', 123, 1.5,['João', 'Maria', 2,20], 90])
# print(exercício + [50, 15, 1000]) # Resposta = ['Luana', 123, 1.5, ['João', 'Maria', 2, 20], 90, 50, 15, 1000]

# lista4 = [2, 4, 6]
# # print(lista4*2) # Resposta = [2, 4, 6, 2, 4, 6]
# #print(lista4*2 + ["Coragem"]) # Resposta = [2, 4, 6, 2, 4, 6, 'Coragem']
# print(4 in lista4) #Usado para identificar determinado elemento dentro da lista. A saíde é na forma de True ou False
# print(0 in lista4)

# lista5 = [1,3,5,7,9,10]
# print(max(lista5)) # Utilizado para identificar o valor máximo da lista
# print(min(lista5)) # Utilizado para identificar o valor mínimo da lista
# print(sum(lista5)) # Utilizado para executar a soma de todos os elementos da lista
# print(sum(lista5)/len(lista5)) # Utilizado para saber a média dos valores da lista - Divide a soma pelo número de elementos

'''
Operação para inserir elementos em uma lista usando a função INSERT- É necessário inserir comandos em 
sequência para concatenação da lista final, porém é preciso definir a posição de cada inserção antes do input. 
EXEMPLO:
'''
# MarCacarros = [] #Lista vazia a ser preenchida
# MarCacarros.insert(0,input('Digite uma marca de carros\n'))
# print(MarCacarros)
# MarCacarros.insert(1,input('Digite outra marca de carros\n'))
# print(MarCacarros) # Saída = ['Jeep', 'Fiat']

'''
Também é possível realizar a inserção de novos elementos na lista utilizando a função APPEND. A diferença entre 
APPEND e INSERT é que, na APPEND, não é necessário declarar as posições dos elementos antes do input pois 
a função aloca os elementos na lista na mesma sequência em que foram declarados. 
EXEMPLO:
'''
# MarCacarros = [] #Lista vazia a ser preenchida
# MarCacarros.append(input('Digite uma marca de carros\n'))
# print(MarCacarros)
# MarCacarros.append(input('Digite outra marca de carros\n')) 
# print(MarCacarros) # Saída = ['Jeep', 'Fiat']

'''
Função REMOVE - Utilizada para remover elementos de determinada lista.
EXEMPLO:
'''
# Exercício2 = ['Luana', 123, 1.5,'João', 'Maria', 2, 20, 90]
# print(Exercício2)
# Exercício2.remove('Luana')
# print(Exercício2)
# print(Exercício2.index('João')) #Função INDEX - Para consultar qual a posição/o índex de determinado elemento em uma lista

# lista5 = [1,3,5,7,9,10]
# lista5.reverse() # Utilizado para inverter a ordem da lista
# print(lista5)
# lista5.sort() # Utilizado para organizar a lista em ordem crescente de valores ou ordem  de letras
# print(lista5)

# Formas de declarar/criar uma tupla:
# Tupla1 = (1,2,3,4,5,6) 
# print(Tupla1) #Saída = (1, 2, 3, 4, 5, 6)
# Tupla2 = (1, )
# print(Tupla2) #Saída = (1,) - Tupla com o 2º elemento vazio
# Tupla3 = ()
# print(Tupla3) #Saída= () - Tupla vazia, 1º forma
# Tupla4 = tuple() # Tupla vazia, 2º forma
# print(Tupla4)

# Strings = ("Maria", "João", "Carlos") #Tupla de istrings
# print(Strings[0]) # 1º posição da tupla = "Maria"
# print(Strings[0:2]) # 2 elementos a partir da 1º posição da tupla = "Maria", "João"


Dicionário = {}
# Dicionário = dict()
# Dicionário['biblioteca'] = 'Estantes'
# # print(Dicionário)
# # print(Dicionário['biblioteca']) # Neste caso a saída será Estantes, pois 'biblioteca' é a "chave" que acessa 'estantes'

Dicionário ['biblioteca'] = {'Estantes' : [1,2,3,4,5,6,7,8]} # dicionário contendo outro dicionário
print(Dicionário)
# print(Dicionário['biblioteca']) #Para acessar todos os itens do dicionário
# print(Dicionário['biblioteca']['Estantes']) #Para acessar os itens referentes a estantes dentro do dicionário biblioteca
# print(Dicionário['biblioteca']['Estantes'][0]) # Acessar o 1º item referente a estantes
# print(Dicionário.keys())
# print(Dicionário['biblioteca'].keys()) # Localiza os elementos(keys) contidos em um dicionário
# print(Dicionário['biblioteca'].items()) # Localiza os itens contidos em um dicionário.
# print(Dicionário.get('biblioteca',None)) 
# print(Dicionário.get('Estantes',None))
# print(Dicionário['Estantes']) # Desta forma da erro, pois estantes não existe


