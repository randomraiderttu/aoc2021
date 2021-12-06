import os

def ingestFile(fileName):
    """Takes a filename parameter, ingests a file and returns a 2-D list, each entry
    consisting of a list of the binary number that was provided

    Args:
        fileName (string): filename without path - path is assumed to be the same path as this script
    """
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),fileName)) as fileObject:
        lines = fileObject.readlines()

    resultList = [list(x.strip()) for x in lines]

    return resultList

def calculateGammaAndEpsilon(input):
    """Given a 2-D list of binary numbers, calculate and return the binary Gamma value

    Args:
        input (list): 2-D list of binary numbers, each digit in the binary list
    """
    nums = len(input[0])
    result = []
    gammaList = []
    epsilonList = []
    gamma = ""
    epsilon = ""

    # Create the array to hold the aggregate values by position
    for i in range(nums):
        result.append({'0': 0, '1': 0})

    for x in input:
        for key, value in enumerate(x):
            if value == '0':
                result[key]['0'] += 1
            elif value == '1':
                result[key]['1'] += 1

    for t in result:
        if t['0'] > t['1']:
            gammaList.append('0')
            epsilonList.append('1')
        else:
            gammaList.append('1')
            epsilonList.append('0')

    gamma = gamma.join(gammaList)
    epsilon = epsilon.join(epsilonList)

    return gamma, epsilon 

def calculateRating(inputList, position, algorithm):
    """Takes a 2D list and the position, calculates the count of 1's and 0's and then pairs down the list
    based on the algorithm passed in. Recursively figures out rating.

    Args:
        inputList (list): Input list - 2D list
        position (int): Bit number in a given binary value to evaluate
        algorithm (int): 1 or 0.  0 indicates we'll take the greatest aggregate between the 1s and 0s, a 
        1 in this value means we'll take the least.
    """
    zeroList = []
    oneList = []
    zeroCount = 0
    oneCount = 0

    # Used for troubleshooting only
    # print(f'CalculateRating - position: {position} - Algorithm: {algorithm} - Length of inputList: {len(inputList)}')

    if len(inputList) == 1:
        return ''.join(inputList[0])

    for x in inputList:
        if x[position] == '0':
            zeroCount += 1
            zeroList.append(x)
        else:
            oneCount += 1
            oneList.append(x)

    if algorithm == 0:
        if oneCount >= zeroCount:
            return calculateRating(oneList, position + 1, algorithm)
        else:
            return calculateRating(zeroList, position + 1, algorithm)
    else:
        if zeroCount <= oneCount:
            return calculateRating(zeroList, position + 1, algorithm)
        else:
            return calculateRating(oneList, position + 1, algorithm)
        

def exercise1(inputList):
    """Solves exercise 1

    Args:
        inputList (list): Takes in the list of strings from the input list
    """
    gamma, epsilon = calculateGammaAndEpsilon(inputList)

    gammaInt = int(gamma, 2)
    epsilonInt = int(epsilon, 2)

    print(f'Gamma binary: {gamma} | Gamma Integer: {gammaInt}')
    print(f'Epsilon binary: {epsilon} | Epsilon Integer: {epsilonInt}')

    print(f'Multiplied value is: {gammaInt * epsilonInt}')

def exercise2(inputList):
    """Solves exercise 2

    Args:
        inputList (list): Takes in the list of integers from the input list
    """

    oxygenRating = calculateRating(inputList=inputList,position=0,algorithm=0)
    co2Rating = calculateRating(inputList=inputList,position=0,algorithm=1)

    oxygenRatingInt = int(oxygenRating,2)
    co2RatingInt = int(co2Rating,2)

    print(f'Oxygen Rating binary: {oxygenRating} | Oxygen Rating Integer: {oxygenRatingInt}')
    print(f'CO2 Rating binary: {co2Rating} | CO2 Rating Integer: {co2RatingInt}')

    print(f'Multiplied value is: {oxygenRatingInt * co2RatingInt}')
    

if __name__ == '__main__':
    input = ingestFile(fileName='inputFile.txt')

    exercise1(input)

    exercise2(input)

