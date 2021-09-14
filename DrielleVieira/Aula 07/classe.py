# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 09:10:59 2021

@author: driellevieira
"""

#Aula 07
#Classe e Funções

#Classe

class Point:
    def __init__(self,initX,initY):
        self.x = initX
        self.y = initY

    def getX(self):
        return self.x
    def gety(self):
        return self.y
    
    def distOrig(self):
        return ((self.x**2) + (self.y**2)) ** 0.5

    def __str__(self):
        return "x=" + str(self.x) + ",y=" + str(self.y)

    def half(self,target):
        mx = (self.x + target.x)/2
        my= (self.y + target.y)/2
        return Point(mx, my)

p = Point(3,4)
q = Point (5,12)
mid = p.half(q)

print(mid)
print(mid.getX())
print(mid.gety())