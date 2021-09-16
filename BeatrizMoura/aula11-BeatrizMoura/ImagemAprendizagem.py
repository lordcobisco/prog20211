

#from scipy.sparse import data
#from sklearn.base import ClassifierMixin
#from sklearn.svm import SVC

#from sklearn.multiclass import OneVsRestClassifier

#from sklearn.preprocessing import LabelBinarizer 

'''
X = [[1,2],[2,4],[4,5],[3,2],[3,1]]
y = [0,0,1,1,2]
classif = OneVsRestClassifier(estimator=SVC())
classif.fit(X,y)
modeloTreinado = classif.fit(X,y)
yestimado = modeloTreinado.predict(X)

#validacao
X = [[4,2],[7,4],[4,9],[3,3],[3,0]]
y = [1,8,1,3,2]
yestimado = modeloTreinado.predict(X)

print(y,yestimado,y==yestimado)

'''
#####################

'''

from sklearn import svm
from sklearn.datasets import load_digits
import matplotlib.pyplot as plt

digits = load_digits()

#plt.gray()

#for imagens in digits.image:

 #   plt.matshow(imagens)
  #  plt.show()
classif = svm.SVC(gamma=0.001, C=100)

modeloTreinado = classif.fit(digits.data[:-1], digits.target[:-1])
predict = modeloTreinado.predict(digits.data[:-1])
print(predict)

imagens_predictions = list.zip(digits[:-1], predict)


counter = 0 
for image in digits.images:
    plt.axis('off')
    plt.imshow(image)
    print(predict[counter])
    counter += 1

'''

############

'''

from sklearn import svm

from sklearn import datasets

classif = svm.SVC(gamma = 'scale')

iris = datasets.load_iris()

X, y = iris.data, iris.target

modeloTreinado = classif.fit(X,y)

from joblib import dump, load #joblib serve para salvar o modelo treinado

dump(modeloTreinado, 'modeloTreinado.mod')

clf = load('modeloTreinado.mod')

print(clf.predict([X[51]]))

'''

######

'''
from skimage import data, io, filters

imagem = data.coins()
io.show(imagem)
io.show

bordas = filter.sobel(imagem)
io.show(bordas)
io.show 

'''

########

'''
import matplotlib.pyplot as plt

from skimage.restoration import(denoise_tv, chambolle, denoise_bilateral, denoise_wavelet, estimate_sigma)
from skimage.restoration import data, img_as_float
from skimage.util import random_noise

original = img_as_float(data.chelsea()[100],[50])
sigma = 0.155
noise = random_noise(original, var = sigma**2)

fig, ax = plt.subplot(nrows = 4, figsize = (8,5)) 

sigma_est = estimate_sigma(noise, multichannel = True, average_sigmas = True)

print( ' Sigma estimado: {}'.format(sigma_est) )


ax[0,2].imshow(noise, multichannel = True)
ax[0,2].axis('off')
ax[0,2].set_title('NoisyImage')

ax[2,0].imshow(denoise_tv(noise, multichannel = True))
ax[2,0].axis('off')
ax[2,0].set_title('TV')


'''

############

import numpy as np
import matplotlib.pyplot as plt
from skimage import data 
from skimage.feature import match_template # encontrar caracteristica dentro da imagem

imagem = data.coins()
coin = imagem[170:220, 75:130]

resultado = match_template(imagem, coin)

ij = np.unravel_index(np.argmax(resultado), resultado.shape)

x,y = ij[::-1]

fig = plt.figure(figsize=(8.3))
ax1 = plt.subplot(1,3,1)
ax2 = plt.subplot(1,3,2)
ax3 = plt.subplot(1,3,3)

ax1.imshow(coin, cmap = plt.cm.gray)
ax2.imshow(imagem, cmap = plt.cm.gray)
hcoin, wcoin = coin.shape
retangulo = plt.Rectangle((x,y), wcoin, hcoin, edgecolor = 'r', facecolor = 'nome' )
ax2.add_patch(retangulo)
ax3.imshow(resultado) 
ax3.plot(x,y, 'o',markeredgecolor = 'r', markerfacecolor = 'nome', markersize = 10)
plt.show()
