"""
Problem 1: Graphing Flights
Create a variable flights that represents the undirected graph below as an adjacency dictionary, where each node's value is represented by a string with the airport's name (ex. "JFK").
"""

flights = {
    "LAX" : ["JFK"],
    "JFK" : ["LAX", "DFW"],
    "DFW" : ["JFK", "ATL"],
    "ATL" : ["DFW"]
}

# print(list(flights.keys()))
# print(list(flights.values()))
# print(flights["JFK"])

"""
Problem 2: There and back
Input: list (adjecency list representing a graph where nodes[i] = [nodes that node i is connected to])
Output: boolean (true if all fights have a returning flight)
Constraints:
    - all flights must have a connected fligt back to it's current node
Edge Cases:
    - empty flights -> True
    
Plan: Iterate through each flight and check if the current flight number is in the flight list of any other flights or not. If not, return False. 
"""

def bidirectional_flights(flights):
    for i in range(len(flights)):
        connectedFlights = flights[i]
        
        for currentFlightNum in connectedFlights:
            if i not in flights[currentFlightNum]:
                return False
            
    return True

flights1 = [[1, 2], [0], [0, 3], [2]]
flights2 = [[1, 2], [], [0], [2]]

# print(bidirectional_flights(flights1))
# print(bidirectional_flights(flights2))

"""
Problem 3: Finding Direct Flights
Input: 2D array (of size n x n ), integer (source)
Output: list (of all destinations the customer can reach from the source)
Constraints:
    - n[i][j] = 1 indicates that there is a flight from i to j
    - n[i][j] = 0 indicates that there is not a flight from i to j

Plan: Since this an adjacency list, look for the list of flights for flight number (source). For each flight in the list, if it is 1, we know it is a connected flight, so append it to a result list and return the list
"""

def get_direct_flights(flights, source):
    sourceFlightConnections = flights[source]
    results = []
    
    for flightNumber in range(len(sourceFlightConnections)):
        if sourceFlightConnections[flightNumber] == 1:
            results.append(flightNumber)
            
    return results

flights = [
            [0, 1, 1, 0],
            [1, 0, 0, 0],
            [1, 1, 0, 1],
            [0, 0, 0, 0]]

# print(get_direct_flights(flights, 2))
# print(get_direct_flights(flights, 3))

"""
Problem 4: Converting Flgiht Representations
Input: list of edges 
Output: dict (representing the list of edges graph as a adjacency dict)
Constraints:
    - flight[i] = [a,b] where there is bidirectional flight between a and b

Plan: Iterate through the list of edges and add b to a's values and a to b's values in the dict. Define the dict with a default value of empty lists
"""

from collections import defaultdict

def get_adj_dict(flights):
    flightsDict = {}
    
    for flight1, flight2 in flights:
        if flight1 not in flightsDict:
            flightsDict[flight1] = []
        if flight2 not in flightsDict:
            flightsDict[flight2] = []
        
        flightsDict[flight1].append(flight2)
        flightsDict[flight2].append(flight1)
        
    return flightsDict

flights = [['Cape Town', 'Addis Ababa'], ['Cairo', 'Lagos'], ['Lagos', 'Addis Ababa'], 
            ['Nairobi', 'Cairo'], ['Cairo', 'Cape Town']]
# print(get_adj_dict(flights))

"""
Problem 5: Find Center of Airport
Input: list of edges ([i,j] where i to j is bidirectional)
Output: Integer (node that is the center of the graph, aka is connected to n-1 nodes)
Edge Cases:
    - there is only one node -> return node
    - there are two nodes and both are connected -> return node that is highest
    
Plan: Iterate through the list of edges and convert the list ot a adjacaency dict. If the list length of the 
values of the dict is n-1, we know it can be a center. Return the highest number center. 
"""

def find_center(terminals):
    flightCountDict = {}
    
    for flight1, flight2 in terminals:
        flightCountDict[flight1] = flightCountDict.get(flight1, 0) + 1
        flightCountDict[flight2] = flightCountDict.get(flight2, 0) + 1
    
    centerFlightNumber = -1
    
    for flightNumber, flightsCount in flightCountDict.items():
        if flightsCount == len(flightCountDict) - 1:
            centerFlightNumber = max(centerFlightNumber, flightNumber)
            
    return centerFlightNumber

