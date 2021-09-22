from sklearn.svm import SVC
from sklearn.multiclass import OneVsRestClassifier
from sklearn.preprocessing import LabelBinarizer

X = [[1,2],[2,4],[4,5],[3,2],[3,1]]
Y = [0,0,1,1,2]
classif = OneVsRestClassifier(estimador=SVC())
modeloTreinado = classif.fit(X,Y)
YEstimado = modeloTreinado.predict(X)
print(Y,YEstimado,Y==YEstimado)

#Validação
X = [[4,2],[7,4],[4,9],[3,3],[3,0]] #isso é o 'images'
Y = [1,8,1,3,2]
YEstimado = modeloTreinado.predict(X)
print(Y,YEstimado,Y==YEstimado)

from sklearn import SVC
from sklearn.datasets import load_digits
import matplotlib.pyplot as plt

digits = load_digits()
plt.gray()
for imagens in digits.images:
  plt.matshow(imagens)
  plt.show()

digits = load_digits()
classif = svm.SVC(gamma=0,001, C=100.)
modeloTreinado = classif.fit(digits.data[:-1],digits.target[:-1])
predict = modeloTreinado.predict(digits.data[:-1])
print(predict)

'''images_and_predictions = list(zip(digits[-1:,predict))
for index,(image,prediction) in enumerate(images_and_predictions):
  plt.axis('off')
  plt.imshow(image)
  print(prediction)'''
                                         
                                         
couter = 0
for image in digits.images:
  plt.axis('off);plt.imshow(image);print(predict[counter])
  counter += 1 
           
from sklearn import svm
from sklearn import datasets
classific = svm.SVC(gamma= 'scale)
iris = datasets.load_iris()
modeloTreinado = classif.fit(X,Y)

from joblib import dumb, load
dumb(modeloTreinado, 'modeloTreinado.mod')

clf = load ('modeloTreinado.mod')
print(clf.predict([X[51]]))


                    
#imagens
from skimage import data, io, filters

imagem = data.coins()
io.show(imagem)
io.show()

bordas = filters.sobel(imagem)

                                        
import matplot.pyplot as plt
from skimage.restoration import (denoise_tv_chambolle)
                                (denoise_bilateral)
                                (denoise_wavelet)
                                (estimate_sigma)
from skimage import data, img_as_float                    
from skimage.util import random_noise
                    
original = img_as_float(data.chelsea()[100:250,50:300])
sigma = 0.155
noise = random_noise(original, var = sigma**2)
fig,ax = plt.suplots(nrows=2,ncols=4,figsize=(8,5))
plt.gray()
                    
sigma_est = estimate_sigma(noisyImage, multichannel=True,
                                       average_sigmas=True)
print("Sigma estimado: {}".format(sigma_est) )

ax[1].inshow(noisyImage)
ax[1]axis('off')
ax[1]set_title('TV')             
                    
ax[2].inshow(denoise_tv_chambolle(noisyImage))          
ax[2]             
ax[2]   
                    
# difícil de acompanhar. Muito rápido.
                    
                    
                    
#plt.show()
import numpy as np
import matplotlib.pyplot as plot
from skimage import data
from skimage.feature import math_template
                                        
imagem = data.coins()
coin = imagem[170:220, 75:130]
                    
resultado = math_template(imagem, coin)
ij = np.unravel_index(np.armax(resultado), resultado.shape)
fig = plt.figure(figsize=(8,3))
axl = plt.suplot(1,3,1)
axl = plt.suplot(1,3,2)
axl = plt.suplot(1,3,3)

axl.imshow(coin, cmap=plt.cm.gray)
axl.imshow(imagem, cmap=plt.cm.gray)
hcoin,wcoin = coin.shape
retângulo = plt.Rectangle((X,Y), wcoin, hcoin, edgecolor = 'r', facecolor='none"
ax2.add.path(rect)
                    
ax3.imshow(resultado)  
ax3.plot(X,Y, 'o',markeredgecolor= 'r',markerfacecolor='none', 
plt.show()
                    
                    
