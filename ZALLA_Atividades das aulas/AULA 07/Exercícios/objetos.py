class Point:

    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY
    
    def getX(self):
        return self.x

    def getY(self):
        return self.y   

#####################

def distanceFromOrigin(self):
    return ((self.x ** 2) + (self.y ** 2)) ** 0.5

def __str__(self):
    return "x=" + str(self.x) + ", y=" + str(self.y)

def halfway(self, target):
    mx = (self.x + target.x)/2
    my = (self.y + target.y)/2
    return Point(mx,my)

#####################

p = Point(3,4)
q = Point(5,12)
mid = p.halfway(q)

print(mid)
print(mid.getX())
print(mid.getY())
