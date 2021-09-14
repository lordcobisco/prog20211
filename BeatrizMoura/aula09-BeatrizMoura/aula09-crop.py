

# Aula 09 - Continuacao da aula sem as devidas instalacoes


#import numpy as np

#lista = [[1.0,0.0,0.0],[]]
#vetornumpy = np.array(lista)
#print(vetornumpy)
#print(vetornumpy.shape)
#print(vetornumpy.ndim)
#print(vetornumpy.size)
#print(type(vetornumpy))
#print(vetornumpy.dtype.name)

#vetornumpy = np.array(lista, dtype = complex)
#vetornumpy = np.array([(1,0), (0,1)], dtype = complex)

'''
import numpy as np

print(np.zeros((3,4)))
#array = np.zeros((3,4))
array = np.ones((3,4))
for i in range (len(array.shape[0]):
    for i in range (len(array.shape[1]):
        print(array[i][j])

array = 30*np.ones(3,4)
print (array)

'''

#import numpy as np

#array = 30*np.arange(10,30,5)
#array = 30*np.arange(0,2,0.3)
#print (array)


'''

import numpy as np

array = 30*np.arange(0,2,0.3)
array = np.linspace(0,2*np.pi,10)
print (array)

x=np.linspace(0,2*np.pi, 10)
print ('x= ', x)
y = np.sin(x)
print('y = ', y)

'''

#import numpy as np

#array = np.arange(6).reshape(2,3)
#print (array)


'''
import numpy as np

vetor1 = np.array([20,30,40,50])
vetor2 = np.arrange(4)
vetorSoma = vetor1 + vetor2
vetorSub = vetor1 - vetor2
vetorMulti = vetor1 * vetor2
vetorDiv = vetor1/vetor2   #as operacoes sao feitas ponto a ponto da matriz
print(vetorSoma, vetor1, vetor2)

vetorMenor = vetor1 < vetor2 
print(vetorMenor)


a = 50*np.random.random((4,1))
vetorComparacao = vetor1 < a
print(vetorComparacao, a)

vetorSoma += vetorSoma
vetorSub -= vetorSub
'''

#import numpy as np

#A = np.array([1,1],[0,1]); print (A)
#B = np.array([2,0],[3,4]); print (B)

#print (A*B); print (A.dot(B))
#print (A@B) # multiplicacao matricial

'''
import numpy as np

a = np.random.random((2,3))
print('a = ', a)
print('soma a = ', a.sum(axis = 0))
print('menor a = ', a.min(axis = 1))
print('maior a = ', a.max(axis = 0))
print('acumulacao = ', a.cumsum(axis = 1))

'''

import numpy as np
#a = np.random.random((50,0))
#print(np.exp(a))
#print(np.sqrt(a))
#print(np.log(a))
#print(np.pow(a))
#print(a**0.5)

a = np.range(10); print(a)
print (a[0])
print (a[2:5])
a[2:5] = 10
print(a)
print (a[:6:2])
print (a[: :-1]) #colocar em ordem decrescente
a = np.array([i**(2) for i in a ]) #preenchendo todos os elementos de uma lista 
print(a)

a = np.array([i**(1/3.) for i in a ])
print(a)
print(np.floor(a+0.3)) #truncamento
print(np.ceil(a+0.3))