terminals1 = [[1,2],[2,3],[4,2]]
terminals2 = [[1,2],[5,1],[1,3],[1,4]]

# print(find_center(terminals1))
# print(find_center(terminals2))

"""
Problem 6: Finding All Reachable Destinations
Input: dict (representing flights where key: current destination, value: list of reachable destinations from current destination), start (destination name)
Output: list (a;; destomatopms reachable from the start)

Plan: Use a BFS to iterate through all possible paths from the starting node and add the current node's value to the resulting list since it a reachable. 
Once the BFS is over, every node that is accessible from the starting node will be in the resulting list, then return that list. 

Psuedo Code:

Create a queue with the starting destination in it. (queue to represent the nodes we want to traverse into next)
Crate a set to keep track of visited nodes

Create a list to represent the reachable destination (nodes)

while queue is not empty:
    currentDestination = queue.popleft()
    add the current node to the visited list
    
    look up the current node in the dict to find it's list of destinations. 
    loop through the currentDestination's list of desintations and add it to the queue if it has not been visited. 
    
return reachable destinations
"""

from collections import deque

def get_all_destinations(flights, start):
    queue = deque()
    queue.append(start)
    visited = set()
    
    reachable = []
    
    while queue:
        currentDestination = queue.popleft()
        
        visited.add(currentDestination)
        reachable.append(currentDestination)
        
        for destination in flights.get(currentDestination, []):
            if destination not in visited:
                queue.append(destination)
            
    return reachable

# flights = {
#     "Tokyo": ["Sydney"],
#     "Sydney": ["Tokyo", "Beijing"],
#     "Beijing": ["Mexico City", "Helsinki"],
#     "Helsinki": ["Cairo", "New York"],
#     "Cairo": ["Helsinki", "Reykjavik"],
#     "Reykjavik": ["Cairo", "New York"],
#     "Mexico City": ["Sydney"],
#     "New York": []   
# }

# print(get_all_destinations(flights, "Beijing"))
# print(get_all_destinations(flights, "Helsinki"))

"""
Problem 7: Find All Reachable Destinations using DFS
Same question as above but using DFS
"""

def get_all_destinations_dfs(flights, start):
    visited = []
    
    def dfs_helper(start_node, visited):
        if start_node in visited:
            return

        visited.append(start_node)
        
        neigborList = flights.get(start_node, [])
        
        for neigbor in neigborList:
            dfs_helper(neigbor, visited)
    
    dfs_helper(start, visited)
    return visited

flights = {
    "Tokyo": ["Sydney"],
    "Sydney": ["Tokyo", "Beijing"],
    "Beijing": ["Mexico City", "Helsinki"],
    "Helsinki": ["Cairo", "New York"],
    "Cairo": ["Helsinki", "Reykjavik"],
    "Reykjavik": ["Cairo", "New York"],
    "Mexico City": ["Sydney"]   
}

# print(get_all_destinations(flights, "Beijing"))
# print(get_all_destinations(flights, "Helsinki"))

"""
Input: list of edges (boarding_passes[i] = (departure, arrival))
Output: list (airports we will pass through in the order visited.)

Plan: Create a dict mapping the departure airport to it's arrival airport. The starting airport is the airport that is not the in dict values and the ending airport is the airport 
that is not in the dict keys.

Time: O(E) - for mapping the list of edges to a dict 
Space: O(E) - for using a hashmap and a list to store the values
"""

def find_itinerary(boarding_passes):
    # map all departures and arrivals using a dict
    flightsDict = {}
    
    for departure, arrival in boarding_passes:
        flightsDict[departure] = arrival
    
    # find the starting point
    start = None
    
    for departure, arrival in flightsDict.items():
        if departure not in flightsDict.values():
            start = departure
    
    # perofrm dfs to find the order
    flightOrder = []
    
    def dfs_helper(currFlight, flightOrder):
        if not currFlight:
            return 
        
        flightOrder.append(currFlight)
        
        next_flight = flightsDict.get(currFlight, None)
        dfs_helper(next_flight, flightOrder)
        
    dfs_helper(start, flightOrder)
    
    return flightOrder

# boarding_passes_1 = [
#                     ("JFK", "ATL"),
#                     ("SFO", "JFK"),
#                     ("ATL", "ORD"),
#                     ("LAX", "SFO")]

