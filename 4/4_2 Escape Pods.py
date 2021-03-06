# Escape Pods
# ===========

# You've blown up the LAMBCHOP doomsday device and broken the bunnies out of Lambda's prison - and now you need to escape from 
# the space station as quickly and as orderly as possible! The bunnies have all gathered in various locations throughout the station, 
# and need to make their way towards the seemingly endless amount of escape pods positioned in other parts of the station. You need 
# to get the numerous bunnies through the various rooms to the escape pods. Unfortunately, the corridors between the rooms can only 
# fit so many bunnies at a time. What's more, many of the corridors were resized to accommodate the LAMBCHOP, so they vary in how many 
# bunnies can move through them at a time. 

# Given the starting room numbers of the groups of bunnies, the room numbers of the escape pods, and how many bunnies can fit through 
# at a time in each direction of every corridor in between, figure out how many bunnies can safely make it to the escape pods at a time at peak.

# Write a function answer(entrances, exits, path) that takes an array of integers denoting where the groups of gathered bunnies are, 
# an array of integers denoting where the escape pods are located, and an array of an array of integers of the corridors, returning 
# the total number of bunnies that can get through at each time step as an int. The entrances and exits are disjoint and thus will never overlap. 
# The path element path[A][B] = C describes that the corridor going from A to B can fit C bunnies at each time step.  
# There are at most 50 rooms connected by the corridors and at most 2000000 bunnies that will fit at a time.

# For example, if you have:
# entrances = [0, 1]
# exits = [4, 5]
# path = [
#   [0, 0, 4, 6, 0, 0],  # Room 0: Bunnies
#   [0, 0, 5, 2, 0, 0],  # Room 1: Bunnies
#   [0, 0, 0, 0, 4, 4],  # Room 2: Intermediate room
#   [0, 0, 0, 0, 6, 6],  # Room 3: Intermediate room
#   [0, 0, 0, 0, 0, 0],  # Room 4: Escape pods
#   [0, 0, 0, 0, 0, 0],  # Room 5: Escape pods
# ]

# Then in each time step, the following might happen:
# 0 sends 4/4 bunnies to 2 and 6/6 bunnies to 3
# 1 sends 4/5 bunnies to 2 and 2/2 bunnies to 3
# 2 sends 4/4 bunnies to 4 and 4/4 bunnies to 5
# 3 sends 4/6 bunnies to 4 and 4/6 bunnies to 5

# So, in total, 16 bunnies could make it to the escape pods at 4 and 5 at each time step.  
# (Note that in this example, room 3 could have sent any variation of 8 bunnies to 4 and 5, such as 2/6 and 6/6, but the final answer remains the same.)

# Languages
# =========

# To provide a Python solution, edit solution.py
# To provide a Java solution, edit solution.java

# Test cases
# ==========

# Inputs:
#     (int list) entrances = [0]
#     (int list) exits = [3]
#     (int) path = [[0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]]
# Output:
#     (int) 6

# Inputs:
#     (int list) entrances = [0, 1]
#     (int list) exits = [4, 5]
#     (int) path = [[0, 0, 4, 6, 0, 0], [0, 0, 5, 2, 0, 0], [0, 0, 0, 0, 4, 4], [0, 0, 0, 0, 6, 6], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
# Output:
#     (int) 16

# Use verify [file] to test your solution and see how it does. When you are finished editing your code, use submit [file] to submit your answer. 
# If your solution passes the test cases, it will be removed from your home folder.

# ## ------------------------------------------------------------------------------------------------------

