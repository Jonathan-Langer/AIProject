import numpy
import numpy as np

from Graph import Graph
from Vertex import Vertex
from Algorithms import BFS
from Algorithms import aStar
from Algorithms import IDS
from Algorithms import checkInput


def main():

    list = [1, 8, 2, 0, 4, 3, 7, 6, 5]
    list2 = [1, 2, 3, 4, 5, 6, 0, 7, 8]

    inputFile = open("input.txt", "r")
    typeOfAlgorithm = int(inputFile.readline())
    boardSize = int(inputFile.readline())
    initialState = inputFile.readline()
    initialState = initialState.split("-")
    for x in range(len(initialState)):
        initialState[x] = int(initialState[x])

    inputFile.close()

    outputFile = open("output.txt","w")

    if checkInput(initialState, numpy.power(boardSize, 2)) % 2 == 1:
        print("No valid solution")
        return

    if len(initialState) != np.power(boardSize,2):
        print("The size of the board that you entered in the second line doesn't match the size of the initial state you entered in the third line"
              + '\n' + "Please check again your input")
        quit()


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