# boarding_passes_2 = [
#                     ("LAX", "DXB"),
#                     ("DFW", "JFK"),
#                     ("LHR", "DFW"),
#                     ("JFK", "LAX")]

# print(find_itinerary(boarding_passes_1))
# print(find_itinerary(boarding_passes_2))

"""
Session 2 
"""

"""
Problem 1: Can Rebook Flight
Oh no! Your flight has been cancelled and you need to rebook. Given an adjacency matrix of today's flights flights where each flight is labeled 0 to n-1 and flights[i][j] = 1 indicates that there is an available flight from location i to location j, return True if there exists a path from your current location source to your final destination dest. Otherwise return False.

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity.

Understand: 
Input: list (adjacency matrix of today's flights), integer (source), integer (destination)
Output: boolean (true, if there exists a path from source to destination)
Constraints:
    - each flight is labled 0 to n-1
    - flights[i][j] = 1 means there is a flight from i to j
Edge Cases:
    - no flights -> return False

Plan: Use a DFS to go through the graph. If the current node is the destination then we know we can reach the destination, return True. 

Pseudo Code:
visited = set()
isPath = False

def dfs_helper(nodeIndex, visited):
    if nodeIndex is in visited, return
    if nodeIndex is equal to the destination, set the boolean as True
    
    get the nodeIndex's adjacency list
    for each flight in the list:
        if the flight is connected, call the dfs helper on the flight

call the dfs_helper function

return isPath boolean
"""

def can_rebook(flights, source, dest):
    visited = set()
    existsPath = False
    
    def dfs_helper(nodeIndex, visited):
        if nodeIndex == dest:
            nonlocal existsPath
            existsPath = True
            return
        
        connectedFlightsStatus = flights[nodeIndex]
        
        for flightNum in range(len(connectedFlightsStatus)):
            if connectedFlightsStatus[flightNum] == 1 and flightNum not in visited:
                dfs_helper(flightNum, visited)
                
    dfs_helper(source, visited)
    return existsPath

"""
Other dfs appraoch 
1) Create a visited list to track locations we have already checked.
2) Define a recursive DFS function:
    a) If the current location is `dest`, return True.
    b) Mark the current location as visited.
    c) Explore all neighbors of the current location.
    d) If we find the destination through one of the neighbors, return True.
3) If the DFS function completes without finding the destination, return False.
4) Call the DFS function starting from `source`.
"""
def can_rebook_dfs(flights, source, dest):
    numLocations = len(flights)
    visited = [False] * numLocations
    
    def dfs(currFlightNum):
        # base case 
        if currFlightNum == dest:
            return True
        
        # update visited nodes
        visited[currFlightNum] = True
        
        # recursively call the function until we reach the base case
        for currDestNumber in range(numLocations):
            if visited[currDestNumber] == False and flights[currFlightNum][currDestNumber] == 1:
                foundDestination = dfs(currDestNumber)
                
                if foundDestination:
                    return True
        
        return False
    
    return dfs(source)


# flights1 = [
#     [0, 1, 0], # Flight 0
#     [0, 0, 1], # Flight 1
#     [0, 0, 0]  # Flight 2
# ]

# flights2 = [
#     [0, 1, 0, 1, 0],
#     [0, 0, 0, 1, 0],
#     [0, 0, 0, 0, 1],
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0]
# ]

# print(can_rebook_dfs(flights1, 0, 2))
# print(can_rebook_dfs(flights2, 0, 2)) 

"""
Problem 2: Can Rebook Flight II
If you solved the above problem can_rebook() using Breadth First Search, try solving it using Depth First Search. If you solved it using Depth First Search, solve it using Breadth First Search.

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity.

Understand: 
Input: list (adjacency matrix), int (source), int (destination)
Output: boolean (repsresents whether or not we can reach the destination from the source)
Constraints: 
    - flights[i][j] = 1 means we can get from i to j
Edge Cases:

Plan: Use a BFS to traverse the graph and see if we can get to the destination or not. If the current node's neighbor has a 1 and it is equal to the 
destination, we know it is reachable. 

Pseudo Code:
numLocations = len(flights)

queue = deque([source])
visited = [False] * numLocations

while queue:
    current flight is at the start of the queue (popleft)
    
    update the visited boolean of the current flight to indicate it is visited
    
    iterate through the flight status of the current flight:
        if a flightNum has a status of 1 and it is not visited:
            if the flightNum is the destination number:
                return True
            
            add the flightnum to the queue
            
return False if we go through all paths without finding the destination number 
"""

