from auto import *
from classes import *

@timer
def spatialHash(myPoints, radius):
    count =0
    mySpace = Space(radius)

    for myPoint in myPoints:
        mySpace.insert(myPoint)
    for myPoint in myPoints:
        for neighbourPoint in mySpace.getNeighbours(myPoint):
            if myPoint.dist(neighbourPoint) <= radius:
                count += 1    
    return count

@timer
def doubleLoop(myPoints, radius): ## The default way of approach
    count =0
    for m in myPoints:
        for n in myPoints:
            if m.dist(n)<=radius:
                count+=1
    return count


def runTest(numPoints, radius):
    if radius >= 1/3:
        raise RadiusTooLarge
    elif radius <= 0:
        raise RadiusTooSmall

    myPoints = [Point(ra(),ra()) for _ in range(numPoints)]

    spatialHashRes, spatialHashTime =spatialHash(myPoints,radius)
    doubleLoopRes, doubleLoopTime   =doubleLoop(myPoints,radius)

    if spatialHashRes != doubleLoopRes:
        raise LogicError
    else:
        return (doubleLoopTime/spatialHashTime), f"Spatial Hashing : {spatialHashTime:.4f}s\nDouble Looping : {doubleLoopTime:.4f}s" ## Speed-up










