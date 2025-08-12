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

print(list(flights.keys()))
print(list(flights.values()))
print(flights["JFK"])