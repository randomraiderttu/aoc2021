import os

def ingestFile(fileName):
    """Takes a filename parameter, ingests a file and returns a list of integers from the file.

    Args:
        fileName (string): filename without path - path is assumed to be the same path as this script
    """
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),fileName)) as fileObject:
        lines = fileObject.readlines()

    stripLines = [int(x.strip()) for x in lines]

    return stripLines

def calDepthChanges(inList):
    """Given a list, walk through and determine if the current depth is greater than the previous depth.
       
       If it is greater, count that as an increase, returning the total increases.

    Args:
        inList (list): Input List
    """
    counter = 0
    prevDepth = 0

    # Loop over the input list and count depth increases over previous value
    # Commented out code was used for troubleshooting
    for x in inList:
        if x > prevDepth and prevDepth != 0:
            counter += 1
        #     print(f'{x} (Increased from {prevDepth})')
        # elif prevDepth == 0:
        #     print(f'{x}')
        # else:
        #     print(f'{x} (Decreased from {prevDepth})')

        prevDepth = x

    return counter

def exercise1(inputList):
    """Solves exercise 1

    Args:
        inputList (list): Takes in the list of integers from the input list
    """

    totIncreases = calDepthChanges(inputList)
    print(f'Exercise1 depth increases: {totIncreases}')

def exercise2(inputList):
    """Solves exercise 2

    Args:
        inputList (list): Takes in the list of integers from the input list
    """

    # Enumerate over the list summing the current and previous two values and create a new list
    results = [inputList[count] + inputList[count-1] + inputList[count-2] for count, value in enumerate(inputList)]
    
    # The first two elements in the array do not have the prior two elements to make a viable 3-value rolling sum, 
    # so we don't include them
    totIncreases = calDepthChanges(results[2:])
    print(f'Exercise2 depth increases: {totIncreases}')
 
if __name__ == '__main__':
    input = ingestFile(fileName='inputFile.txt')

    exercise1(input)

    exercise2(input)

