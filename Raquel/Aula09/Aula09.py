import numpy as np
lista = [[1.0,0.0,0.],[0.,1.,2.]]
vetornumpy = np.array(lista)
print(vetornumpy)

print(vetornumpy.shape)
print(vetornumpy.ndim)
print(vetornumpy.size)
print(type(vetornumpy))
print(vetornumpy.dtype.nam)




vetornumpy = np.array([(1,0),(0,1)],dtype=complex)
vetornumpy = np.array([1,2],dtype=complex)
print(vetornumpy)
