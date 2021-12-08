import os

# Below is my array key
#   0000
#  1    2
#  1    2
#   3333
#  4    5
#  4    5
#   6666
#
# 0 = (0,1,2,4,5,6)
# 1 = (2,5)
# 2 = (0,2,3,4,6)
# 3 = (0,2,3,5,6)
# 4 = (1,2,3,5)
# 5 = (0,1,3,5,6)
# 6 = (0,1,3,4,5,6)
# 7 = (0,2,5)
# 8 = (0,1,2,3,4,5,6)
# 9 = (0,1,2,3,5,6)

class Display:
    """Display in the submarine consisting of signals and output
    """

    def __init__(self, input) -> None:
        self.signalList = []
        self.outputList = []
        # -1 is better so I know this value hasn't been set yet vs 0 which is a legit value
        self.countEasyNums = -1
        self.outputNumber = -1
        self.rawInput = input
        self.populateSignalAndOutput()
        self.cipher = {
            '0': [],
            '1': [],
            '2': [],
            '3': [],
            '4': [],
            '5': [],
            '6': [],
            '7': [],
            '8': [],
            '9': []
        }

    def populateSignalAndOutput(self):
        tmpList = self.rawInput.split(' | ')
        tmpSignalList = tmpList[0].strip().split()
        self.signalList = [sorted(list(t)) for t in tmpSignalList]
        tmpOutputList = tmpList[1].strip().split()
        self.outputList = [sorted(list(s)) for s in tmpOutputList]

    def calculateEasyNums(self):
        tmpCount = 0
        for x in self.outputList:
            if len(x) in (2,3,4,7):
                tmpCount += 1

        # Set it in case we want to use it again
        self.countEasyNums = tmpCount
        
        return self.countEasyNums

    def populateCipher(self):
        # IMPORTANT - lists are passed by reference, so these functions remove values from it
        #   making subsequent function calls work on a smaller list - just what's left.
        tmpSignalList = self.signalList[:]
        self.populate1478(tmpSignalList)
        self.populate069(tmpSignalList)
        self.populate235(tmpSignalList)

    def populate1478(self, tmpList):
        # Had to do "for" loops for each one because removing an element mid-loop was throwing it off
        for r in tmpList:
            if len(r) == 2:
                self.cipher['1'] = r
                tmpList.remove(r)
        for r in tmpList:
            if len(r) == 4:
                self.cipher['4'] = r
                tmpList.remove(r)
        for r in tmpList:
            if len(r) == 3:
                self.cipher['7'] = r
                tmpList.remove(r)
        for r in tmpList:
            if len(r) == 7:
                self.cipher['8'] = r
                tmpList.remove(r)

    def populate069(self, tmpList):
        # tmpList has 5 signal numbers and 6 signal numbers left, so let's make a smaller list to work with
        #   to help with elimination
        subList = []
        # Need these two ciphers to figure out 0 and 9, remaining is 6
        fourCipher = self.cipher['4']
        oneCipher = self.cipher['1']
        
        # create sublist of 6 signal numbers (0,6,9)
        for r in tmpList:
            if len(r) == 6:
                subList.append(r)

        # Get the 9 and then remove it from our subList (of 6 sig numbers) and overall tmpList
        #    The 9 has all the signals of a 4, but 0 and 6 do not.
        for rec in subList:
            if all(x in rec for x in fourCipher):
                self.cipher['9'] = rec
                tmpList.remove(rec)
                subList.remove(rec)
        
        # Get the 0 and 6 - only two numbers left in our subList
        #   and the 0 has both signals of the 1
        if all(x in subList[0] for x in oneCipher):
            # If the one signal is in here, this is the 9 and the other signal is the 6 else flip it
            self.cipher['0'] = subList[0]
            self.cipher['6'] = subList[1]
        else:
            self.cipher['6'] = subList[0]
            self.cipher['0'] = subList[1]

        tmpList.remove(subList[0])
        tmpList.remove(subList[1])

    def populate235(self, tmpList):
        # Need the 1 cipher to figure out which 5 signal digit is the 3 (has the one in it)
        # Need the 6 cipher to figure out which 5 signal digit is the 5 (a 6 digit has the 5 signals in it)
        oneCipher = self.cipher['1']
        sixCipher = self.cipher['6']
        
        # Get the 3 and then remove it from our overall tmpList
        for rec in tmpList:
            if all(x in rec for x in oneCipher):
                self.cipher['3'] = rec
                tmpList.remove(rec)

        # Get the 2 and 5 - only two numbers left
        #   and the 5's signals can be found in the six but a 2 can't.
        if all(x in sixCipher for x in tmpList[0]):
            self.cipher['5'] = tmpList[0]
            self.cipher['2'] = tmpList[1]
        else:
            self.cipher['2'] = tmpList[0]
            self.cipher['5'] = tmpList[1]

        tmpList.remove(tmpList[0])
        tmpList.remove(tmpList[0])

    def generateOutputNum(self):
        outputString = ''
        for num in self.outputList:
            for key, value in self.cipher.items():
                if num == value:
                    outputString += key
        self.outputNumber = int(outputString)

    def printCipher(self):
        # Used only for troubleshooting - print the cipher nice and neat
        for key, value in self.cipher.items():
            print(f'Key: {key} - Cipher: {value}')

def ingestFile(fileName):
    """Reads the single line and returns a list

    Args:
        fileName (string): filename without path - path is assumed to be the same path as this script
    """
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),fileName)) as fileObject:
        lines = fileObject.readlines()

    return lines

def exercise1(displayList):
    tmpCount = 0

    for x in displayList:
        tmpCount += x.calculateEasyNums()

    print('-------------------------------------')
    print('Exercise 1')
    print(f'Count of Easy Numbers in Output List: {tmpCount}')

def exercise2(displayList):
    tmpCount = 0

    for x in displayList:
        x.populateCipher()
        x.generateOutputNum()
        tmpCount += x.outputNumber

    print('-------------------------------------')
    print('Exercise 2')
    print(f'Total of Output Numbers from Displays: {tmpCount}')

def loadDisplays(input):
    tmpDisplayList = []
    for x in input:
        tmpDisplay = Display(x)
        tmpDisplayList.append(tmpDisplay)

    return tmpDisplayList

if __name__ == '__main__':
    input = ingestFile(fileName='inputFile.txt')

    displayList = loadDisplays(input)

    exercise1(displayList)

    exercise2(displayList)
