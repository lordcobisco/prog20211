# # from sklearn.svm import SVC
# # from sklearn.multiclass import OneVsRestClassifier
# # from sklearn.preprocessing import LabelBinarizer

# # x = [[1,2],[2,4],[4,5],[3,2],[3,1]]
# # y = [0,0,1,1,2]
# # classif = OneVsRestClassifier(estimator = SVC())
# # modeloTreinado = classif.fit(x,y)
# # yestimado = modeloTreinado.predict(x,y)
# # print(y,yestimado, y==yestimado)

# from sklearn import svm
# from sklearn.datasets import load_digits
# import matplotlib as plt

# digits = load_digits()
# # plt.gray()
# # for imagens in digits.imagens:
# #     plt.matshow(imagens)
# #     plt.show()
# classif = svm.SVC(gama=0.001, c=100.)
# modeloTreinado = classif.fit(digits.data[:-1], digits.target[:-1])
# predict = modeloTreinado.predict(digits.data[:-1], digits.target[:-1])
# print(predict)
# imagens_and_predicitions = list(zip(digits[-1:],predict))
# for index, (imagem,prediciton) in enumerate(imagens_and_predicitions):
#     plt.axis('off')
#     plt.imshow(image)
#     modeloTreinado.predict(imagens)

from sklearn import svm
from sklearn import datasets
classif = svm.SVC(gama='scale')
iris = datasets.load_iris()
x, y = iris.data, iris.target
modeloTreinado = classif.fit(x, y)
print(y[51])

from joblib import dump, load
dump(modeloTreinado, 'modeloTreinado.mod')

clf = load('modeloTreinado.mod')
print(clf.predict([x[51]]))