def can_rebook_bfs(flights, source, dest):
    numLocations = len(flights)
    
    queue = deque([source])
    visited = [False] * numLocations
    
    while queue:
        currentFlightNum = queue.popleft()
        
        visited[currentFlightNum] = True
        
        # check the connected flights for this current flight
        for currDestNum in range(numLocations):
            if flights[currentFlightNum][currDestNum] == 1 and not visited[currDestNum]:
                if currDestNum == dest:
                    return True
                
                queue.append(currDestNum)

    return False

# flights1 = [
#     [0, 1, 0], # Flight 0
#     [0, 0, 1], # Flight 1
#     [0, 0, 0]  # Flight 2
# ]

# flights2 = [
#     [0, 1, 0, 1, 0],
#     [0, 0, 0, 1, 0],
#     [0, 0, 0, 0, 1],
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0]
# ]

# print(can_rebook_bfs(flights1, 0, 2))
# print(can_rebook_bfs(flights2, 0, 2)) 
"""
Problem 3: Number of Flights
You are a travel planner and have an adjacency matrix flights with n airports labeled 0 to n-1 where flights[i][j] = 1 indicates CodePath Airlines offers a flight from airport i to airport j. You are planning a trip for a client and want to know the minimum number of flights (edges) it will take to travel from airport start to their final destination airport destination on CodePath Airlines.

Return the minimum number of flights needed to travel from airport i to airport j. If it is not possible to fly from airport i to airport j, return -1.

Understand:
Input: list (adjacency matrix flights labeled from 0 to n-1)
Output: int (min number of flights (edges) it will take to travel from i to j (airport to destination))
Constraints: 
    - we want the min number of flights
Edge Cases:
    - cannot travel from i to j -> -1
Plan: Use DFS to traverse through each path of the node and determine which path is the min resursively.

Pseudo Code:
numFlights = len(flights)
visited = [False] * numFlights
pathLength = flaot("inf")

def dfs(node, visited, pathTotal):
    update the current node's visited status
    
    Base Case
    if the node is the destinaton, set the pathLength to the min of the current pathLength and current pathTotal, return 
    
    Recursive Case 
    for i in range(numFlights):
        if the neighbor is not visited and it can be visited from the current node:
            make recursive call on the neighbor with updated pathTotal
    
dfs(0, visited, 1)

if pathLength is still inf, return -1
otherwise, return pathLength

Time and Space Complexity:
Time: O(V^2)
Space: O(V)
"""

def counting_flights(flights, i, j):
    numFlights = len(flights)
    pathLength = float("inf")
    
    def dfs(node, currentPathLength):
        # base case
        if node == j:
            nonlocal pathLength
            pathLength = min(pathLength, currentPathLength)
            
        # recursive case    
        for neighborFlight in range(numFlights):
            if flights[node][neighborFlight] == 1:
                dfs(neighborFlight, currentPathLength+1)

    dfs(i, 0)
    
    if pathLength == float("inf"):
        return -1
    
    return pathLength

flights = [
    [0, 1, 1, 0, 0], # Airport 0
    [0, 0, 1, 0, 0], # Airport 1
    [0, 0, 0, 1, 0], # Airport 2
    [0, 0, 0, 0, 1], # Airport 3
    [0, 0, 0, 0, 0]  # Airport 4
]

# print(counting_flights(flights, 0, 2))  
# print(counting_flights(flights, 0, 4))
# print(counting_flights(flights, 4, 0))

"""
BFS Approach
Plan: Use a BFS by creating a queue to keep track of which nodes to traverse next and traverse the graph level by level. If we encounter a node that 
is equal to the destination. We have found the shortest path to it. Update the pathlength and return the pathlength. 

numFlights = len(flights)
queue = deque([starting node])
visited = [False] * len(numFlights)
level = 0

while queue:
    levelLen = len(queue)
    
    for i in range(levelLen):
        process the current node by popping from the queue
        update it's status in the visited list
        
        if the current node is the destination, retrun the level
        
        for neighborFlightNum in range(numFlights):
            if the neighbor is not visited and it is connected to the current node: 
        
    increment the level after the current level has been processed

return -1


Time and Space Complexity:
Time: O(V^2) - go through each node and then the node's neighbors to check if they are connected
Space: O(V) - queue will hold at most v nodes in the case where all nodes are connected
"""

