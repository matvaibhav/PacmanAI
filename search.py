# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]


def genericSearch(problem,fringe):
    """
        :param problem: current state and variables of pacman
        :param fringe: fringe list for traversing pacman states
        :return : path to goal from source

        This is generic search function which traverse graph in the order specific to
        the fringe list used. For example if Stack is used as fringe list it will search
        in DFS manner or if Queue is used it will search in BFS manner.
        In this function we pop element from fringe list, check if this node is goal,
        add to visited node to avoid re-visiting it and push into the fringe the unvisited
        successors of current node. We do this till we reach the goal state. Path to goal
        is returned.
    """

    visitedNodes = []   # List of visited nodes
    action = []         # List of actions taken to reach that particular state from start state
    while not fringe.isEmpty():
        v, action, cost = fringe.pop()
        if problem.isGoalState(v):
            return action
        if v not in visitedNodes:
            visitedNodes.append(v)
            successors = problem.getSuccessors(v)
            for item in successors:
                coordinates, nextAction, nextCost = item
                fringe.push((coordinates,action+[nextAction],cost+nextCost))
    return []

def genericSearchWithHeuristics(problem, fringe, heuristic=None):
    """
        :param problem: current state and variables of pacman
        :param fringe: fringe list for traversing pacman states
        :param heuristic: Heuristic used by pacman to learn some extra information about the goal state.
        :return : path to goal from source

        This is generic search function which traverses the graph in the order specific to
        the fringe list used. For example if Priority Queue with null heuristic is used
        it will search in UCS manner.
        This function also takes into account heuristic which helps pacman to take informed
        decision about which nodes to explore on the basis of heuristic function used.
        In this function we pop element from fringe list based on cost and heuristic function
        using priority queue, check if this node is goal, add to visited node to avoid re-visiting
        it and push into the fringe the unvisited successors of current node. We do this till
        we reach the goal state. Path to goal is returned.
    """

    visitedNodes = []   # List of visited nodes
    action = []         # List of actions taken to reach that particular state from start state
    while not fringe.isEmpty():
        v, action = fringe.pop()
        if problem.isGoalState(v):
            return action
        if v not in visitedNodes:
            visitedNodes.append(v)
            successors = problem.getSuccessors(v)
            for item in successors:
                coordinates, nextAction, nextCost = item
                newCost = problem.getCostOfActions(action+[nextAction]) + heuristic(coordinates, problem)
                fringe.push((coordinates,action+[nextAction]),newCost)
    return []

def depthFirstSearch(problem):
    """Search the deepest nodes in the search tree first."""
    stack = util.Stack()    # Stack used as fringe list
    stack.push((problem.getStartState(),[],0))
    return genericSearch(problem,stack)

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    queue = util.Queue()    # Queue used as fringe list
    queue.push((problem.getStartState(),[],0))
    return genericSearch(problem,queue)

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    pQueue = util.PriorityQueue()   # Priority queue used as fringe list
    cost = 0
    pQueue.push((problem.getStartState(), []), cost)
    return genericSearchWithHeuristics(problem, pQueue,nullHeuristic)

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    pQueue = util.PriorityQueue()   # Priority queue used as fringe list
    cost = 0
    pQueue.push((problem.getStartState(), []), cost)
    return genericSearchWithHeuristics(problem, pQueue, heuristic)

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch