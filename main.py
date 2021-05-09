import numpy as np

from Graph import Graph
from Vertex import Vertex
from Algorithms import BFS
from Algorithms import aStar


def solvable(board):
    counter = 0
    for i in range(len(board)-1):
        for j in range(i+1 , len(board)):
            if (( board[i] > board[j]) and board[i] and board[j]):
                counter += 1

    if (counter %2 ==0):
        return True
    return False

def main():
    #file = "1-2-3-4-5-6-0-7-8"
    #f = open("ass.txt", "w+")
    #f.write(file)
    #f.close()
    #gl = open("ass.txt", "r")
    #reader = gl.read()
    #curr = reader.split("-")
    #res = [int(x) for x in curr]
    # print(res)
    #res = np.array(res)
    #newarr = []
    #for x in range(len(res)):
        #newarr.append(x)
    # print(res)
    #res2 = res
    #res = np.hsplit(res, 3)
    # print(res)
    # print(newarr)
    # print(np.asmatrix(res))
    #for x in range(len(newarr) - 1):
        #if newarr[x] < newarr[x + 1]:
            #newarr[x], newarr[x + 1] = newarr[x + 1], newarr[x]
    # print(newarr)
    #newarr = np.array(newarr)
    #newarr = np.hsplit(newarr, 3)
    #newarr = np.asmatrix(newarr)
    # matrix = [[1, 2, 3], [4, 5, 6], [0, 7, 8]]
    # v = Vertex(matrix)
    # g = Graph(v, matrix)

    list = [1, 8, 2, 0, 4, 3, 7, 6, 5]
    list2 = [1, 2, 3, 4, 5, 6, 0, 7, 8]

    f = open("input.txt", "r")
    typeOfAlgorithm = int(f.readline())
    boardSize = int(f.readline())
    initialState = f.readline()
    initialState = initialState.split("-")
    for x in range(len(initialState)):
        initialState[x] = int(initialState[x])

    if solvable(initialState) == False:
        print("The puzzle isn't solvable")
    else:
        BFS_Solution = BFS(initialState, boardSize)
        #BFS_Solution = BFS(list, 3)
        print("BFS Solution is: ", BFS_Solution[0])
        print("Number of explored nodes is: ", BFS_Solution[1])
        # print(g.E)

        aStar_solution = aStar(initialState, boardSize)
        print("AStar solution is", aStar_solution[0])
        print("Number of explored nodes is: ", aStar_solution[1])


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
