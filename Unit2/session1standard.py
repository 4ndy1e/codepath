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

festival_schedule = {
    "Blood Orange": {"day": "Friday", "time": "9:00 PM", "stage": "Main Stage"},
    "Metallica": {"day": "Saturday", "time": "8:00 PM", "stage": "Main Stage"},
    "Kali Uchis": {"day": "Sunday", "time": "7:00 PM", "stage": "Second Stage"},
    "Lawrence": {"day": "Friday", "time": "6:00 PM", "stage": "Main Stage"}
}

print(get_artist_info("Blood Orange", festival_schedule)) 
print(get_artist_info("Taylor Swift", festival_schedule))  



