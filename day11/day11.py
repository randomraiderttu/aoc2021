import os

def ingestFile(fileName):
    """Reads the single line and returns a list

    Args:
        fileName (string): filename without path - path is assumed to be the same path as this script
    """
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),fileName)) as fileObject:
        lines = fileObject.readlines()

    tmpStringList = [list(x.strip()) for x in lines]

    tmpList = [list(map(int,i)) for i in tmpStringList]

    return tmpList

def flash(input, y, x, flashList):
    for yy in range(y-1,y+2):        
        for xx in range(x-1,x+2):
            curPoint = {'y': yy,'x' :xx}
            try:
                # higher bounds will error, negatives will find a value from the end, so i have to continue past them
                if yy < 0 or xx < 0:
                    continue
                if y != yy or x != xx:
                    input[yy][xx] += 1
                    if input[yy][xx] > 9 and curPoint not in flashList:
                        flashList.append(curPoint)
                        flash(input, yy, xx, flashList)
            except IndexError:
                # trapping for index errors makes it easier than accounting for the boundaries
                pass

def exercise(input, steps, exerciseNum):
    flashScore = 0

    for i in range(steps):
        flashList = []

        # Step A - add one
        for y, yv in enumerate(input):
            for x, xv in enumerate(yv):
                input[y][x] += 1

        # Step B - Start flashin
        for y, yv in enumerate(input):
            for x, xv in enumerate(yv):
                curPoint = {'y': y, 'x': x}
                if input[y][x] > 9 and curPoint not in flashList:
                    flashList.append({'y': y, 'x': x})
                    flash(input, y, x, flashList)

        flashScore += len(flashList)

        for t in flashList:
            input[t['y']][t['x']] = 0

        if len(flashList) == 100 and exerciseNum == 2:
            print('------------------------------------')
            print(f'Step {i+1} results in all numbers flashing.')
            return 0

    if exerciseNum == 1:
        print('------------------------------------')
        print(f'Exercise 1 - Flashscore = {flashScore}')
    elif exerciseNum == 2:
        print('------------------------------------')
        print(f'Test failed, {steps} was not enough to reach synchronization, try a higher number')

if __name__ == '__main__':
    input = ingestFile(fileName='inputFile.txt')
    # Have to use this functionality to copy because it's 2D
    #   copy command didn't work nor did [:]
    input2 = [x[:] for x in input]

    # exercise 1
    exercise(input, 100, 1)

    # exercise 2
    exercise(input2, 1000, 2)