from typing import Counter
from sklearn.svm import SVC
from sklearn.multiclass import OneVsRestClassifier
from skleean.preprocessing import LabelBinarizer


x = [[1,2],[2,4],[4,5],[3,2],[3,1]]
y = [0,0,1,1,2]
classif = OneVsRestClassifier,(estimator=SVC())
modeloTreinado = classif.fit(x,y)
#agora fazer o modelo
yestimado = modeloTreinado.predict(x)
print(y, yestimado, y==yestimado)

#validação
x = [[4,2],[7,4],[4,9],[3,3],[3,0]]
y = [1,8,1,3,2]
yestimado = modeloTreinado.predict(x)
print(y, yestimado, y==yestimado)


#classificação



#Imagem
from sklearn import svm
from sklearn.datasets import load_digits
import metplotlib.pyplot as plt

digits = load_digits()
plt.gray()
for imagens in digits.images:
    plt.matshow(imagens)
    plt.show()
classif = svm.SVC(gama=0.001, c=100.)
modeloTreinado = classif.fit(digits.data[:-1],digits.target[:-1])   
predict = modeloTreinado.predict(digits.data[:-1]) 
print (predict)
#images_and_predictions = list(zip(digits.images[-1:],predict))
#for index, (image,prediction) in enumerate(images_and_predictions):
    #plt.axis('off')
    #plt.imshow(image)
#print(prediction)

#for imagens in digits.images:
    #plt.matshow(imagens)
    #plt.show()  
    #modeloTreinado.predict(imagens[:-1])  

Counter = 0
for image in digits.images:
    plt.axis("off"),plt.imshow(image),print(predict[Counter])
    Counter +=1



#from sklearn import svm
#from sklearn import datasets
#classif = svm.SVC(gama='scale')
#iris = datasets.load_iris()
#x, y = iris.data,iris.target
#modeloTreinado = classif.fit (x,y)
#print(y[51])

#from joblib import dump, load
#dump(modeloTreinado,'modeloTreinado.mod')

#clf = load# 

from skimage import data, io, filters

imagem = data.coins()
io.imshow(imagem)
io.show()

bordas = filters.sobel(imagem)
io.imshow(bordas)
io.show()


#restauração dde imagem
import matplotlib.pyplot as plt
from skimage.restoration import (denoise_tv_chambolle,denoise_bilateral,denoise_wavelet,estimate_sigma)
from skiimage import data , img_as_float
from skimage.ultil import random_noise


original = img_as_float(data.chelsea()[100:250,50:300])
sigma = 0.155
noise = random_noise(original,var = sigma**2)

fig ,ax = plt.subplots(nrows=2,ncols=4,figsize=(8,5))
plt.gray()

sigma_est = estimate_sigma(noisyImsge,multichannel=True,
                                     average_sigma=True)                                   
ax[0].axis('off')
ax[0].set_title('TV')
ax [0,1].imshow(denoise_bilateral(noisyImage,multichannel=True, convert2ycbcr=True))
ax[3]
ax[1]


#caracteristica da imagem

import numpy as np
import matplotlib.pyplot as pl
from skimage import data 
from skimage.feature import match_template

imagem = data.coins()
coin = imagem[170:220,75:130]

resultado = match_template(imagem ,coin)
ij = np.unravel_index(np.argmax(resultado),resultado.shape)
x,y = ij[::-1]
fig = plt.figure(figsize=(8,3))
ax1 = plt.subplots(1,3,1)
ax2 = plt.subplots(1,3,2)
ax3 = plt.subplots(1,3,3)

ax1.imshow(coin,cmap=plt.cm.gray)
ax2.imshow(imagem,cmap=plt.cm.gray)
hcoin,wcoin = coin.shape
retângulo = plt.Rectangle(x,y),wcoin,hcoin,edgecolor='r',facecolor='none'
ax2.add_patch(retângulo)

ax3.imshow(resultado)
ax3.plot(x,y,'o',markeredgecolor='r',markerfacecolor='none',markersize=10)
plt.show()