def counting_flights_bfs(flights, i, j):
    queue = deque([i])
    visited = [False] * len(flights)
    level = 0
    
    while queue:
        # proces the current level
        levelLen = len(queue)
        
        for i in range(levelLen):
            currentNode = queue.popleft()
            visited[currentNode] = 1
            
            if currentNode == j:
                return level
            
            # add the current node's neighbor's to be processed after this level
            for neighborFlightNum in range(len(flights)):
                if not visited[neighborFlightNum] and flights[currentNode][neighborFlightNum] == 1:
                    queue.append(neighborFlightNum)
        
        level += 1

    # return -1 if we go through all nodes and never found the destination
    return -1

# print(counting_flights_bfs(flights, 0, 2))  
# print(counting_flights_bfs(flights, 0, 4))
# print(counting_flights_bfs(flights, 4, 0))
"""
Problem 4: Number of Airline Regions
CodePath Airlines operates in different regions around the world. Some airports are connected directly with flights, while others are not. However, if airport a is connected directly to airport b, and airport b is connected directly to airport c, then airport a is indirectly connected to airport c.

An airline region is a group of directly or indirectly connected airports and no other airports outside of the group.

You are given an n x n matrix is_connected where is_connected[i][j] = 1 if CodePath Airlines offers a direct flight between airport i and airport j, and is_connected[i][j] = 0 otherwise.

Return the total number of airline regions operated by CodePath Airlines.

Understand: 
Input: n x n matrix (is_connected[i][j] = 1)
Output: int (total number of airline regions)
Constraints:
    - airline region is a group of directly/indirectly connected airports and no other airports outside of the group
Edge Cases:

Plan: use a DFS traversal and keep track of the nodes that have already been visited. There is a new region when we encounter a flight that has 
not been visited because it is not connected to the region of flights we performed the dfs on. 

Pseudo Code:
visited = set()
totalRegions

def dfs(node, visited):
    add the current node to the visited set
    
    for neighborNodeNum in range(len(is_connected)):
        if neighborNodeNum is not visited and it is connectedd, recursively call the function on this node 
        
for flightNum in range(is_connected):
    if flightNum not in visited:
        call the dfs function on the current node
        increment the total number of regions
        
return totalRegions
"""

def num_airline_regions(is_connected):
    visited = set()
    totalRegions = 0
    
    def dfs(node, visitd):
        visitd.add(node)
        
        for neighborNodeNum in range(len(is_connected)):
            if neighborNodeNum not in visitd and is_connected[node][neighborNodeNum] == 1:
                dfs(neighborNodeNum, visited)

    for flightNum in range(len(is_connected)):
        if flightNum not in visited:
            dfs(flightNum, visited)
            totalRegions += 1
    
    return totalRegions

is_connected1 = [
    [1, 1, 0],
    [1, 1, 0],
    [0, 0, 1]
]

is_connected2 = [
    [1, 0, 0, 1],
    [0, 1, 1, 0],
    [0, 1, 1, 0],
    [1, 0, 0, 1]
]

# print(num_airline_regions(is_connected1))
# print(num_airline_regions(is_connected2)) 

"""
Problem 5: Get Flight Cost
You are given an adjacency dictionary flights where for any location source, flights[source] is a list of tuples in the form (destination, cost) indicating that there exists a flight from source to destination at ticket price cost.

Given a starting location start and a final destination dest return the total cost of flying from start to dest. If it is not possible to fly from start to dest, return -1. If there are multiple possible paths from start to dest, return any of the possible answers.

Understand:
Input:adjacency dict (flights, flights[source] = (destination, cost)]), start (source name), destination (dest name)
Output: integer (cost to get from start to end), -1 if not possible
Constraints:
Edge Cases:

Plan: Use a DFS to search through each path until one from the start to the destination is found. To keep track of the cost, add a a parameter to the dfs
helper function. 

Pseudo Code:
visited = set()

def dfs(node, visited, totalCost):
    add the current node to the visited set
    
    Base Case
    if node is equal to the dest, return the total cost
    
    call the dfs helper function on the current node's list of neighbors and update the total cost
    
    remove current node from visited to backtrack for dfs
    return -1 if all paths are visited and there is no dest node
    
return call the dfs function on the starting noode with the visited set and totalCost of 0
"""

