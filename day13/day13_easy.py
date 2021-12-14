import os

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

def exercise1(instructions, points):
    axis = instructions[0]['axis']
    foldLine = instructions[0]['value']

    if axis == 'x':
        for p in points:
            if p['x'] > foldLine:
                p['x'] = foldLine - (p['x'] - foldLine)

    if axis == 'y':
        for p in points:
            if p['y'] > foldLine:
                p['y'] = foldLine - (p['y'] - foldLine)

    
    # dedupe the list of points
    result = [dict(t) for t in {tuple(p.items()) for p in points}]
    
    dotCount = len(result)
    

    print('-------------------------------------')
    print('Exercise 1')
    print(f'Exercise 1 Dot Count: {dotCount}')

def exercise2(instructions, points):
    maxY = 0
    maxX = 0

    for i in instructions:
        axis = i['axis']
        foldLine = i['value']
        
        if axis == 'x':
            maxX = foldLine
            for p in points:
                if p['x'] > foldLine:
                    p['x'] = foldLine - (p['x'] - foldLine)

        if axis == 'y':
            maxY = foldLine
            for p in points:
                if p['y'] > foldLine:
                    p['y'] = foldLine - (p['y'] - foldLine)

    
    # dedupe the list of points
    result = [dict(t) for t in {tuple(p.items()) for p in points}]

    print('-------------------------------------')
    print('Exercise 2')
    for y in range(maxY):
        line = ''
        for x in range(maxX):
            if {'x': x, 'y': y} in result:
                line += '#'
            else:
                line += ' '
        print(line)


if __name__ == '__main__':
    points, maxX, maxY, instructions = ingestFile(fileName='inputFile.txt')

    # g = Grid(points, maxX, maxY)

    exercise1(instructions, points)

    exercise2(instructions, points)
