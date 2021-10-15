############## IMPORTS #####################
from itertools import product
import random
import math
import numpy as np
###########################################

########## FUNCTION ABBREVIATIONS ########
ra=random.random
rn=range
fl=math.floor
ce=math.ceil
##########################################

## Creates a unique hash given a normalized tuple (x,y). Note that for this hash to be unique, 0<=x<c, 0<=y<c must be ensured.
getHash = lambda p,c          : p[1]*c+p[0]                                                                                     

## Generates a set of points such that these points can be 'masked' with a starting point to obtain all possible neighbouring cells
getCircleMask = lambda r,c,rs : set(filter(lambda p:np.hypot(*p)<=r*c+1,[(x,y) for x,y in product(rn(-rs,rs+1),rn(-rs,rs+1))])) 

## This function does the masking described by the above function, whilst also ensuring the uniqueness condition of getHash
addMask = lambda h, c, mask   : [h+getHash(m,c) for m in filter(lambda p: (h%c+p[0]>=0 and h%c+p[0]<c and h//c+p[1]>=0 and h//c+p[1]<c),mask)]

class Point: ## This class represents a point, and has some useful methods attributed to it
    def __init__(self, x, y, payload = None): self.x, self.y, self.payload = x,y,payload ## Initialises point. Payload is for any extra info needing to be supplied 
    def normalize(self, cellSize): return (fl(self.x*cellSize), fl(self.y*cellSize))    ## Returns the point in a hashable form
    def dist(self, other): return np.hypot(self.x-other.x,self.y-other.y)               ## Returns the distance to another point, proved other is an object of class type Point

class Cell: ## A data structure class. Makes it easy to create new keys in dictionaries by using 'put'. 'putted' is a boolean return that has use.
    def __init__(self)       : self.data = {}   ## Initialises cell. 
    def put(self, key, value): self.data[key] = self.data.get(key, []) + (value if type(value) is list else [value]) ## Adds a value to the list attributed to a key.
    def putted(self, key)    : return key in self.data.keys()   ## If there are any values attributed to a key, then this will return true.
    def get(self, key)       : return self.data.get(key, [])    ## Gets the values attributed to a key.

class Space: ## This object is used to store all data about neighbouring cells and which points are stored in each cell.
    def __init__(self, radius): ## Initialises a space.
        self.radius, self.cellSize, self.cellMap, self.cache = radius, fl(1/radius), Cell(), Cell()
        self.mask        = getCircleMask(self.radius, self.cellSize, ce(1+self.radius*self.cellSize)) ## Gets the mask for the current space.
        self.getPointHash= lambda p : getHash(p.normalize(self.cellSize),self.cellSize)               ## Normalizes and hashes a point, depends on cellSize and is relative to class
    
    def insert(self, point): ## Put a point into the space.
        pointHash = self.getPointHash(point) 

        self.cellMap.put(pointHash, point)
        if not self.cache.putted(pointHash): ## If the neighbours of the cell the point was put into have not been found, find them.
            self.cache.put(pointHash, addMask(pointHash, self.cellSize, self.mask))
    
    def getNeighbours(self, point): ## Gets the neighbouring points as a generator, given any point.
        for nHash in self.cache.get(self.getPointHash(point)):
            for nCell in self.cellMap.get(nHash):
                yield nCell


## Helpful exceptions for testing
class LogicError(Exception):
    def __str__(self): return "Logic error occured."
class RadiusTooLarge(Exception):
    def __str__(self): return "Radius is too large."
class RadiusTooSmall(Exception):
    def __str__(self): return "Radius is too small."
