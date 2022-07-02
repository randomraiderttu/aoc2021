import os
import random
import math

PATHLIST = []

def ingestFile(fileName):
    """Reads the single line and returns a list

    Args:
        fileName (string): filename without path - path is assumed to be the same path as this script
    """
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),fileName)) as fileObject:
        lines = fileObject.readlines()

    tmpStringList = [list(x.strip()) for x in lines]

    tmpList = [list(map(int,i)) for i in tmpStringList]
    maxX = len(tmpList[0])
    maxY = len(tmpList)

    return tmpList, maxX, maxY

def checkMap(map, maxX, maxY):
    for x in range(100):
        randomX = random.randint(100, maxX-1)
        randomY = random.randint(100, maxY-1)

        originalX = randomX%100
        originalY = randomY%100

        xAdder = math.floor(randomX / 100)
        yAdder = math.floor(randomY / 100)

        print(f'Original point: map(y{originalY},x{originalX}) value: {map[originalY][originalX]} ** Adders(x:{xAdder}y:{yAdder}) - New Point: map(y{randomY},x{randomX}) value: {map[randomY][randomX]}')

        if map[randomY][randomX] != ((map[originalY][originalX] + xAdder + yAdder)%9 if (map[originalY][originalX] + xAdder + yAdder) > 9 else (map[originalY][originalX] + xAdder + yAdder)):
            print(f'FAILED: Original point: map(y{originalY},x{originalX}) value: {map[originalY][originalX]} ** Adders(x:{xAdder}y:{yAdder}) - New Point: map(y{randomY},x{randomX}) value: {map[randomY][randomX]}')

def amplifyMap(map, maxY, maxX):
    # for t in range(maxY, 5*maxY):
    #     map.append([])
    for yy in range(1,6):
        for y in range((yy-1)*maxY,yy*maxY):
            if y == len(map):
                tmpY = []
                for xxx in map[y-maxY][:maxX]:
                    tmpY.append(1 if xxx + 1 > 9 else xxx + 1)
                map.append(tmpY)
            for xx in range(1,5):
                tmpLine = []
                for x in range((xx-1)*maxX,xx*maxX):
                    tmpLine.append(1 if map[y][x] + 1 > 9 else map[y][x] + 1)
                map[y] += tmpLine

    # for i in map:
    #     print(i)


def exercise1(map, maxY, maxX):
    # Initialize risk map
    riskMap = []
    for y in range(maxY):
        tmp = [0 for x in range(maxX)]
        riskMap.append(tmp)

    for y in range(maxY):
        for x in range(maxX):
            if y == 0 and x == 0:
                riskMap[y][x] = map[y][x]
            elif y == 0 and x != 0:
                riskMap[y][x] = map[y][x] + riskMap[y][x-1]
            elif y != 0 and x == 0:
                riskMap[y][x] = map[y][x] + riskMap[y-1][x]
            elif y != 0 and x != 0:
                riskMap[y][x] = min(riskMap[y][x-1], riskMap[y-1][x]) + map[y][x]
            else:
                raise Exception('How did i get here?')

    # for t in riskMap:
    #     print(t)

    print('-------------------------------------------')
    print('Exercise 1')
    print(f'Lowest Risk Total: {riskMap[maxY-1][maxX-1] - riskMap[0][0]}')


def exercise2(map, maxY, maxX):
    amplifyMap(map, maxY, maxX)
    newMaxX = len(map[0])
    newMaxY = len(map)

    print('x', newMaxX, 'y', newMaxY)
    print(f'last element is {map[newMaxY-1][newMaxX-1]}')

    checkMap(map, newMaxX, newMaxY)

    # Initialize risk map
    riskMap = []
    for y in range(newMaxY):
        tmp = [0 for x in range(newMaxX)]
        riskMap.append(tmp)


    for y in range(newMaxY):
        for x in range(newMaxX):
            if y == 0 and x == 0:
                riskMap[y][x] = map[y][x]
            elif y == 0 and x != 0:
                riskMap[y][x] = map[y][x] + riskMap[y][x-1]
            elif y != 0 and x == 0:
                riskMap[y][x] = map[y][x] + riskMap[y-1][x]
            elif y != 0 and x != 0:
                riskMap[y][x] = min(riskMap[y][x-1], riskMap[y-1][x]) + map[y][x]
            else:
                raise Exception('How did i get here?')

    with open('result.txt', 'w') as f:
        for y in riskMap:
            l = ''
            for x in y:
                l += str(x).ljust(7)
            f.write(l + "\n")
        
    # for t in riskMap:
    #     print(t)

    print('-------------------------------------------')
    print('Exercise 2')
    print(f'Lowest Risk Total: {riskMap[newMaxY-1][newMaxX-1] - riskMap[0][0]}')

if __name__ == '__main__':
    # input, maxX, maxY = ingestFile(fileName='sampleInput.txt')
    input, maxX, maxY = ingestFile(fileName='scottInput.txt')
    # input, maxX, maxY = ingestFile(fileName='inputFile.txt')

    exercise1(input, maxY, maxX)

    exercise2(input, maxY, maxX)