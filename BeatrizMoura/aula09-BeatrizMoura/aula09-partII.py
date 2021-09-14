
# Numpy - Parte II

import numpy as np

#a = np.arange(12)*2; print(a)
#i = np.array([1,3,8,5])
#print(a[i])
#j = np.array([[3,4],[9,7]])
#print (a[j])

'''
pallete = np.array([0,0,0],
                   [255,0,0],
                   [0,255,0],
                   [0,0,255],
                   [255,255,255])
        
imagem = np.array([0,1,2,0],
                  [0,3,4,0])


a = np.arange(12)*2; print(a)                
print(pallete[imagem])
print(a<[a<5])
a[a<5] = 5
a[a>15] = 15
print (a)

b = np.array([True, False])
c = np.array[[1,2], [3,4]]
print (c[b,:]) # mostra todas as colunas
print (c[b,b])

'''

A = np.array([1.,2.],[3.,4.]); print(A)
print(A.transpose())
print(A.inv())
print(A@A)
print(A.trace())
print(A.linalg.eig(A))
b = np.array([[5.],[7.]])
print(np.linalg.solve(A,b)) # x = Ax= b 


