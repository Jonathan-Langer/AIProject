import numpy as np
import copy


class Vertex:
    mat = []
    adj = []
    GoalState=[1, 2, 3, 4, 5, 6, 7, 8, 0]

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

    def isGoal(self):
        if self.state == self.GoalState:
            return True
        return False

    def up(self):
        v = Vertex(copy.copy(self.mat))
        for i in range(len(self.mat)):
            for j in range(len(self.mat)):
                if v.mat[i, j] == 0:
                    self.x=i-1
                    self.y=j
                    v.mat[i, j], v.mat[i - 1, j] = v.mat[i - 1, j], v.mat[i, j]
                    return v
        return v

    def down(self):
        v = Vertex(copy.copy(self.mat))
        for i in range(len(self.mat)):
            for j in range(len(self.mat)):
                if v.mat[i, j] == 0:
                    self.x=i+1
                    self.y=j
                    v.mat[i, j], v.mat[i + 1, j] = v.mat[i + 1, j], v.mat[i, j]
                    return v
        return v

    def right(self):
        v = Vertex(copy.copy(self.mat))
        for i in range(len(self.mat)):
            for j in range(len(self.mat)):
                if v.mat[i, j] == 0:
                    self.x=i
                    self.y=j+1
                    v.mat[i, j], v.mat[i, j+1] = v.mat[i, j+1], v.mat[i, j]
                    return v
        return v

    def left(self):
        v = Vertex(copy.copy(self.mat))
        for i in range(len(self.mat)):
            for j in range(len(self.mat)):
                if v.mat[i, j] == 0:
                    self.x=i
                    self.y=j-1
                    v.mat[i, j], v.mat[i, j-1] = v.mat[i, j-1], v.mat[i, j]
                    return v
        return v

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

    def print(self):
        print(self.state)

    def discoverChildren(self, n):
        x = self.state.index(0)
        moves = self.available_moves(x,n)

        children=[]

        for direction in moves:
            temp=self.state.copy()
            if direction == 'Left':
                temp[x], temp[x - 1] = temp[x - 1], temp[x]
            elif direction == 'Right':
                temp[x], temp[x + 1] = temp[x + 1], temp[x]
            elif direction == 'Up':
                temp[x], temp[x - n] = temp[x - n], temp[x]
            elif direction == 'Down':
                temp[x], temp[x + n] = temp[x + n], temp[x]

            children.append(
                Vertex(temp, self, direction, self.depth + 1, 1))  # depth should be changed as children are produced
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
        solution =[]
        solution.append(self.direction)
        path = self
        while path.pai != None:
            path = path.pai
            solution.append(path.direction)
        solution = solution[:-1]
        solution.reverse()
        return solution


    def available_moves(self, x, n):
        moves = ['Left', 'Right', 'Up', 'Down']
        if x % n == 0:
            moves.remove('Left')
        if x % n == n - 1:
            moves.remove('Right')
        if x - n < 0:
            moves.remove('Up')
        if x + n > n * n - 1:
            moves.remove('Down')

        return moves







