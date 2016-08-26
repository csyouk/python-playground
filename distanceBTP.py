import math

def absoluteDistance(a,b):
    print 'approach to a absFct()'
    if a<b:
        return b-a
    else:
        return a-b

def square(x):
    return x**2

def squareRoot(x):
    return math.sqrt(x)


def distanceBetweenTwoPoints(x1,y1,x2,y2):
    x = absoluteDistance(x1,x2)
    y = absoluteDistance(y1,y2)
    squaredX = square(x)
    squaredY = square(y)
    sum = squaredX + squaredY
    return squareRoot(sum)

print distanceBetweenTwoPoints(0,0,3,4)
