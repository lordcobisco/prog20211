
# Matplotlib

# usar: pip install matplotlib

import matplotlib
import numpy as np
import matplotlib.pyplot as plt

'''

t = np.linspace(0,2*np.pi, 100)
fig, ax = plt.subplots()
ax.plot = (t, np.sin(t))
plt.show()

'''

'''
t = np.linspace(0,2*np.pi, 100)
fig, ax = plt.subplot(2,2)

ax[0,0].plot(t,3*np.sin(t))
ax[0,0].set_title('Titulo do primeiro Grafico')

fig, ax = plt.subplot(1,0)
ax[1,0].plot(t,3*np.sin(t))
ax[1,0].set_title('Titulo do segundo Grafico')

fig, ax = plt.subplot(0,1)
ax[0,1].plot(t,3*np.sin(t))
ax[0,1].set_title('Titulo do terceiro Grafico')

fig, ax = plt.subplot(1,1)
ax[1,1].plot(t,3*np.sin(t))
ax[1,1].set_title('Titulo do quarto Grafico')


ax[1,1].set(xlim=(-2,2), ylim=(-4,4))

fig.tight_layout()

plt.show()

'''

'''

# Grafico de Barras

N=5
mediaHomens = (20,35,30,35,27)
mediaMulheres = (25,25,38,15,29)
stdHomens = (2,3,3,3,2)
stdMulheres = (0,5,0,5,7)
ind = np.arange(N)
width = 0.35
p1= plt.bar(ind, mediaHomens,width, yerr =stdHomens)
p2= plt.bar(ind, mediaMulheres,width, yerr =stdMulheres)

plt.ylabel('Pontuacao')
plt.title('Pontuacao por grupo')
plt.xticks(ind,('G1','G2','G3','G4','G5'))
plt.yticks(np.arange(0,81,10))
plt.legend ((p1[0],p2[0]),('Homem', 'Mulher'))

'''

'''
# Grafico Pizza

labels = 'Frogs','Hogs','Dogs', 'Logs'

size = [15,30,45,10]

fig, ax = plt.subplots()
ax.pie(size,labels=labels, shadow = True, explode =(0,0,0.1,0)) #explode eh pra separar as fatias
plt.show

'''

'''
#BoxPlot

np.random.seed(122313)
all_data = [np.random.normal(0, std ,size=100)] for std in range(1.4) # gerando valores gaussianos
labels = ['x1','x2','x3']
fig, ax = plt.subplots(nrows = 1, ncols = 1,figsize(9,4))
bplot = ax.boxplot(all_data, vert = True, labels=labels)
plt.show()

'''


# Histograma

np.random.seed(23123123)

N_points = 100000
n_bins = 20
x = np.random.randn(N_points)
fig, ax = plt.subplots(1,1)
ax.hist(x,n_bins)
plt.show



# 3D

np.random.seed(23123123)

fig = plt.figure()
ax = fig.gca(projection = '3D')
x = np.random.sample(100)
y = np.random.sample(100)
z = np.random.sample(100)

ax.scatter(x,y,z) # vai gerar pontos

plt.show()


