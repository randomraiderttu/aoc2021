import os

def ingestFile(fileName):
    """Reads the single line and returns a list

    Args:
        fileName (string): filename without path - path is assumed to be the same path as this script
    """
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),fileName)) as fileObject:
        line = fileObject.read()

    tmpList = line.strip().split(',')
    resultList = [int(x) for x in tmpList]

    return resultList

def exercise1(input, greatestPosition, leastPosition):
    """Determine the point between greatest and least positions that allow the crabs
       to use the least amount of fuel aligning to a common position assuming movement
       results in spending 1 fuel

    Args:
        input (list): List of horizontal locations of crabs
        greatestPosition (integer): Upper boundary for the search area
        leastPosition (integer): Lower boundary for the horizontal search area
    """
    # Hate this, but it was the fastest way to choose an upper bound which the first
    #   total value would be lower than to start comparing
    leastTotal = 999999999999
    
    for x in range(leastPosition, greatestPosition+1):
        total = 0
        for crab in input:
            total += abs(x - crab)
        leastTotal = min(total, leastTotal)

    print('-------------------------------------------')
    print('Exercise1')
    print(f'Least Total: {leastTotal}')
    print()

def exercise2(input, greatestPosition, leastPosition):
    """Determine the point between greatest and least positions that allow the crabs
       to use the least amount of fuel aligning to a common position assuming movement
       results in spending incrementally more fuel per move.

    Args:
        input (list): List of horizontal locations of crabs
        greatestPosition (integer): Upper boundary for the search area
        leastPosition (integer): Lower boundary for the horizontal search area
    """
    # Hate this, but it was the fastest way to choose an upper bound which the first
    #   total value would be lower than to start comparing
    leastTotal = 999999999999
    
    for x in range(leastPosition, greatestPosition+1):
        total = 0
        for crab in input:
            dist = abs(x - crab)
            total += ((dist*(dist+1))/2)
        leastTotal = min(total, leastTotal)

    print('-------------------------------------------')
    print('Exercise2')
    print(f'Least Total: {leastTotal}')
    print()

if __name__ == '__main__':
    input = ingestFile(fileName='inputFile.txt')

    # Get greatest and least positions to act as the boundaries for which we'll search
    #   for acceptable middle points
    greatestPosition = max(input)
    leastPosition = min(input)

    exercise1(input, greatestPosition, leastPosition)

    exercise2(input, greatestPosition, leastPosition)
