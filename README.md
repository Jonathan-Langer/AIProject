# AI Project - Solving The N-Puzzle Problem 

The goal of this project is to implement a search engine that supports several search algorithms to solve the ***N-Puzzle Problem***.
In our implementation, we used informed search algorithms such as: AStar and uninformed search algorithms such as: BFS and IDS. 

# The Problem
Given a n×n game board with n^2 tiles, where one slot is empty and each of the other slots contains a number
from 1 to n^2-1 (in any order). <br />
The goal is to move the tiles so that they will be displayed like in the goal position.<br />
The target state is set to be an ascending order of the numbers with the empty slot at the end. <br />
At each step, you can slide one of the four adjacent tiles (left, right, down and up) into the empty space. The options available to us are: up, down, right, left - there are cases where it isn't possible to move in all directions. In addition, the transition between states will be through moving the empty square, which will have the value of 0.
The cost of each movement is fixed - a cost of 1.

# Requirements
1. Implement the n-puzzle problem.
2. Your solver should accept n as input(the size of the game board), along with the initial state.
3. Your solver allows the user to select search strategy as input (Using a specific encoding that we will expand on later).
4. Solve the problem using the selected search algorithm by the user.

# Implementation 
***Input*** - The program will read its input from a single ***input.txt*** file. The first line in the file will determine which
algorithm to use: We will support 3 search algorithms: BFS, IDS, and A*. In order to know, which algorithm to choose, we will determine the type of algorithm
using the encoding:
* 1 - IDS
* 2 - BFS
* 3 - AStar <br />

In the second line will be written the size of the game board. <br />
In the third line will be written the initial state of the game board. <br />
***Output*** - The program will write into a file named ***output.txt*** and it will contain only one line in the following format:
A route that is described by the series of actions required to get from the initial state to the goal state. The actions are R
(Right), L (Left), D (Down), and U (Up) (capital letters).

***Note: In the Astar search algorithm we used the Manhattan Distance method.***

