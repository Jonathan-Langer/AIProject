import numpy as np

from Graph import Graph
from Vertex import Vertex

import Node
import UninformedSearch

def main():
    # file = "1-2-3-4-5-6-0-7-8"
    # f = open("ass.txt", "w+")
    # f.write(file)
    # f.close()
    # gl = open("ass.txt", "r")
    # reader = gl.read()
    # curr = reader.split("-")
    # res = [int(x) for x in curr]
    # print(res)
    # res = np.array(res)
    # newarr = []
    # for x in range(len(res)):
    #     newarr.append(x)
    # print(res)
    # res2 = res
    # res = np.hsplit(res, 3)
    # print(res)
    # print(newarr)
    # print(np.asmatrix(res))
    # for x in range(len(newarr)-1):
    #     if newarr[x] < newarr[x+1]:
    #         newarr[x], newarr[x+1] = newarr[x+1], newarr[x]
    # print(newarr)
    # newarr = np.array(newarr)
    # newarr = np.hsplit(newarr, 3)
    # newarr = np.asmatrix(newarr)
    #matrix = [[1, 2, 3], [4, 5, 6], [0, 7, 8]]
    #v = Vertex(matrix)
    #g = Graph(v, matrix)
    #print(g.E)


    puzzle = [1,2,4,3,0,5,7,6,8]
    root = Node(puzzle)
    ui = UninformedSearch()

    solution = ui.BFS(root)

    if len(solution) > 0:
        for i in range(len(solution)):
            solution[i].printPuzzle()
    else:
        print("No path to solution is found")



if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
