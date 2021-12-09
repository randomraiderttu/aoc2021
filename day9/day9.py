import os

class lowPoint:
    """Class that holds the lowpoint coordinates and it's basin coordinates
    """
    def __init__(self, cell) -> None:
        self.cell = cell
        self.basinList = []
        self.basinTotal = -1

    def addToBasin(self, cell):
        # Had to create this so you don't get dupes in your basin list
        # You can't convert a list of Dicts to a set - it's unhashable
        if cell not in self.basinList:
            self.basinList.append(cell)

    def calculateBasinTotal(self):
        self.basinTotal = len(self.basinList)


def ingestFile(fileName):
    """Reads the single line and returns a list

    Args:
        fileName (string): filename without path - path is assumed to be the same path as this script
    """
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),fileName)) as fileObject:
        lines = fileObject.readlines()

    tmpStringList = [list(x.strip()) for x in lines]

    tmpList = [list(map(int,i)) for i in tmpStringList]

    xBoundary = len(tmpList[0]) - 1
    yBoundary = len(tmpList) - 1

    return tmpList, xBoundary, yBoundary

def isLowPoint(map, xMax, yMax, rKey, cKey):
    evalPoint = map[rKey][cKey]

    evalList = []
    # If it isn't row 1, I can check the number above it
    if rKey != 0:
        evalList.append(map[rKey-1][cKey])
    # If it isn't the last row, I can check the number below it
    if rKey != yMax:
        evalList.append(map[rKey+1][cKey])
    # If it isn't the first column, I can check the column to the left of it
    if cKey != 0:
        evalList.append(map[rKey][cKey-1])
    # If it isn't the last column, I can check the column to the right of it
    if cKey != xMax:
        evalList.append(map[rKey][cKey+1])

    if all(evalPoint < x for x in evalList):
        return True
    else:
        return False

def findBasin(map, xMax, yMax, lp, curCell):
    # curCell is a dict {'x': 0, 'y': 0} format
    
    # Setting these values here makes this a shit ton more readable
    curVal = map[curCell['y']][curCell['x']]
    curX = curCell['x']
    curY = curCell['y']

    # If the current cell is an 8, 9's can't be in basins, adjacent 8s aren't higher
    #   and any other value would be lower so it doesn't apply
    if curVal == 8:
        return 0

    # If it isn't row 1, I can check the number above it
    if curY != 0:
        if map[curY-1][curX] > curVal and \
           map[curY-1][curX] != 9:
            lp.addToBasin({'x': curX, 'y': curY-1})
            findBasin(map, xMax, yMax, lp, {'x': curX, 'y': curY-1})

    # If it isn't the last row, I can check the number below it
    if curY != yMax:
        if map[curY+1][curX] > curVal and \
           map[curY+1][curX] != 9:
            lp.addToBasin({'x': curX, 'y': curY+1})
            findBasin(map, xMax, yMax, lp, {'x': curX, 'y': curY+1})

    # If it isn't the first column, I can check the column to the left of it
    if curX != 0:
        if map[curY][curX-1] > curVal and \
           map[curY][curX-1] != 9:
            lp.addToBasin({'x': curX-1, 'y': curY})
            findBasin(map, xMax, yMax, lp, {'x': curX-1, 'y': curY})

    # If it isn't the last column, I can check the column to the right of it
    if curX != xMax:
        if map[curY][curX+1] > curVal and \
           map[curY][curX+1] != 9:
            lp.addToBasin({'x': curX+1, 'y': curY})
            findBasin(map, xMax, yMax, lp, {'x': curX+1, 'y': curY})

    return 0

def exercise1(map, xMax, yMax, lowPointList):
    riskTotal = 0
    for rKey, rVal in enumerate(map):
        for cKey, cVal in enumerate(rVal):
            if isLowPoint(map, xMax, yMax, rKey, cKey):
                riskTotal += (cVal+1)
                # Identifying these for exercise2
                tmp = lowPoint({'x':cKey, 'y':rKey})
                tmp.addToBasin(tmp.cell)
                lowPointList.append(tmp)

    print('-------------------------------------')
    print('Exercise 1')
    print(f'Risk Level Total for Map is: {riskTotal}')

def exercise2(map, xMax, yMax, lowPointList):
    # Find the basis and calculate the total basin for that lowpoint
    for lp in lowPointList:
        findBasin(map, xMax, yMax, lp, lp.cell)
        lp.calculateBasinTotal()

    # Create a list of just basin totals, then reverse it and multiply the first 3
    tmp = [x.basinTotal for x in lowPointList]
    sortedBasinTotals = sorted(tmp, reverse=True)
    answer = sortedBasinTotals[0] * sortedBasinTotals[1] * sortedBasinTotals[2]

    print('-------------------------------------')
    print('Exercise 2')
    print(f'3 Largest Basins Multiplied: {answer}')

if __name__ == '__main__':
    input, xMax, yMax = ingestFile(fileName='inputFile.txt')
    lowPointList = []

    exercise1(input, xMax, yMax, lowPointList)

    exercise2(input, xMax, yMax, lowPointList)
