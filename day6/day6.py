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

def calculateGrowth(fishList, days):
    for x in range(days):
        numFish = len(fishList)
        # Troubleshooting code only
        # print(f'Day: {x}  - Total: {numFish}')
        for key, fish in enumerate(fishList[:numFish]):
            fishList[key] -= 1
            if fishList[key] == -1:
                fishList.append(8)
                fishList[key] = 6
    return len(fishList)

def exercise1(fishList):
    """Solves exercise 1

    Args:
        inputList (list): Takes in the list of integers from the input list
    """
    total = calculateGrowth(fishList, 80)

    print('-----------------------------------------')
    print('Exercise1')
    print(f'Total Lanternfish: {total}')

def exercise2(fishList):
    """Solves exercise 2

    Args:
        inputList (list): Takes in the list of integers from the input list
    """
    total = 0

    # Set the dict based on the input
    fishDict = {}
    for x in fishList:
        fishDict[x] = (fishDict.get(x) or 0) + 1

    # Loop through the number of days adjusting each group of lanternfish by how many days old they are
    #   and creating new lanternfish as needed.
    # For each iteration, create a new tmpDict based on the current fishDict and replace it at the end
    for r in range(256):
        tmpDict = {}
        tmpDict[0] = fishDict.get(1) or 0
        tmpDict[1] = fishDict.get(2) or 0
        tmpDict[2] = fishDict.get(3) or 0
        tmpDict[3] = fishDict.get(4) or 0
        tmpDict[4] = fishDict.get(5) or 0
        tmpDict[5] = fishDict.get(6) or 0
        tmpDict[6] = (fishDict.get(0) or 0) + (fishDict.get(7) or 0)
        tmpDict[7] = fishDict.get(8) or 0
        tmpDict[8] = fishDict.get(0) or 0

        # Troubleshooting only
        # total = 0
        # for t in range(9):
        #     total += tmpDict[t]

        fishDict = tmpDict
        # print(f'{r} - Total: {total} - {sorted(fishDict.items())}')

    # Reinitialize to 0 if i'm troubleshooting and uncomment my troubleshooting code above
    # total = 0
    for value in fishDict.values():
        total += value


    print('-----------------------------------------')
    print('Exercise2')
    print(f'Total Lanterfish: {total}')


if __name__ == '__main__':
    input = ingestFile(fileName='inputFile.txt')
    inputB = input.copy()

    exercise1(input)

    exercise2(inputB)