import os

class bingoCard:
    """Bingo Card Class that holds the data for a bingo card and the functions you can execute
    on the bingo card.
    """

    def __init__(self, numList, bingoCardNumber) -> None:
        self.bingoCard = []
        self.bingoCardNumber = bingoCardNumber
        self.initialList = numList
        self.winRank = 0
        self.winningNumber = 0
        self.populateBingoCard()

    def populateBingoCard(self):
        for r in self.initialList:
            row = []
            for c in r:
                row.append({'value': c, 'isMarked': False})
            self.bingoCard.append(row)

    def printBingoCard(self):
        print('-------------------------------------')
        print(f'Bingo Card {self.bingoCardNumber}')
        for r in self.bingoCard:
            printVal = ''
            for c in r:
                if c['isMarked']:
                    printVal += ('*' + c['value']).rjust(4)
                else:
                    printVal += c['value'].rjust(4)
            print(printVal)

    def markBingoCard(self, bingoNumber):
        for r in self.bingoCard:
            for c in r:
                if c['value'] == bingoNumber:
                    c['isMarked'] = True

        return self.checkBingoCard()
        
    def checkBingoCard(self):
        for r in self.bingoCard:
            if r[0]['isMarked'] and r[1]['isMarked'] and r[2]['isMarked'] and r[3]['isMarked'] \
               and r[4]['isMarked']:
               return True
        
        for x in range(5):
            if self.bingoCard[0][x]['isMarked'] and \
               self.bingoCard[1][x]['isMarked'] and \
               self.bingoCard[2][x]['isMarked'] and \
               self.bingoCard[3][x]['isMarked'] and \
               self.bingoCard[4][x]['isMarked']:
               return True

        return False

    def printCardScore(self):
        total = 0
        for r in self.bingoCard:
            for c in r:
                if not c['isMarked']:
                    total += int(c['value'])

        print(f'Card Score: {int(self.winningNumber) * total}')

        


def ingestFile(fileName):
    """Ingest the file

    Args:
        fileName (string): filename without path - path is assumed to be the same path as this script
    """
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),fileName)) as fileObject:
        lines = fileObject.readlines()

    resultList = [x.strip() for x in lines]
    
    # Get the bingo number call list
    bingoNumbers = resultList[0].split(',')

    cardList = []
    bingoCard = []

    cardList = [x.strip() for x in resultList[2:]]
    
    return bingoNumbers, cardList

def loadCardFile(cardFile):
    """Takes a 2D array of bingo cards separated by newline and returns a list of bingoCards

    Args:
        cardFile (list): 2D array of bingo cards separated by newlines

    Returns:
        list: Returns a list of bingoCard classes
    """
    cardList = []
    tmpList = []
    bingoCardNumber = 1
    for key, r in enumerate(cardFile):
        if not r:
            tmpCard = bingoCard(tmpList, bingoCardNumber)
            bingoCardNumber += 1
            cardList.append(tmpCard)
            # Here for troubleshooting only
            # tmpCard.printBingoCard()
            tmpList = []
            continue
        tmpRow = r.split()
        tmpList.append(tmpRow)
    tmpCard = bingoCard(tmpList, bingoCardNumber)
    # Here for troubleshooting only
    # tmpCard.printBingoCard()
    cardList.append(tmpCard)

    return cardList

def exercise1(cardList, bingoNumbers):
    """Solves exercise 1
    """
    
    print('###################################################')    
    print('Exercise 1')
    
    for num in bingoNumbers:
        for card in cardList:
            isWinner = card.markBingoCard(num)
            if isWinner:
                print('****WINNER******')
                print(f'Called Number: {num}')
                print(card.bingoCardNumber)
                card.printBingoCard()
                card.winningNumber = num
                card.printCardScore()
                return 0

def exercise2(cardList, bingoNumbers):
    """Solves exercise 1
    """
    winnerRanking = 1
    for num in bingoNumbers:
        for card in cardList:
            # If this card is already a winner, stop marking it
            if card.winRank != 0:
                continue

            isWinner = card.markBingoCard(num)

            if isWinner:
                card.winningNumber = num
                card.winRank = winnerRanking
                winnerRanking += 1

    # Walk through cards, evaluate winning cards and what order they won in
    #   Find the last card to win and calculate it's card score
    tmpTracker = 0
    for card in cardList:
        if card.winRank > 0:
            if card.winRank > tmpTracker:
                lastWinningCard = card
                tmpTracker = lastWinningCard.winRank
    
    print('###################################################')    
    print('Exercise 2')
    print('Last Winning Cards Score:')
    lastWinningCard.printBingoCard()
    lastWinningCard.printCardScore()

if __name__ == '__main__':
    bingoNumbers, cardFile = ingestFile(fileName='inputFile.txt')

    cardList = loadCardFile(cardFile)

    exercise1(cardList, bingoNumbers)

    exercise2(cardList, bingoNumbers)