def answer1(entrances, exits, path):
    
    # First, it's important to realize that this is a multiple sources, multiple 
    # sinks problem where we have to find the max flow. This problem builds off
    # of the single source, single sink problem. To get the max flow for the 
    # latter problem, you create a residual graph and then find an augmenting
    # path through the residual graph using DFS, updating the residual graph
    # based on the augmenting path found. So long as there is an augmenting path 
    # through the residual graph, you can increase the flow. 
    #
    # We can extend this solution to multiple sources and multiple sinks. If
    # an augmenting path can be found starting at ***any*** source and ending
    # at ***any*** sink, you can increase the flow.
    
    # The residual graph starts out being the same as the graph given to us. 
    residual = path[:]
    
    # How many bunnies can make it to the escape pods at each time step?
    numBunnies = 0    
    
    # To determine whether the number of bunnies we found is the max flow, we
    # have to have a tracker that would determine whether we were able to find
    # an augmented path
    prevNumBunnies = -1
    
    # While we are still able to find an augmented path...
    while prevNumBunnies != numBunnies:
        
        # Set the tracker here. If an augmented path is found, numBunnies will 
        # change.
        prevNumBunnies = numBunnies
    
        # Check all paths starting at each available entrance
        for j in entrances:
    
            # Visited graph - which nodes have been visited?
            visited = []
            
            # The augmented path, implemented as a stack. The stack will add a 
            # node if the node is connected to at least one other unvisited 
            # node. The node on the top of the stack will be popped otherwise.
            path = []
            
            # Start the path at an entrance
            node = j                    
            while 1:
                
                # Keep track of whether or not we have found an unvisited node
                # connected to our current node of interest
                findUnvisited = False   
                
                # Also keep track of visited nodes
                visited.append(node)      
                
                # To speed up program, use a greedy algorithm. At each node,
                # only travel to a connected unvisited node that would allow
                # the maximum number of bunnies to travel through.
                maximum = 0
                index = 0
                
                # Check all adjacent nodes for the one that would allow the
                # maximum number of bunnies to travel through
                for i in range(len(residual[node])):
                    if residual[node][i] > maximum and i not in visited:
                        maximum = residual[node][i]
                        index = i
                        findUnvisited = True
                
                # Go to the node that would allow the most number of bunnies
                # in the corridor
                if findUnvisited:
                    path.append(node)
                    node = index
                
                # If there are no unvisited nodes connected to this entrance, 
                # check the paths connecting to another entrance.
                elif not path:
                    break   
                
                # If there are no unvisited nodes connected, backtrace in the 
                # augmented path.
                else:
                    node = path.pop()
                
                # If we find an end node, update the residual graph depending 
                # on the augmented path. To speed up the program, get the 
                # maximum number of bunnies that could go through the corridor
                # by finding the bottleneck corridor in the augmenting path
                # (the corridor that would allow the least number of bunnies to
                # go through. Use that to update numBunnies
                if node in exits:
                    path.append(node)
                    minimum = 2000000
                    for j in range(len(path) - 1):
                        if residual[path[j]][path[j + 1]] < minimum:
                            minimum = residual[path[j]][path[j + 1]]
                    numBunnies += minimum
                    for j in range(len(path) - 2):
                        residual[path[j]][path[j + 1]] -= minimum
                        residual[path[j + 1]][path[j]] += minimum
                    residual[path[len(path) - 2]][path[len(path) - 1]] -= minimum
                    break
 
    # Return number of bunnies
    return numBunnies

# ## ------------------------------------------------------------------------------------------------------


from collections import deque


INF = float("inf")


class Graph:
    def __init__(self, entrances, exits, path):
        self.graph = [list(row) for row in path]
        self.nodes_number = len(self.graph)
        self.max_flow = None

        self.entrance = self.nodes_number
        self.exit = self.nodes_number + 1

        for row in range(self.nodes_number):
            self.graph[row].append(0)
            self.graph[row].append(INF if row in exits else 0)

        self.nodes_number += 2

        self.graph.append([(INF if x in entrances else 0) for x in range(self.nodes_number)])
        self.graph.append([0] * self.nodes_number)

    def bfs(self):
        visited = set()
        deq = deque()
        deq.append((self.entrance, [self.entrance]))

        while len(deq) > 0:
            current, path = deq.popleft()
            if current == self.exit:
                return path

            for i in range(self.nodes_number):
                if i not in visited and self.graph[current][i] > 0:
                    visited.add(i)
                    new_path = list(path)
                    new_path.append(i)
                    deq.append((i, new_path))

        return None

    def get_max_flow(self):
        if self.max_flow is None:
            max_flow = 0

            while True:
                shortest_path = self.bfs()

                if shortest_path is None:
                    break

                flow = INF
                for i in range(1, len(shortest_path)):
                    node_from = shortest_path[i - 1]
                    node_to = shortest_path[i]
                    flow = min(flow, self.graph[node_from][node_to])

                for i in range(1, len(shortest_path)):
                    node_from = shortest_path[i - 1]
                    node_to = shortest_path[i]
                    self.graph[node_from][node_to] -= flow
                    self.graph[node_to][node_from] += flow

                max_flow += flow

            self.max_flow = max_flow

        return self.max_flow


def answer(entrances, exits, path):
    g = Graph(entrances, exits, path)
    return g.get_max_flow()