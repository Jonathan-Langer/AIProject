import numpy as np

class Vertex:
    mat = []
    adj = []

    def __init__(self, mat, parent, direction, depth, cost):
        self.state = mat
        self.pai = parent
        self.direction = direction
        self.depth = depth
        self.heuristic = 0
        if parent:
            self.cost = parent.cost + cost
        else:
            self.cost = cost


    def isGoal(self, state):
        if self.state == state:
            return True
        return False


    def print(self):
        print(self.state)

    def discoverChildren(self, n): #returns a list with all the possible children of the current node
        x = self.state.index(0)
        moves = self.available_moves(x, n)

        children = []

        for direction in moves:
            temp = self.state.copy()
            if direction == 'Right':
                temp[x], temp[x - 1] = temp[x - 1], temp[x]
            elif direction == 'Left':
                temp[x], temp[x + 1] = temp[x + 1], temp[x]
            elif direction == 'Down':
                temp[x], temp[x - n] = temp[x - n], temp[x]
            elif direction == 'Up':
                temp[x], temp[x + n] = temp[x + n], temp[x]

            children.append(
                Vertex(temp, self, direction, self.depth + 1,  self.cost + 1))  # depth and cost should be changed as children are produced
        return children


    def solution(self): #The function returns a list with the route from the initial state to the goal state
        solution = []
        if self.direction == 'Up':
            solution.append('U')
        elif self.direction == 'Down':
            solution.append('D')
        elif self.direction == 'Right':
            solution.append('R')
        elif self.direction == 'Left':
            solution.append('L')
        path = self
        while path.pai: #the loop will continues until we will reach to the initial state
            path = path.pai
            if path.direction == 'Up':
                solution.append('U')
            elif path.direction == 'Down':
                solution.append('D')
            elif path.direction == 'Right':
                solution.append('R')
            elif path.direction == 'Left':
                solution.append('L')
        solution.reverse()
        return solution

    def available_moves(self, x, n): #Function that returnes a list with all the available moves we can do from the current node
        moves = ['Up', 'Down', 'Left', 'Right'] #If several vertexes are formed at the same time (common parent) the vertexes will be arranged in the following order: up, down, left, right.
        if x % n == 0:
            moves.remove('Right')
        if x % n == n - 1:
            moves.remove('Left')
        if x - n < 0:
            moves.remove('Down')
        if x + n > n * n - 1:
            moves.remove('Up')

        return moves

    def f(self, n): #Function that returns the sum between the cost and the manhattan distance between the current node and the goal state
        return self.g() + self.h(n)

    def g(self):
        return self.cost

    def h(self, n): #The heuristic function according to Manhattan Distance
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


    def generateGoalState(self, n): #Generates Goal State
        GoalState = []
        for x in range(np.power(n, 2)):
            GoalState.append(x + 1)
        GoalState[np.power(n, 2) - 1] = 0
        return GoalState

    def findVal(self, mat, val): #Returns the coordinate of a specific value in the board game
        for x in range(len(mat)):
            for y in range(len(mat)):
                if mat[x, y] == val:
                    return x, y;