def calculate_cost(flights, start, dest):
    visited = set()
    
    def dfs(node, visited, totalCost):
        visited.add(node)
        
        # base case
        if node == dest:
            return totalCost
        
        # recursive calls
        neighbors = flights[node]
        
        for currNeighbor, currNeighborCost in neighbors:
            if currNeighbor not in visited:
                res = dfs(currNeighbor, visited, totalCost + currNeighborCost)
                
                if res != -1:
                    return res
        
        # dfs backtracking 
        # visited.remove(node)
        
        return -1

    return dfs(start, visited, 0)

flights = {
    'LAX': [('SFO', 50)],
    'SFO': [('LAX', 50), ('ORD', 100), ('ERW', 210)],
    'ERW': [('SFO', 210), ('ORD', 100)],
    'ORD': [('ERW', 300), ('SFO', 100), ('MIA', 400)],
    'MIA': [('ORD', 400)]
}

print(calculate_cost(flights, 'LAX', 'MIA'))

"""
Problem 6: Fixing Flight Booking Software
CodePath Airlines uses Breadth First Search to suggest the route with the least number of layovers to its customers. But their software has a bug and is malfunctioning. Help the airline by identifying and fixing the bug.

When properly implemented, the function should accept an adjacency dictionary flights and returns a list with the shortest path from a source location to a destination location.

For this problem:

Identify and fix any bug(s) in the code.

Evaluate the time complexity of the function. Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity.

If CodePath Airlines used an adjacency matrix instead of an adjacency dictionary/list, would the time complexity change? Why or why not?

Understand:
Input:
Output:
Constraints:
Edge Cases:

Plan:

Pseudo Code:
"""

"""
Problem 7: Expanding Flight Offerings
CodePath Airlines wants to expand their flight offerings so that for any airport they operate out of, it is possible to reach all other airports. They track their current flight offerings in an adjacency dictionary flights where each key is an airport i and flights[i] is an array indicating that there is a flight from destination i to each destination in flights[i]. Assume that if there is flight from airport i to airport j, the reverse is also true.

Given flights, return the minimum number of flights (edges) that need to be added such that there is flight path from each airport in flights to every other airport.

Understand:
Input: adjacency dict (flights, where flight[i] contains a list of airport destinations) 
Output: integer (min number of flights (edges) that need to be added such that there is a flight from each airport from flights to every other airport)
Constraints:
    - if there is a flight from i to j, the reverse is also true
Edge Cases:

Plan: Use a dfs to find the number of regions or components in the graph. The min number of flights that need to be added to connect all these are 
essentially going to be the total number of components/regions - 1. 

Pseudo Code:
visited = set()
totalRegions = 0

def dfs(node, visited):
    add node to visited
    
    recursively call the dfs function on the current node's neighbor if it has not been visited yet

for each key (location) in the adjacecency dict:
    if the location has not been visited, call the recursive dfs function on the location and increment the region count
    
return totalRegions - 1

Time and Space Complexity:
Time: O(n) - visit each node at least one time 
Space: O(n) - using a set to store the nodes that have been visited
"""

def  min_flights_to_expand(flights):
    visited = set()
    totalRegions = 0 
    
    # helper function for the dfs 
    def dfs(node, visited):
        visited.add(node)
        
        neighbors = flights.get(node, [])
        
        for currNeighbor in neighbors:
            if currNeighbor not in visited:
                dfs(currNeighbor, visited)
    
    # call the dfs on each location if it has not been visited yet (indicates a new region)
    for location in flights:
        if location not in visited:
            dfs(location, visited)
            totalRegions += 1
    
    return max(0, totalRegions - 1)

flights = {
    'JFK': ['LAX', 'SFO'],
    'LAX': ['JFK', 'SFO'],
    'SFO': ['JFK', 'LAX'],
    'ORD': ['ATL'],
    'ATL': ['ORD']
}

print(min_flights_to_expand(flights))

"""
Problem 8: Get Flight Itinerary
Given an adjacency dictionary of flights flights where each key is an airport i and flights[i] is an array indicating that there is a flight from destination i to each destination in flights[i], return an array with the flight path from a given source location to a given destination location.

If there are multiple flight paths from the source to destination, return any flight path.

Understand:
Input:
Output:
Constraints:
Edge Cases:

Plan:

Pseudo Code:
"""
