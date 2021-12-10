import os
import math

SCORECIPHER = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

CLOSINGCHAR = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<'
}

EX2CIPHER = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4
}

def ingestFile(fileName):
    """Reads the single line and returns a list

    Args:
        fileName (string): filename without path - path is assumed to be the same path as this script
    """
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),fileName)) as fileObject:
        lines = fileObject.readlines()

    tmpList = [list(x.strip()) for x in lines]

    return tmpList

def evaluateLine(row):
    tmpList = []

    for key, y in enumerate(row):
        # First character is a not an opening chunk marker or we closed out a chunk and are starting over in a line
        if key == 0 or (key != 0 and not tmpList):
            if y not in CLOSINGCHAR.values():
                return SCORECIPHER[y], []
            else:
                tmpList.append(y)
        # If it's an opening marker, add to the list
        elif y in CLOSINGCHAR.values():
            tmpList.append(y)
        # If it's a closing marker, it better match the latest opening marker else we have a corrupt line
        elif y in CLOSINGCHAR.keys():
            # It's a corrupt line, assign the point value and break out
            if CLOSINGCHAR[y] != tmpList.pop():
                return SCORECIPHER[y], []
        else:
            raise Exception('Unexpected Failure')

    # You got all the way through the line without a failure, return 0 - this is a good line
    return 0, tmpList

def exercise1(input):
    openCharRowList = []
    tmpScore = 0
    previousScore = tmpScore

    for key, x in enumerate(input):
        tmp = []

        # Get the score, or if it's a good line, return the characters that would make it whole
        score, tmp = evaluateLine(x)

        if score == 0:
            openCharRowList.append(tmp)

        tmpScore += score

    print('-------------------------------------')
    print('Exercise 1')
    print(f'Syntax Score is: {tmpScore}')

    # return the unfinished array of open characters
    return openCharRowList

def exercise2(input):
    scoreList = []

    for x in input:
        score = 0
        for y in reversed(x):
            score = (score * 5) + EX2CIPHER[y]

        scoreList.append(score)

    sortedScores = sorted(scoreList)

    # lists are 0-based - so use the floor of the middle element, not the ceiling
    middle = math.floor(len(sortedScores)/2)

    print('-------------------------------------')
    print('Exercise 2')
    print(f'The AutoCorrect winning score is: {sortedScores[middle]}')

if __name__ == '__main__':
    input = ingestFile(fileName='inputFile.txt')

    goodList = exercise1(input)

    # You only need the remaining open characters to generate the score
    exercise2(goodList)