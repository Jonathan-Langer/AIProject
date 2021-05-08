import copy

import numpy as np
from collections import defaultdict
from Vertex import Vertex


class Graph:
    E = []
    V = []
    GoalState = []

    def __init__(self, v, mat):
        self.initial_gs(mat)
        self.vGoalState = Vertex(copy.copy(self.GoalState))
        self.build_graph(v)

    """"
    def build_graph(self, v):
        queueOfVertex = []
        queueOfVertex.append(v)
        if self.is_goal_state(v) or self.is_exist(v):
            self.add_v(v)
            return
        else:
            self.add_v(v)
            v.find_zero()
            while len(queueOfVertex)!=0:
                state = queueOfVertex.pop(0)
                
                if state.is_up():
                    u = Vertex(copy.copy(state.mat))
                    u = u.up()
                    self.add_edge(state, u)
                    queueOfVertex.append(u)
                    u.print()
                    # self.build_graph(u)

                if state.is_down():
                    u = Vertex(copy.copy(state.mat))
                    u = u.down()
                    self.add_edge(state, u)
                    queueOfVertex.append(u)
                    u.print()
                    # self.build_graph(u)

                if state.is_right():
                    u = Vertex(copy.copy(state.mat))
                    u = u.right()
                    self.add_edge(state, u)
                    queueOfVertex.append(u)
                    u.print()
                    # self.build_graph(u)

                if state.is_left():
                    u = Vertex(copy.copy(state.mat))
                    u = u.left()
                    self.add_edge(state, u)
                    queueOfVertex.append(u)
                    u.print()
                    # self.build_graph(u)
    """
    """
    def build_graph(self, v):
        queueOfVertex = []
        queueOfVertex.append(v)
        if self.is_goal_state(v) or self.is_exist(v):
            self.add_v(v)
            return

        self.add_v(v)
        #v.find_zero()
        while len(queueOfVertex) != 0:
            state = queueOfVertex.pop(0)
            state.find_zero()
            if state.is_up():
                u = Vertex(copy.copy(state.mat))
                u = u.up()
                self.add_edge(state, u)
                if self.is_goal_state(u): #or self.is_exist(u):
                    u.print()
                    break
                if not self.is_exist(u):
                    queueOfVertex.append(u)
                #u.print()
                # self.build_graph(u)

            if state.is_down():
                u = Vertex(copy.copy(state.mat))
                u = u.down()
                self.add_edge(state, u)
                if self.is_goal_state(u):
                    u.print()
                    break
                if not self.is_exist(u):
                    queueOfVertex.append(u)
                #u.print()
                # self.build_graph(u)

            if state.is_right():
                u = Vertex(copy.copy(state.mat))
                u = u.right()
                self.add_edge(state, u)
                if self.is_goal_state(u):
                    u.print()
                    break
                if not self.is_exist(u):
                    queueOfVertex.append(u)
                #u.print()
                # self.build_graph(u)

            if state.is_left():
                u = Vertex(copy.copy(state.mat))
                u = u.left()
                self.add_edge(state, u)
                if self.is_goal_state(u):
                    break
                if not self.is_exist(u):
                    queueOfVertex.append(u)
                #u.print()
                # self.build_graph(u)
    """


    def add_edge(self, v, u):
        self.E.append([v, u])
        v.adj.append(u)
        u.pai = v

    def add_v(self, v):
        self.V.append(v)

    def is_exist(self, v):
        for v1 in range(len(self.V)):
            if self.V[v1] == v:
                return True
        return False

    def is_goal_state(self, v):
        if v == self.vGoalState:
            return True
        else:
            return False

    def initial_gs(self, mat):
        for x in range(np.power(len(mat), 2)):
            self.GoalState.append(x+1)
        self.GoalState[np.power(len(mat), 2)-1] = 0
        self.GoalState = np.array(self.GoalState)
        self.GoalState = np.hsplit(self.GoalState, len(mat))
        self.GoalState = np.asmatrix(self.GoalState)

    # def move_zero(self, size):
    #     self.GoalState[0, 0], self.GoalState[size-1, size-1] = self.GoalState[size-1, size-1], self.GoalState[0, 0]
    #     return self.GoalState





