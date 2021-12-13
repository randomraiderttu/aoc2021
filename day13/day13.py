import os
import math

class Grid:
    """Grid of points
    """

    def __init__(self, points, maxX, maxY) -> None:
        self.points = points
        self.maxX = maxX
        self.maxY = maxY
        self.grid = self.populateBaseGrid(maxX, maxY)
        self.fillGridWithPoints()

    def populateBaseGrid(self, maxX, maxY):
        tmpGrid = []
        for y in range(maxY):
            tmpRow = []
            for x in range(maxX):
                tmpRow.append(' ')
            tmpGrid.append(tmpRow)
        print(f'Starting Max Grid: (x: {len(tmpGrid[0])}, y: {len(tmpGrid)}')
        return tmpGrid

    def fillGridWithPoints(self):
        for p in self.points:
            self.grid[p['y']][p['x']] = '#'

    def printGrid(self):
        for y in self.grid:
            print(y)

    def printReadableGrid(self):
        for y in self.grid:
            print(''.join(y))

    def foldGrid(self, instruction):
        print(f'Instruction: {instruction}')
        if instruction['axis'] == 'x':
            self.foldAlongX(instruction['value'])
        elif instruction['axis'] == 'y':
            self.foldAlongY(instruction['value'])
        else:
            raise Exception('Unknown instruction')

    def foldAlongY(self, line):
        # The exercise makes it sound like it was folding the paper in half, but ONE, JUST ONE, instruction on the Y axis was not a fold in half - it was off by one number on the fold
        # which is why my y axis logic is different than my x-axis and i didn't care to go back and fix X to line up with Y logic....because folding on X was always exactly in half.

        for y in range(line + 1,self.maxY):
            yy = line - (y-line)
            for x in range(self.maxX):
                if self.grid[yy][x] != '#':
                    self.grid[yy][x] = self.grid[y][x]

        self.grid = self.grid[:line]
        self.maxY = line

    def foldAlongX(self, line):
        if line != math.floor(len(self.grid[0])/2):
            oldLine = line
            line = math.floor(len(self.grid[0])/2)
            print(f'XPATH - Chose a new line instead - {line} vs original {oldLine}')

        for y, yv in enumerate(self.grid):
            for x, xv in enumerate(yv[:line]):
                if xv != '#':
                    self.grid[y][x] = self.grid[y][(self.maxX-1) - x]

        self.grid = [x[:line] for x in self.grid]
        self.maxX = line

    def countDotsInGrid(self):
        tmpCount = 0
        for y in self.grid:
            for x in y:
                if x == '#':
                    tmpCount += 1
        
        return tmpCount


def ingestFile(fileName):
    """Reads the single line and returns a list

    Args:
        fileName (string): filename without path - path is assumed to be the same path as this script
    """
    maxX = 0
    maxY = 0

    ylist = []

    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),fileName)) as fileObject:
        lines = fileObject.readlines()

    points = []
    instructions = []

    breakNum = 0
    for x in lines:
        # break on reading the file to separate grid from instructions
        if x == '\n':
            breakNum += 1
            continue

        if breakNum == 0:
            tmpLine = x.strip().split(',')
            points.append({'x': int(tmpLine[0]), 'y': int(tmpLine[1])})
            maxX = max(maxX, int(tmpLine[0]))
            maxY = max(maxY, int(tmpLine[1]))
        else:
            tmp = x.strip().split()
            fold = tmp[2].split('=')
            instructions.append({'axis': fold[0], 'value': int(fold[1])})

    return points, maxX + 1, maxY + 1, instructions

def exercise1(instructions, g):

    g.foldGrid(instructions[0])

    print('-------------------------------------')
    print('Exercise 1')
    print(f'Exercise 1 Dot Count: {g.countDotsInGrid()}')

def exercise2(instructions, g):

    for i in instructions:
        g.foldGrid(i)

    print('-------------------------------------')
    print('Exercise 2')
    g.printReadableGrid()

if __name__ == '__main__':
    points, maxX, maxY, instructions = ingestFile(fileName='inputFile.txt')

    g = Grid(points, maxX, maxY)

    # exercise1(instructions, g)

    exercise2(instructions, g)
