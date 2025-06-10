"""
Given two lists of strings artists and set_times of length n, write a function lineup() that maps each artist to their set time.
An artist artists[i] has set time set_times[i]. Assume i <= 0 < n and len(artists) == len(set_times).

Understand: 
Input - two lists of strings (artists and set_times)
Output - dict (key: artist, value: time)
Constraints - i <= 0 < n and len(artists) === len(set_times)
Edge - empty lists: return empty dict 

Plan: 
1. Create an empty dict 
2. Create a loop for len(either list) iterations and map the value in each list 
at i as a key value pair 
3. return the dict 
"""

def lineup(artists, set_times):
  result = {}

  for i in range(len(artists)):
    result[artists[i]] = set_times[i]

  return result

artists1 = ["Kendrick Lamar", "Chappell Roan", "Mitski", "Rosalia"]
set_times1 = ["9:30 PM", "5:00 PM", "2:00 PM", "7:30 PM"]

artists2 = []
set_times2 = []

print(lineup(artists1, set_times1))
print(lineup(artists2, set_times2))

