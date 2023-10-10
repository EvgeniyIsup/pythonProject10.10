# import math
# def circle(r):
#     return math.pi*r**2

import random
def generateList(size):
    array = []
    for i in range(size):
        array.append(random.randint(1,20))
    return array
def unique(array:list):
    array = set(array)
    return list(array)

def counter(array):
    return len(array)