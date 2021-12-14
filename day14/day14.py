import os

def ingestFile(fileName):
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),fileName)) as fileObject:
        lines = fileObject.readlines()

    resultList = [x.strip() for x in lines]
    
    # Get the bingo number call list
    template = resultList[0].strip()

    cipher = {}

    for x in resultList[2:]:
        tmp = x.split(' -> ')
        cipher[tmp[0]] = tmp[0][0] + tmp[1] + tmp[0][1]

    return template, cipher

def genStringPairList(inString):
    tmpString = []
    for i in range(len(inString)):
        if i == (len(inString) - 2):
            tmpString.append(inString[i] + inString[i+1])
            break
        else:
            tmpString.append(inString[i] + inString[i+1])

    return tmpString


def exercise1(template, cipher, steps):
    curString = template[:]

    for i in range(steps):
        newStringList = genStringPairList(curString)
        print(f'Step {i} - Broken Out String Length is: {len(newStringList)}')
        # reinitialize to empty so we can build a new one
        curString = ''
        for key, pair in enumerate(newStringList):
            newStringList[key] = cipher[pair]

        for key, value in enumerate(newStringList):
            if key == (len(newStringList) - 1):
                curString += value
            else:
                curString += value[:2]

    letterCount = dict()
    for i in curString:
        letterCount[i] = letterCount.get(i, 0) + 1

    print(letterCount)

    maxElementCount = max(letterCount.values())
    minElementCount = min(letterCount.values())

    print('-----------------------------------------')
    print('Exercise1')
    print(f'Difference in max min values is: {maxElementCount - minElementCount}')

def exercise2(template, cipher, steps):
    tmpList = genStringPairList(template)
    dPairs = {}

    result = {}
    for l in template:
        result[l] = result.get(l, 0) + 1

    for i in tmpList:
        dPairs[i] = dPairs.get(i,0) + 1

    for x in range(steps):
        tmpDict = {}
        for key, value in dPairs.items():
            tmpDict[cipher[key][:2]] = tmpDict.get(cipher[key][:2], 0) + value
            tmpDict[cipher[key][1:3]] = tmpDict.get(cipher[key][1:3], 0) + value
            result[cipher[key][1]] = result.get(cipher[key][1], 0) + value

        dPairs = tmpDict

    maxElementCount = max(result.values())
    minElementCount = min(result.values())

    print('-----------------------------------------')
    print('Exercise2')
    print(f'Difference in max min values is: {maxElementCount - minElementCount}')


if __name__ == '__main__':
    template, cipher = ingestFile(fileName='inputFile.txt')

    exercise1(template, cipher, 10)

    exercise2(template, cipher, 40)
