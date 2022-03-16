import math
import random
import population
import time


def main(squareNumber, minSquare, maxSquare, minDistance, W, H):
    """
    squareNumber = 50
    minSquare = 10
    maxSquare = 200
    minDistance = 10
    W, H = 1000, 1000
    """
    
    timeout_start = time.time()
    timeout = 10

    listSquares = []
    class Square():
        def __init__(self, x, y, width):
            self.center = [x, y]
            self.width = width
        def set(self):
            self.x1y1 = [self.center[0]-self.width//2, self.center[1]-self.width//2]
            self.x2y2 = [self.center[0]+self.width//2, self.center[1]+self.width//2]
    def checkDistance(square1, square2):

        distance = math.sqrt((square1.center[0] - square2.center[0])**2 + (square1.center[1] - square2.center[1])**2)
        #mustDistance = square1.width*math.sqrt(2) + minDistance + square2.width*math.sqrt(2)
        mustDistance = square1.width//2*math.sqrt(2) + minDistance + square2.width//2*math.sqrt(2)
        if distance <= mustDistance:
            return False
        else:
            return True

    i = 0
    while i < squareNumber and time.time() < timeout_start + timeout:
        square = Square(random.randint(-W//10, W), random.randint(-H//10, H), random.randint(minSquare, maxSquare))
        if len(listSquares) == 0:
            square.set()
            listSquares.append(square)
            i+=1
            continue    

        add = True
        for each in listSquares:
            if checkDistance(square, each) == False:
                add = False
                break

        if add:
            square.set()
            listSquares.append(square)
            i+=1

    if i < squareNumber:
        return False
    
    return population.main(listSquares, W, H)

    



