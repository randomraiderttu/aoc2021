import os

CAVEPATHS = []

class Cave:
    """Object representing a cave, its size and its connecting caves
    """

    def __init__(self, caveName) -> None:
        self.caveName = caveName
        if caveName == caveName.upper():
            self.caveSize = 1
        else:
            self.caveSize = 0
        self.connectedCaves = []

    def addConnectedCave(self, connectingCaveName):
        if connectingCaveName not in self.connectedCaves:
            self.connectedCaves.append(connectingCaveName)



def ingestFile(fileName):
    """Reads the single line and returns a list

    Args:
        fileName (string): filename without path - path is assumed to be the same path as this script
    """
    resultList = []
    
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),fileName)) as fileObject:
        lines = fileObject.readlines()

    for x in lines:
        caveCon = x.strip().split('-')
        resultList.append(caveCon)

    return resultList

def populateCaves(input):
    tmpCaves = {}
    for x in input:
        for y in range(2):
            if x[y] not in tmpCaves.keys():
                # add it
                newCave = Cave(x[y])
                tmpCaves[x[y]] = newCave

            # Add the 
            if y == 0:
                tmpCaves[x[y]].addConnectedCave(x[1])
            else:
                tmpCaves[x[y]].addConnectedCave(x[0])

    return tmpCaves

def getSmallCaveRepeatsInPath(curPath, allowedMoves):
    if allowedMoves == 1:
        # short circuit, if allowed moves to small caves is 1, you can move to all small caves once
        # this is really only to restrict the allowed moves to small caves more than once for ONE small cave
        return 0
    smallCaveRepeatCount = 0
    counts = dict()
    for i in curPath:
        counts[i] = counts.get(i, 0) + 1

    for t in counts.keys():
        if t == t.lower() and counts[t] >= allowedMoves:
            smallCaveRepeatCount += 1

    return smallCaveRepeatCount

def moveCaves(curCave, curPath, caves, allowedMoves=1):
    numDoubles = 0

    if curCave.caveName == 'end':
        # create value copy and save to global list and bail
        tmp = curPath[:]
        CAVEPATHS.append(tmp)
        return 0

    for x in curCave.connectedCaves:
        testPath = curPath[:]
        testPath.append(caves[x].caveName)
        if (caves[x].caveSize == 0 and testPath.count(caves[x].caveName) > allowedMoves) or \
            getSmallCaveRepeatsInPath(testPath, allowedMoves) > 1 or x == 'start':
            pass
        else:
            # Create value copy to send to the next call
            tmp = curPath[:]
            tmp.append(caves[x].caveName)
            moveCaves(caves[x], tmp, caves, allowedMoves)

def exercise1(caves):
    tmp = ['start']
    moveCaves(caves['start'], tmp, caves)

    # for troubleshooting only
    # for t in CAVEPATHS:
    #     print(t)

    print('-------------------------------------------')
    print('Exercise 1')
    print(f'Total Cave Paths: {len(CAVEPATHS)}')

def exercise2(caves):
    total = 0

    # Restart cavepaths for exercise 2
    CAVEPATHS.clear() 
    tmp = ['start']
    moveCaves(caves['start'], tmp, caves, 2)


    # # for troubleshooting only
    # for t in CAVEPATHS:
    #     print(t)

    print('-------------------------------------------')
    print('Exercise 2')
    print(f'Total Cave Paths: {len(CAVEPATHS)}')

if __name__ == '__main__':
    input = ingestFile(fileName='inputFile.txt')

    caves = populateCaves(input)

    # for key, value in caves.items():
    #     print(key, ' - ', value.connectedCaves, ' - ', value.caveSize)

    exercise1(caves)

    exercise2(caves)