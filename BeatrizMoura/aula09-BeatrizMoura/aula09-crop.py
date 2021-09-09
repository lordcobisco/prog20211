

# Continuacao da aula sem as devidas instalacoes


import numpy as np

lista = [[1.0,0.0,0.0],[]]
vetornumpy = np.array(lista)
print(vetornumpy)
print(vetornumpy.shape)
print(vetornumpy.ndim)
print(vetornumpy.size)
print(type(vetornumpy))
print(vetornumpy.dtype.name)

vetornumpy = np.array(lista, dtype = complex)
vetornumpy = np.array([(1,0), (0,1)], dtype = complex)
