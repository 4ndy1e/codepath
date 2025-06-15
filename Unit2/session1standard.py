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

# artists1 = ["Kendrick Lamar", "Chappell Roan", "Mitski", "Rosalia"]
# set_times1 = ["9:30 PM", "5:00 PM", "2:00 PM", "7:30 PM"]

# artists2 = []
# set_times2 = []

# print(lineup(artists1, set_times1))
# print(lineup(artists2, set_times2))

# ---

"""
You are designing an app for your festival to help attendees have the best experience possible! As part of the application, users will be able to easily search their favorite artist and find out the day, time, and stage the artist is playing at. Write a function get_artist_info() that accepts a string artist and a dictionary festival_schedule mapping artist's names to dictionaries containing the day, time, and stage they are playing on. Return the dictionary containing the information about the given artist.

If the artist searched for does not exist in festival_schedule, return the dictionary {"message": "Artist not found"}.

Understand: 
Input - Artist (string), festival schedule (dict)
Output - Dict (containing day, time, stage)
Constraints - return artist not found if no artist in schedule 
Edge Cases - n/a 

Plan:
1. Check dict to see if artist exists inside the dict 
2. if artist exists, return the value of the artist, using the artist's naem as the key
3. return a dict with a key of 'message' and value of 'Artist not found' otherwise 
"""

def get_artist_info(artist, festival_schedule):
  if artist in festival_schedule:
    return festival_schedule[artist]
  return {'message' : 'Artist not found'}

# festival_schedule = {
#     "Blood Orange": {"day": "Friday", "time": "9:00 PM", "stage": "Main Stage"},
#     "Metallica": {"day": "Saturday", "time": "8:00 PM", "stage": "Main Stage"},
#     "Kali Uchis": {"day": "Sunday", "time": "7:00 PM", "stage": "Second Stage"},
#     "Lawrence": {"day": "Friday", "time": "6:00 PM", "stage": "Main Stage"}
# }

# print(get_artist_info("Blood Orange", festival_schedule)) 
# print(get_artist_info("Taylor Swift", festival_schedule))




"""
Given two lists of length n, crew and position, map the space station crew to their position on board the international space station.
Each crew member crew[i] has job position[i] on board, where 0 <= i < n and len(crew) == len(position).

Input:
  Two lists: crew and position of length n
Output:
  Dict mapping each crew member to their position
Constraints:
  0 <= i < n
  len(crew) === len(position)
Edge Cases: 
  Empty list: return {}
  Empty name: skip

Plan: 
  Initialize empty dict
  Use a for loop iterate through both lists mapping each crew and position at index i to to each other as key and value pairs 
"""

def space_crew(crew, position):
  res = {}

  for i in range(len(crew)):
    res[crew[i]] = position[i]

  return res

# exp70_crew = ["Andreas Mogensen", "Jasmin Moghbeli", "Satoshi Furukawa", "Loral O'Hara", "Konstantin Borisov"]
# exp70_positions = ["Commander", "Flight Engineer", "Flight Engineer", " Flight Engineer", "Flight Engineer"] 

# ax3_crew = ["Michael Lopez-Alegria", "Walter Villadei", "Alper Gezeravci", "Marcus Wandt"]
# ax3_positions = ["Commander", "Mission Pilot", "Mission Specialist", "Mission Specialist"]

# print(space_crew(exp70_crew, exp70_positions))
# print(space_crew(ax3_crew, ax3_positions))

"""
Write a function data_difference() that accepts two dictionaries experiment1 and experiment2 and returns a new dictionary that contains only key-value pairs found exclusively in experiment1 but not in experiment2.

Input: Two dictionaries (experiment1 experiment2)
Output: Dictionary (key-val pairs only found in experiment1)
Constraints: exclusively experiment1
Edge Cases: 
  Empty lists: return {}
  Everything in exp1 is in exp2: return {}

Plan: 
  1. Create empty dict
  2. Loop through exp1 and check if the current key-val pair is exclusive 
      - exp1 key does not exist in exp2
      - exp1[key] != exp2[key]   #values do not equal each other 
  3. return dict 
"""

def data_difference(exp1, exp2):
  res = {}

  for key, val in exp1.items():

    if key not in exp2.keys() or exp1[key] != exp2[key]:
      res[key] = val 

  return res

# exp1_data = {'temperature': 22, 'pressure': 101.3, 'humidity': 45}
# exp2_data = {'temperature': 18, 'pressure': 101.3, 'radiation': 0.5}

# print(data_difference(exp1_data, exp2_data))


"""
NASA has asked the public to vote on a new name for one of the nodes in the International Space Station. Given a list of strings votes where each string in the list is a voter's suggested new name, implement a function get_winner() that returns the suggestion with the most number of votes.

If there is a tie, return either option.

Input: List (votes, where each index is a vote for the name)
Output: String (name of the most voted)
Constraints: Return only one string 
Edge Cases: 
  Empty List: empty string
  Empty name: Skip over it 

Plan: 
  1. Create a dict to store the  frequency of all names
  2. Create a loop to go through each name and increment the value of each name when it occurs
  3. Return the max of key of the dict
"""

def get_winner(votes):
  freqeuncy = {}

  highestVote = 0
  mostVotedName = ""

  for name in votes:
    freqeuncy[name] = freqeuncy.get(name, 0) + 1

    if freqeuncy[name] > highestVote:
      highestVote = freqeuncy[name]
      mostVotedName = name

  return mostVotedName


# votes1 = ["Colbert", "Serenity", "Serenity", "Tranquility", "Colbert", "Colbert"]
# votes2 = ["Colbert", "Serenity", "Serenity", "Tranquility", "Colbert"]

# print(get_winner(votes1))
# print(get_winner(votes2))

