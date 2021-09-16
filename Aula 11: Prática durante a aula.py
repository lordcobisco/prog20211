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

images_and_predictions = list(zip(digits[-1:,predict))
for index,(image,prediction) in enumerate(images_and_predictions):
  plt.axis('off')
  plt.imshow(image)
  print(prediction)















  
