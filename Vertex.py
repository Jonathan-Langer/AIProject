import numpy as np
import copy


class Vertex:
    mat = []
    adj = []

    # Ctor
    def __init__(self, mat):
        self.mat = copy.copy(mat)  # Shallow copy
        self.mat = np.asmatrix(self.mat)
        self.find_zero()
        self.pai = None
        self.x = None
        self.y = None

    # Move matrix up, down, left, right
    def up(self):
        v = Vertex(copy.copy(self.mat))
        for i in range(len(self.mat)):
            for j in range(len(self.mat)):
                if v.mat[i, j] == 0:
                    v.mat[i, j], v.mat[i + 1, j] = v.mat[i + 1, j], v.mat[i, j]
                    return v
        return v

    def down(self):
        v = Vertex(copy.copy(self.mat))
        for i in range(len(self.mat)):
            for j in range(len(self.mat)):
                if v.mat[i, j] == 0:
                    v.mat[i, j], v.mat[i - 1, j] = v.mat[i - 1, j], v.mat[i, j]
                    return v
        return v

    def right(self):
        v = Vertex(copy.copy(self.mat))
        for i in range(len(self.mat)):
            for j in range(len(self.mat)):
                if v.mat[i, j] == 0:
                    v.mat[i, j], v.mat[i, j-1] = v.mat[i, j-1], v.mat[i, j]
                    return v
        return v

    def left(self):
        v = Vertex(copy.copy(self.mat))
        for i in range(len(self.mat)):
            for j in range(len(self.mat)):
                if v.mat[i, j] == 0:
                    v.mat[i, j], v.mat[i, j+1] = v.mat[i, j+1], v.mat[i, j]
                    return v
        return v

    def find_zero(self):  # Finds the current index of zero
        for i in range(len(self.mat)):
            for j in range(len(self.mat)):
                if self.mat[i, j] == 0:
                    self.x = i
                    self.y = j

    # Checks if there is a way up, down, left, right
    def is_up(self):
        if self.x < len(self.mat)-1:
            return True
        else:
            return False

    def is_down(self):
        if self.x > 0:
            return True
        else:
            return False

    def is_right(self):
        if self.y > 0:
            return True
        else:
            return False

    def is_left(self):
        if self.y < len(self.mat)-1:
            return True
        else:
            return False

    def __eq__(self, v2):  # Operator '=='
        for x in range(len(self.mat)):
            for y in range(len(self.mat)):
                if self.mat[x, y] != v2.mat[x, y]:
                    return False
        return True









