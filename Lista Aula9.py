import numpy as np
import math



ang = np.array(angulo_lista)
print(ang)

lista = []
for linha in ang:
    soma = linha[0] + linha[1]
    lista.append(soma)
print(lista)
print(sum(lista))

lista2 = []
for linha in ang:
    listaMedia = angulo.mean()
    lista2.append(listaMedia)

lista3 = []
for linha in ang:
    menor_angulo = ang.min()
    lista3.append(menor_angulo)
print(lista3)

lista4 = []
for linha in ang:
    maior_angulo = ang.max()
    lista4.append(maior_angulo)
print(lista4)

lista5 = []
for linha in ang:
    integral = ang.sum()
    lista5.append(integral)
print(lista5)

lista6 = []
for linha in ang:
    diferenca = listaMedia - ang**2
    divisao = diferenca/len(ang)
    lista6.append(divisao)
print(lista6)

lista7 = []
for linha in ang:
    variacaoAngular = np.diff(ang)
    lista7.append(variacaoAngular)
print(lista7)

lista8 = []
for linha in ang:
    arredondamento = np.around(ang, decimals = 3)
    lista8.append(arredondamento)
print(lista8)