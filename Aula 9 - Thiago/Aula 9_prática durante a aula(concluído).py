import numpy as np
print (np.zeros((3,4)))
a = []
a.append

import numpy as np
print (np.zeros((3,4)))
for i in range (array.shape[0])
    for j in range(array.shape[1])
        print(array[1][j])


array = 30*np.ones((3,4)))
print(array)

array = 30*np.empty((3,4)))
print(array)

array = 30*np.arange(10,30,5)
array = 30*np.arange(0,2,0.3)
print(array)

from numpy import pi
array = np.linspace (0,2*np.pi,10)
print(array)

array = 30*np.arange(0,2,0.3)
print(array)

x = np.linspace (0,2*np.pi,100)
print('x = ', x)
y = np.sin(x)
print('y = ',y)

array = np.arange(6).reshape((2,3))
print(array)

array = np.arange(9).reshape((3,3))
print(array)

array = np.arange(24).reshape((2,3,4))
print(array)

vetor1 = np.array([20,30,40,50]);print(vetor1)
vetor2 = np.arange(4);print(vetor2)
vetorSoma = vetor1+vetor2
print(vetorSoma)


vetorSoma = vetor1+vetor2
vetorSubtração = vetor1-vetor2
vetorMultiplicação = vetor1*vetor2
vetorDivisão = vetor1/vetor2
vetorComparação = vetor1<vetor2
vetorComparação = vetor1<np.random((4,))
print(vetorComparação)

a = 50*np.random.random((4,));print(a)
vetorComparação = vetor1<a
print(vetorComparação)

vetor1 += vetor2; vetor1 = vetor1 + vetor2
vetor1 -= vetor2; vetor1 = vetor1 - vetor2
vetor1 *= vetor2; vetor1 = vetor1 * vetor2

A = np.array([[1,1],[0,1]])
B = np.array([[2,0],[3,4]])
print(A*B);print(A.dot(B))
print(A@B) #o arroba faz a operação matricial

a = np.random.random((2,3))
print("a = ", a)
print("sum a = ", a.sum(axis=0))
print("min a = ", a.min(axis=1))
print("max a = ", a.max(axis=0))
print("cumsum a = ", a.cumsum(axis=1))


a = np.random.random(50,))
print(np.exp(a))
print(np.sqrt(a))
print(np.log(a))
print(np.pow(a**5))
print(a**5)
print(a**0.5)

a = np.arange(10);print(a)
print(a[0])
print(a[2:5])

a[2:5] = 10
print(a)

print(a[:6:2])
print(a[: :-1])

a = np.array([i**(2) for i in a])
print (a)

a = np.array([i**(1/3.) for i in a])
print (a)
print(np.floor(a))

a = np.array([i**(1/3.) for i in a])
print (a)
print(np.floor(a+0.3))
print(np.ceil(a+0.3))


a = np.arange(12)*2;print(a)
i = np.array([1,3,8,5]) #valores especificos para acessar posições específicas do vetor final.
print(a[i])

j = np.array([3,4],[9,7])
print(a[j])

palette = np.array([[0,0,0],
                   [255,0,0],
                    0,255,0],
                    0,0,255],
                    255,255,255]])

imagem = np.array([[0,1,2,0]
                   [0,3,4,0]])
print(palette[imagem])

a = np.arange(12)*2;print(a)
print(a[a<5])
a[a<5] = 5
a[a>5] = 5
print(a)

b = np.array[True, False]
c = np.array[[1,2],[3,4]];print(c)
print(c[b,:])

b = np.array[True, True]
c = np.array[[1,2],[3,4]];print(c)
print(c[b,:])
print(c[b,b])


A = np.array([[1.,2.],[3.,4.]]);print(A)
print(A.transpose())
print(A.inv(A))
print(A@A)
print(np.trace(A)))
print(np.linalg.eig(A))
b = np.array([[5.],[7.]])
print(np.linalg.solve(A.b)) # Ax=b












