import os

class ventField:
    """A class that represents the vent field and what you can do to manipulate it
    """

    def __init__(self, inputList) -> None:
        self.inputList = inputList
        self.ventListCoordinates = []
        self.populateVentCoordList()
        self.ventField = self.generateVentField()

    def generateVentField(self):
        """Generate the 0'd out vent field we'll use as we start processing coordinates

        Returns:
            List: 2D List of the x,y field
        """
        maxX = 0
        maxY = 0
        tmpVentField = []

        # We need the max x and y coordinates to know how big of an empty field to generate
        for x in self.ventListCoordinates:
            maxX = max(maxX, x['From']['x'], x['To']['x'])
            maxY = max(maxY, x['From']['y'], x['To']['y'])

        print(f'Max X: {maxX}   - Max Y: {maxY}')
        
        # Given the maxes for each axis, create the field and return it
        for y in range(maxY+1):
            tmpList = [0 for x in range(maxX+1)]
            tmpVentField.append(tmpList)

        return tmpVentField

    def parseCoordinates(self, line):
        """Takes in a line from the input and returns an object with x,y coordinates
        for the from and to locations

        Args:
            line (string): A single line from the input file that needs to be parsed

        Returns:
            dict: Returns a dictionary defining the "from" and "to" coordinates, each
                each containing an x,y coordinate. For ease of use later, I go ahead and 
                order the lower coordinates first.            
        """
        tmpList = line.split(' -> ')
        AList = tmpList[0].split(',')
        BList = tmpList[1].split(',')
        A = {'x': int(AList[0].strip()), 'y': int(AList[1].strip())}
        B = {'x': int(BList[0].strip()), 'y': int(BList[1].strip())}

        isStraightLine = self.isStraightLine(A, B)
        
        # for later looping, order with y coordinates as smaller first
        if A['y'] == B['y']:
            if A['x'] > B['x']:
                return {'From': B, 'To': A, 'isStraightLine': isStraightLine}
            else:
                return {'From': A, 'To': B, 'isStraightLine': isStraightLine}
        elif A['y'] > B['y']:
            return {'From': B, 'To': A, 'isStraightLine': isStraightLine}
        else:
            return {'From': A, 'To': B, 'isStraightLine': isStraightLine}

    def populateVentCoordList(self):
        """Populate the ventListCoordinate list from the input lines
        """
        for x in self.inputList:
            self.ventListCoordinates.append(self.parseCoordinates(x))

    def isStraightLine(self, A, B):
        """Returns a bool to tell you if the line is straight; vertical or horizontal

        Args:
            A (dict): Dict with x and y coordinates
            B (dict): Dict with x and y coordinates

        Returns:
            [type]: [description]
        """
        if A['x'] == B['x'] or A['y'] == B['y']:
            return True
        else:
            return False

    def logStraightVents(self, A, B):
        """Creates markers in the vent field for the straight lines

        Args:
            A (dict): Object with x,y coordinates
            B (dict): Object with x,y coordinates
        """
        for y in range(A['y'], B['y']+1):
            for x in range(A['x'], B['x']+1):
                self.ventField[y][x] += 1

    def logDiagonalVents(self, A, B):
        """Creates markers in the vent field for the diagonal lines

        Args:
            A (dict): Object with x,y coordinates
            B (dict): Object with x,y coordiantes
        """
        # Diagonal lines can be at a 45 or -45 degree angle, so you have to account
        #    for how you increment or decrement the x axis
        if A['x'] < B['x']:
            isNegativeSlope = False
        else:
            isNegativeSlope = True
        
        currentX = A['x']
        for y in range(A['y'], B['y']+1):
            self.ventField[y][currentX] += 1
            if isNegativeSlope:
                currentX -= 1
            else:
                currentX += 1

    def fillVentField(self, straightLineFlag, diagonalLineFlag):
        """Create markers in the vent field, taking parameters that dictate if we should load
              straight, diagonal or both kinds of lines - decided to do the distinction here
              so that exercise1 and exercise2 can determine which lines they add to the event
              field independently

        Args:
            straightLineFlag (bool): Boolean to tell you if you should load straight lines
            diagonalLineFlag (bool): Boolean to tell you if you shoud load diagonal lines
        """
        for r in self.ventListCoordinates:
            if r['isStraightLine'] and straightLineFlag:
                self.logStraightVents(r['From'], r['To'])
            elif not r['isStraightLine'] and diagonalLineFlag:
                self.logDiagonalVents(r['From'], r['To'])

def ingestFile(fileName):
    """Takes a filename parameter, ingests a file and returns a list of integers from the file.

    Args:
        fileName (string): filename without path - path is assumed to be the same path as this script
    """
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),fileName)) as fileObject:
        lines = fileObject.readlines()

    return lines


def exercise1(vf):
    """Solves exercise 1

    Args:
        vf (ventField class): Current VentField we're working with
    """
    # Fill the event field with straight lines only
    vf.fillVentField(True, False)
    
    # Count it up - get an answer
    counter = 0
    for y in vf.ventField:
        for x in y:
            if x >= 2:
                counter += 1

    print('Exercise 1')
    print(f'Total number of overlapping lines: {counter}')
    print()

def exercise2(vf):
    """Solves exercise 2

    Args:
        vf (ventField class): Current VentField we're working with
    """
    # Fill the event field with diagonal lines only
    vf.fillVentField(False, True)
    
    # Count it up - get an answer
    counter = 0
    for y in vf.ventField:
        for x in y:
            if x >= 2:
                counter += 1

    print('Exercise 2')
    print(f'Total number of overlapping lines: {counter}')
    print()


if __name__ == '__main__':
    input = ingestFile(fileName='inputFile.txt')

    vf = ventField(input)

    exercise1(vf)

    exercise2(vf)

