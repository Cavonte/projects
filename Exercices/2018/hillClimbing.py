import random
import os
import math

inputMatrix = []
with open('mat','r') as file:
    for currentLine in file:
        localList = []
        currentLine = currentLine.split('  ')
        for number in currentLine:
            if int(number) >=0:
                localList.append(int(number))

        inputMatrix.append(localList)

# O(10) constant
def isLandValid(posX, posY, length, width, height):
    adjustedLength = length - 1
    uwidth = width - 1
    return posX >= 0 and posX <= uwidth and posY >= 0 \
           and posY <= uwidth and posX + adjustedLength >= 0 \
           and posX + adjustedLength <= uwidth \
           and posY + adjustedLength >= 0 \
           and posY + adjustedLength <= uwidth


# O(n^2) where n is the size of the land being scored
def getScore(posX, posY, landSize, inputMatrix):
    if isLandValid(posX, posY, landSize, len(inputMatrix[0]), len(inputMatrix)) == False:
        return 0
    landPrice = 0
    for xCoord in range(posX, posX + landSize):
        for yCoord in range(posY, posY + landSize):
            landPrice += inputMatrix[xCoord][yCoord]
    return landPrice

def getHeuristic(posX, posY, landSize, inputMatrix, budget,wantedAmount):
    if isLandValid(posX, posY, landSize, len(inputMatrix[0]), len(inputMatrix)) == False:
        return float("inf")
    count = 0
    for xCoord in range(posX, posX + landSize):
        for yCoord in range(posY, posY + landSize):
          # count += abs(wantedAmount - inputMatrix[xCoord][yCoord])
          count += wantedAmount - inputMatrix[xCoord][yCoord]


    return count



# inputMatrix = [[4, 6, 7, 3, 6, 2, 3, 2, 7],
#                [3, 5, 2, 1, 3, 6, 4, 2, 2],
#                [3, 5, 2, 1, 6, 4, 7, 3, 2],
#                [6, 3, 1, 7, 5, 2, 7, 7, 0],
#                [7, 1, 5, 3, 4, 2, 6, 1, 2],
#                [5, 2, 3, 7, 1, 6, 4, 5, 5],
#                [6, 5, 7, 3, 2, 4, 1, 3, 8],
#                [1, 8, 6, 5, 2, 7, 3, 4, 4],
#                [3, 9, 2, 8, 6, 7, 5, 4, 1]]

linearDictionaries = []
randomDictionaries = []
budget = 70
tolerance = 15;
highestLandPriceLinear = 0
highestLandPriceRandom = 0

width = len(inputMatrix[0])
height = len(inputMatrix)
linearCounter = 0
randomCounter = 0


for landSize in range(0, width):
    landSize = (width - 1) - landSize
    if landSize <= 1:
        break

    # Linear
    for xCoord in range(0, width):
        for yCoord in range(0, height):
            score = getScore(xCoord, yCoord, landSize, inputMatrix)
            linearCounter += 1
            if score != None:
                # print(score,xCoord,yCoord,landSize)
                if score > budget - tolerance and score <= budget:
                    linearDictionaries.append(
                        {'x': xCoord, 'y': yCoord, 'landSize': landSize, 'score': score, 'method': 'linear'})
                if score > highestLandPriceRandom:
                    highestLandPriceLinear = score

    # Random
    wantedAmount = math.floor(budget / (landSize * landSize))
    for attempts in range(0, 30):
        while True:
            randomCoordinateX = int.from_bytes(os.urandom(1), byteorder='little')
            randomCoordinateY = int.from_bytes(os.urandom(1), byteorder='little')
            winningCoordinate = {'x': randomCoordinateX, 'y': randomCoordinateY, 'landSize': landSize,
                                 'method': 'random', 'heur' : 1000000,
                                 'score': getScore(int(randomCoordinateX/10), int(randomCoordinateY/10), landSize, inputMatrix)}
            if winningCoordinate['score'] > 0 and randomCoordinateX <= width and randomCoordinateY <= height:
                break
        # print(winningCoordinate['x'],winningCoordinate['y'])
        while (True):
            previousCoord = winningCoordinate
            for x in range(-1, 2):
                for y in range(-1, 2):
                    randomCounter += 1
                    newX = winningCoordinate['x'] + x
                    newY = winningCoordinate['y'] + y
                    score = getScore(newX, newY, landSize, inputMatrix)
                    heur = getHeuristic(newX, newY, landSize, inputMatrix,budget,wantedAmount)
                    if heur < winningCoordinate['heur'] and score <= budget:
                        winningCoordinate = {'x': newX, 'y': newY, 'landSize': landSize, 'score': score,'heur':heur,
                                             'method': 'random'}
                    if score > highestLandPriceRandom:
                        highestLandPriceRandom = score

            if (previousCoord == winningCoordinate):
                break
        if winningCoordinate['score'] > budget - tolerance and winningCoordinate['score'] <= budget:
            randomDictionaries.append(winningCoordinate)

# print(highestLandPriceLinear)
# print(linearCounter)
localLinearTop = 0
for land in linearDictionaries:
    # print(land)
    if land['score'] > localLinearTop:
        localLinearTop = land['score']

# print(highestLandPriceRandom)
# print(randomCounter)
localRandomTop = 0
for land in randomDictionaries:
    # print(land)
    if land['score'] > localRandomTop:
        localRandomTop = land['score']

print(linearCounter)
print(localLinearTop)
print(randomCounter)
print(localRandomTop)
