# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 11:09:28 2021

@author: driellevieira
"""

#Aula 05 - Dicionários

dicionario = {}
# dicionario = dict()
dicionario["Biblioteca"] = {"Estantes": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "Livros":[]}
# print(dicionario)
# print(dicionario["Biblioteca"])
# print(dicionario["Biblioteca"]["Estantes"])
# print(dicionario["Biblioteca"]["Estantes"][0])
#print(dicionario["Biblioteca"]["Estantes"]["Livros"])

# print (dicionario.keys())
# print (dicionario["Biblioteca"].keys())

print(dicionario["Biblioteca"].items())
print(len(dicionario["Biblioteca"]))
print(dicionario.get("Biblioteca", None))
print(dicionario.get("Estantes", None))