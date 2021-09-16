import matplotlib
import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0,2*np.pi,100)
fig, ax = plt.subplots()
ax.plot(t.np.sin(t))
plt.show()

t = np.linspace(0,2*np.pi,100)
fig, ax = pltsubplots(2,2)
ax[0,0.plot(t,3*np.sin(t));ax[0,0.set_title('Título do primeiro parágrafo')
ax[0,0.plot(t,3*np.sin(t));ax[1,0.set_title('Título do segundo parágrafo')
ax[0,0.plot(t,3*np.sin(t));ax[0,1.set_title('Título do terceiro parágrafo')
ax[0,0.plot(t,3*np.sin(t));ax[1,1.set_title('Título do quarto parágrafo')
ax[1,1.set(xlim=(-2,2, ylim=(-4,4))
fig.tight_layout()
plt.show()

N = 5
mediaHomens = (20,35,30,35,27); stdHomens = (2,3,3,3,2)
mediaMulheres = (25,25,38,15,29);stdMulheres = (0,5,0,5,7)
ind = np.arange(N);width = 0.35
p1 = plt.bar(ind,mediaHomens,width yerr=stdHomens)
p2 = plt.bar(ind,mediaMulheres,width yerr=stdMulheres)
plt.ylabel('Pontuação')
plt.title('Pontuação por grupo de idade')
plt.xticks('G1','G2','G3','G4','G5')
plt.yticks(...

labels = 'Frogs', 'Hogs','Dogs', 'Logs'
size = [15,30,45,10]
fig,ax = plt.subplots()
ax.pie(size,labels=labels,shadow=True;explode=(0,0,0.1,0))
plt.show()

#Gráfico Bloxplot
np.random.seed(19680801)
all_data = [np.random.normal(0,std,size=100) for std in range (1,4)]
labels = ['x1','x2','x3']
fig,ax = plt.subplots(nrows=1,ncols==1, figsize=(9,4))
bplot = ax.boxplot(all_data,vert=True,labels=labels)
plt.show()

#Histograma
np.random.seed(19680801)
N_points = 100000
n_bins = 20
x = np.random.randn(N_points)
fig,ax=plt.subplots(1,1)
ax.hist(x,n_bins)
plt.show()

#Gráficos 3D
np.random.seed(19680801)
fig = plt.figure()
ax = fig.gca(projection='3d')
x = np.random.sample(100)
z = np.random.sample(100)
y = np.random.sample(100)
ax.scatter(x,y,z)
plt.show()









