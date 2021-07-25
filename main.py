import numpy
import numpy as np

from Algorithms import BFS
from Algorithms import aStar
from Algorithms import IDS


def main():

    inputFile = open("input.txt", "r")
    typeOfAlgorithm = int(inputFile.readline())
    boardSize = int(inputFile.readline())
    initialState = inputFile.readline()
    initialState = initialState.split("-")
    for x in range(len(initialState)):
        initialState[x] = int(initialState[x])

    inputFile.close()

    if len(initialState) != np.power(boardSize,2):  #Checks if the size of the board game that is given in the second line actually match with the size of the initial state that is given in the third line
        print("The size of the board that you entered in the second line doesn't match the size of the initial state you entered in the third line"
              + '\n' + "Please check again your input")
        quit()


    outputFile = open("output.txt", "w")

    #solution[1] is the number of explored nodes, and we also returned it, in order to check ourselves and see that our implementations of all the search algorithms are correct.
    #For example the number of explored nodes in A* should be lower than the number of explored nodes in BFS.

    if typeOfAlgorithm == 1: #IDS
            Solution = IDS(initialState, boardSize)
            if len(Solution[0]) == 0:
                outputFile.write("The input you gave me is also the goal state" + '\n')
                #outputFile.write("Number of explored nodes is: " + str(Solution[1]))
            else:
                outputFile.write("IDS Solution is: " + str(Solution[0]) + '\n')
                #outputFile.write("Number of explored nodes is: " + str(Solution[1]))

    elif typeOfAlgorithm == 2: #BFS
        Solution = BFS(initialState, boardSize)
        if len(Solution[0]) == 0:
            outputFile.write("The input you gave me is also the goal state" + '\n')
            #outputFile.write("Number of explored nodes is: " + str(Solution[1]))
        else:
            outputFile.write("BFS Solution is: " + str(Solution[0]) + '\n')
            #outputFile.write("Number of explored nodes is: " + str(Solution[1]))

    elif typeOfAlgorithm == 3: #A*
        Solution = aStar(initialState, boardSize)
        if len(Solution[0])==0:
            outputFile.write("The input you gave me is also the goal state" + '\n')
            #outputFile.write("Number of explored nodes is: " + str(Solution[1]))
        else:
            outputFile.write("A* Solution is: " + str(Solution[0]) + '\n')
            #outputFile.write("Number of explored nodes is: " + str(Solution[1]))
    else:
        print("You didn't enter an appropreate number in the second line, Please check your input")
    print("Finished Calculating...Please check the answer in the output.txt file")

if __name__ == '__main__':
    main()

