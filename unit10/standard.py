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
print(get_adj_dict(flights))

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
    flightsDict = get_adj_dict(terminals)
    centerFlightNumber = -1
    
    for flightNumber, flightConnectionsList in flightsDict.items():
        if len(flightConnectionsList) == len(flightsDict)-1:
            centerFlightNumber = max(centerFlightNumber, flightNumber)
            
    return centerFlightNumber

terminals1 = [[1,2],[2,3],[4,2]]
terminals2 = [[1,2],[5,1],[1,3],[1,4]]

print(find_center(terminals1))
print(find_center(terminals2))