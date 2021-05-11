import numpy as np
import copy
#import datetime as dt

class Vertex:
    mat = []
    adj = []
    #GoalState = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    AStar_evaluation = None
    heuristic = None

    def __init__(self, mat, parent, direction, depth, cost):
        self.state = mat
        #self.mat = np.asmatrix(self.mat)
        #self.find_zero()
        self.pai = parent
        self.direction = direction
        self.depth = depth

        if parent:
            self.cost = parent.cost + cost
        else:
            self.cost = cost


    def isGoal(self, state):
        if self.state == state:
            return True
        return False


    def find_zero(self):
        self.x = -1
        self.y = -1
        for i in range(len(self.mat)):
            for j in range(len(self.mat)):
                if self.mat[i, j] == 0:
                    self.x = i
                    self.y = j
        if(self.x==-1 or self.y == -1):
            raise Exception("The matrix didnt include 0 please check the start state again, Thank you")


    def is_up(self):
        if self.x > 0:
            return True
        else:
            return False

    def is_down(self):
        if self.x < len(self.mat)-1:
            return True
        else:
            return False

    def is_right(self):
        if self.y < len(self.mat)-1:
            return True
        else:
            return False

    def is_left(self):
        if self.y > 0:
            return True
        else:
            return False

    """
    def __eq__(self, v2):
        for x in range(len(self.mat)):
            for y in range(len(self.mat)):
                if self.mat[x, y] != v2.mat[x, y]:
                    return False
        return True
    """

    def up(self, temp, x, n):
        temp[x], temp[x - n] = temp[x - n], temp[x]

    def down(self, temp, x, n):
        temp[x], temp[x + n] = temp[x + n], temp[x]

    def left(self, temp, x, n):
        temp[x], temp[x - 1] = temp[x - 1], temp[x]

    def right(self, temp, x, n):
        temp[x], temp[x - 1] = temp[x - 1], temp[x]


    def print(self):
        print(self.state)

    def discoverChildren(self, n):
        x = self.state.index(0)
        moves = self.available_moves(x, n)

        children = []

        for direction in moves:
            temp = self.state.copy()
            if direction == 'Left':
                temp[x], temp[x - 1] = temp[x - 1], temp[x]
            elif direction == 'Right':
                temp[x], temp[x + 1] = temp[x + 1], temp[x]
            elif direction == 'Up':
                temp[x], temp[x - n] = temp[x - n], temp[x]
            elif direction == 'Down':
                temp[x], temp[x + n] = temp[x + n], temp[x]

            children.append(
                Vertex(temp, self, direction, self.depth + 1,  self.cost + 1))  # depth should be changed as children are produced
        return children

        """
        if self.is_up():
            u = Vertex(copy.copy(self.mat), self,'U',self.depth + 1, 1)
            u = u.up()
            children.append(u)
        else:
            moves.remove('U')

        if self.is_down():
            u = Vertex(copy.copy(self.mat), self, 'D', self.depth + 1, 1)
            u = u.down()
            children.append(u)
        else:
            moves.remove('D')

        if self.is_right():
            u = Vertex(copy.copy(self.mat), self, 'R', self.depth + 1, 1)
            u = u.right()
            children.append(u)
        else:
            moves.remove('R')

        if self.is_left():
            u = Vertex(copy.copy(self.mat), self, 'L', self.depth + 1, 1)
            u = u.left()
            children.append(u)
        else:
            moves.remove('L')
        """

    def solution(self):
        solution = []
        solution.append(self.direction)
        path = self
        while path.pai:
            path = path.pai
            solution.append(path.direction)
        solution = solution[:-1]
        solution.reverse()
        return solution

    def available_moves(self, x, n):
        moves = ['Up', 'Down', 'Left', 'Right']
        if x % n == 0:
            moves.remove('Left')
        if x % n == n - 1:
            moves.remove('Right')
        if x - n < 0:
            moves.remove('Up')
        if x + n > n * n - 1:
            moves.remove('Down')

        return moves

    def f(self, n):
        return self.g() + self.h(n)

    def g(self):
        return self.cost

    def h(self, n):
        sum = 0;
        newmat = np.array(self.state.copy())
        GS = np.array(self.generateGoalState(n))
        newmat = np.hsplit(newmat, n)
        newmat = np.asmatrix(newmat)
        GS = np.hsplit(GS, n)
        GS = np.asmatrix(GS)
        for x in range(n):
            for y in range(n):
                if not newmat[x, y] == 0:
                    x_val, y_val = x, y;
                    x_goal, y_goal = self.findVal(GS, newmat[x, y])
                    sum += (abs(x_val - x_goal)+abs(y_val - y_goal))
        return sum

    def __lt__(self, other):
        if self.f(int(np.sqrt(len(self.state)))) == other.f(int(np.sqrt(len(other.state)))):
            if(self.direction!=None) and (other.direction!=None):
                if len(self.direction) == len(other.direction):
                    return self.direction < other.direction
                else:
                    return len(self.direction) < len(other.direction)
            else:
                return self.f(int(np.sqrt(len(self.state)))) < other.f(int(np.sqrt(len(other.state))))


    def generateGoalState(self, n):
        GoalState = []
        for x in range(np.power(n, 2)):
            GoalState.append(x + 1)
        GoalState[np.power(n, 2) - 1] = 0
        return GoalState

    def findVal(self, mat, val):
        for x in range(len(mat)):
            for y in range(len(mat)):
                if mat[x, y] == val:
                    return x, y;


    def generateGoalState(self, n):
        GoalState = []
        for x in range(np.power(n, 2)):
            GoalState.append(x + 1)
        GoalState[np.power(n, 2) - 1] = 0
        return GoalState









#def up(self):
    #     v = Vertex(copy.copy(self.mat))
    #     for i in range(len(self.mat)):
    #         for j in range(len(self.mat)):
    #             if v.mat[i, j] == 0:
    #                 self.x=i-1
    #                 self.y=j
    #                 v.mat[i, j], v.mat[i - 1, j] = v.mat[i - 1, j], v.mat[i, j]
    #                 return v
    #     return v
    #
    #
    # def down(self):
    #     v = Vertex(copy.copy(self.mat))
    #     for i in range(len(self.mat)):
    #         for j in range(len(self.mat)):
    #             if v.mat[i, j] == 0:
    #                 self.x=i+1
    #                 self.y=j
    #                 v.mat[i, j], v.mat[i + 1, j] = v.mat[i + 1, j], v.mat[i, j]
    #                 return v
    #     return v
    #
    # def right(self):
    #     v = Vertex(copy.copy(self.mat))
    #     for i in range(len(self.mat)):
    #         for j in range(len(self.mat)):
    #             if v.mat[i, j] == 0:
    #                 self.x=i
    #                 self.y=j+1
    #                 v.mat[i, j], v.mat[i, j+1] = v.mat[i, j+1], v.mat[i, j]
    #                 return v
    #     return v
    #
    # def left(self):
    #     v = Vertex(copy.copy(self.mat))
    #     for i in range(len(self.mat)):
    #         for j in range(len(self.mat)):
    #             if v.mat[i, j] == 0:
    #                 self.x=i
    #                 self.y=j-1
    #                 v.mat[i, j], v.mat[i, j-1] = v.mat[i, j-1], v.mat[i, j]
    #                 return v
    #     return v



