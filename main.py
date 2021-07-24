import numpy
import numpy as np

from Algorithms import BFS
from Algorithms import aStar
from Algorithms import IDS
from Algorithms import checkInput


def main():

    inputFile = open("input.txt", "r")
    typeOfAlgorithm = int(inputFile.readline())
    boardSize = int(inputFile.readline())
    initialState = inputFile.readline()
    initialState = initialState.split("-")
    for x in range(len(initialState)):
        initialState[x] = int(initialState[x])

    inputFile.close()

    if len(initialState) != np.power(boardSize,2):
        print("The size of the board that you entered in the second line doesn't match the size of the initial state you entered in the third line"
              + '\n' + "Please check again your input")
        quit()


    validInputFlag = False
    outputFile = open("output.txt", "w")
    if boardSize % 2 == 0:
        if checkInput(initialState, numpy.power(boardSize, 2)) % 2 == 1:
            validInputFlag = True
    elif boardSize % 2 == 1:
        if checkInput(initialState, numpy.power(boardSize, 2)) % 2 == 0:
            validInputFlag = True

    """if validInputFlag:
        print("No valid solution")
        return"""



    if typeOfAlgorithm == 1:
            Solution = IDS(initialState, boardSize)
            if len(Solution[0]) == 0:
                outputFile.write("The input you gave me is also the goal state" + '\n')
                outputFile.write("Number of explored nodes is: " + str(Solution[1]))
            else:
                outputFile.write("IDS Solution is: " + str(Solution[0]) + '\n')
                outputFile.write("Number of explored nodes is: " + str(Solution[1]))

    elif typeOfAlgorithm == 2:
        Solution = BFS(initialState, boardSize)
        if len(Solution[0]) == 0:
            outputFile.write("The input you gave me is also the goal state" + '\n')
            outputFile.write("Number of explored nodes is: " + str(Solution[1]))
        else:
            outputFile.write("BFS Solution is: " + str(Solution[0]) + '\n')
            outputFile.write("Number of explored nodes is: " + str(Solution[1]))
    else:
        Solution = aStar(initialState, boardSize)
        if len(Solution[0])==0:
            outputFile.write("The input you gave me is also the goal state" + '\n')
            outputFile.write("Number of explored nodes is: " + str(Solution[1]))
        else:
            outputFile.write("A* Solution is: " + str(Solution[0]) + '\n')
            outputFile.write("Number of explored nodes is: " + str(Solution[1]))

    print("Finished Calculating...please check the answer in the output.txt file")

if __name__ == '__main__':
    main()

