import os

def ingestFile(fileName):
    """Takes a filename parameter, ingests a file and returns a 2-dimensional array, each entry
    consisting of a direction in element 1 and an integer value in element 2

    TODO: It would be better if I converted the value to a true integer before I pass it along, but
    I'm playing catchup and don't want to mess with it - plus my WSL2 instance is giving me fits and
    I only have so much time.

    Args:
        fileName (string): filename without path - path is assumed to be the same path as this script
    """
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),fileName)) as fileObject:
        lines = fileObject.readlines()

    resultList = [x.strip().split(' ') for x in lines]

    return resultList

def moveSub(instructions, currentCoordinates):
    """Moves submarine according to given instructions

    Args:
        instructions (list): Two-element list with the first element indicating the direction
                    of the movement and the second element defining how far to move
        currentCoordinates (dict): Dictionary with current X and Y coordinates
    """
    if instructions[0] == 'down':
        return {'x': currentCoordinates['x'], 'y': currentCoordinates['y'] + int(instructions[1])}
    elif instructions[0] == 'up':
        return {'x': currentCoordinates['x'], 'y': currentCoordinates['y'] - int(instructions[1])}
    elif instructions[0] == 'forward':
        return {'x': currentCoordinates['x'] + int(instructions[1]), 'y': currentCoordinates['y']}
    else:
        return currentCoordinates

def moveSubWithAim(instructions, currentCoordinates):
    """Moves submarine according to given instructions using down/up to affect your vector

    Args:
        instructions (list): Two-element list with the first element indicating the direction
                    of the movement and the second element defining how far to move
        currentCoordinates (dict): Dictionary with current X and Y coordinates and current aim
    """
    if instructions[0] == 'down':
        return {'x': currentCoordinates['x'], 
                'y': currentCoordinates['y'], 
                'aim': currentCoordinates['aim'] + int(instructions[1])
                }
    elif instructions[0] == 'up':
        return {'x': currentCoordinates['x'], 
                'y': currentCoordinates['y'], 
                'aim': currentCoordinates['aim'] - int(instructions[1])
                }
    elif instructions[0] == 'forward':
        return {'x': currentCoordinates['x'] + int(instructions[1]), 
                'y': currentCoordinates['y'] + (currentCoordinates['aim'] * int(instructions[1])),
                'aim': currentCoordinates['aim']
                }
    else:
        return currentCoordinates


def exercise1(inputList):
    """Solves exercise 1

    Args:
        inputList (list): Takes in the list of integers from the input list
    """
    coordinates = {'x': 0, 'y': 0}

    for x in inputList:
        coordinates = moveSub(x, coordinates)

    print('Exercise1 Results')
    print('---------------------------------------------')
    print(f'Final coordinates are: {coordinates}')
    print(f"Multiplying yields: {coordinates['x'] * coordinates['y']}")
    print('---------------------------------------------')

def exercise2(inputList):
    """Solves exercise 2

    Args:
        inputList (list): Takes in the list of integers from the input list
    """
    coordinates = {'x': 0, 'y': 0, 'aim': 0}

    for x in inputList:
        coordinates = moveSubWithAim(x, coordinates)

    print('')
    print('Exercise2 Results')
    print('---------------------------------------------')
    print(f'Final coordinates are: {coordinates}')
    print(f"Multiplying yields: {coordinates['x'] * coordinates['y']}")
    print('---------------------------------------------')


if __name__ == '__main__':
    input = ingestFile(fileName='inputFile.txt')

    exercise1(input)

    exercise2(input)

