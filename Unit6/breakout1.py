# top_hits_2010s = SongNode("Uptown Funk", SongNode("Party Rock Anthem", SongNode("Bad Romance")))

# uptown_funk = SongNode("Uptown Funk")
# party_rock_anthem = SongNode("Party Rock Anthem")
# bad_romance = SongNode("Bad Romance")
# uptown_funk.next = party_rock_anthem
# party_rock_anthem.next = bad_romance
# print_linked_list(uptown_funk)

"""
input: linked list (playlist)
output: dict (maps each artist in the list to its frequency)
constraints: 
edge cases: 
    - empty playlist -> empty dict

plan: 
high level: Loop through the play list and look at each song's artist creating a dict to keep track of the frequency

Time: O(n)
Space: O(n)
"""

class SongNode:
    def __init__(self, song, artist, next=None):
        self.song = song
        self.artist = artist
        self.next = next

# For testing
def print_linked_list(node):
    current = node
    while current:
        print((current.song, current.artist), end=" -> " if current.next else "")
        current = current.next
    print()

def get_artist_frequency(playlist):
    curr = playlist
    frequency = {}
    
    while curr: 
        # check for song's artist
        frequency[curr.artist] = frequency.get(curr.artist, 0) + 1
        curr = curr.next
    
    return frequency

playlist = SongNode("Saturn", "SZA", 
                SongNode("Who", "Jimin", 
                        SongNode("Espresso", "Sabrina Carpenter", 
                                SongNode("Snooze", "SZA"))))

# print(get_artist_frequency(playlist))


# problem 3
# Function with a bug!
"""
Input: linked list with songs, song
Output: modified linked list without song
Constraints: none
Examples/edge cases: empty linked list -> None
                     song does not exist in linked list -> head of linked list
                     song is head of linked list -> head will be head.next

Time: O(n)
Space: O(1)
"""
def remove_song(playlist_head, song):
    if not playlist_head:
        return None
    if playlist_head.song == song:
        return playlist_head.next

    current = playlist_head
    while current.next:
        if current.next.song == song:
            current.next = current.next.next  
            return playlist_head 
        current = current.next

    return playlist_head

# playlist = SongNode("SOS", "ABBA", 
#                 SongNode("Simple Twist of Fate", "Bob Dylan",
#                     SongNode("Dreams", "Fleetwood Mac",
#                         SongNode("Lovely Day", "Bill Withers"))))

# print_linked_list(remove_song(playlist, "Dreams"))


"""
input: playlist (linked list)
output: boolean (true if playlist has a cycle)
constraints: 
edge cases: 
    - empty list -> return False
    - one node (points itself) -> return True
    - one node -> return False
    
Plan: 
High Level: Create a slow and fast pointer to go through the list (fast moves 2 nodes, slow moves 1 node), if they land on the same node, return True (represents a cycle is in the list)

slow = fast = head

while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    
    if slow == fast:
        return True
        
return False

Time and Space Complexity: 
time: O(n)
space: O(1)
"""

def on_repeat(playlist_head):
    slow = fast = playlist_head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True
        
    return False
    
# song1 = SongNode("GO!", "Common")
# song2 = SongNode("N95", "Kendrick Lamar")
# song3 = SongNode("WIN", "Jay Rock")
# song4 = SongNode("ATM", "J. Cole")
# song1.next = song2
# song2.next = song3
# song3.next = song4
# song4.next = song2

# print(on_repeat(song1))
    
"""
Input: head (playlist_head)
Output: length of the cycle (if any)
Constraints: 
Edge Cases: 
    - Empty list -> return 0
    - List of one node (with cycle) -> return 1
    
Plan:
High Level: Use the fast and slow pointer technique to determine whether or not there is a cycle. If there is a cycle, find the start of the cycle (setting flow to head, moving fast one step). Once the pointers meet, this is the start. Initialize a pointer to keep track of the start and move one pointer until it meets the start again (keep track of length).

Determine whether or not the list contains a cycle:
slow = fast = head

while fast and fast.next: 
    slow = slow.next
    fast = fast.next.next
    
    if slow == fast:
        break
else:
    return 0
    
Find the start of the cycle:
slow = head

while slow != fast:
    slow = slow.next
    fast = fast.next
    
Keep track of the length and move one of the pointers until they land on each other again
length = 1
start = slow 
fast = fast.next

while fast != start:
    length += 1
    fast = fast.next
    
return length
"""

def loop_length(playlist_head):
    slow = fast = playlist_head
    
    # Determine whether a cycle is in the list or not 
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            break
    else:
        return 0
    
    # Find the start of the linked list cycle
    slow = playlist_head
    
    while slow != fast:
        slow = slow.next
        fast = fast.next
        
    # Find the length of the linked list cycle
    length = 1
    start = slow 
    fast = fast.next
    
    while fast != start:
        length += 1
        fast = fast.next
        
    return length

song1 = SongNode("Wein", "AL SHAMI")
song2 = SongNode("Si Ai", "Tayna")
song3 = SongNode("Qalbi", "Yasser Abd Alwahab")
song4 = SongNode("La", "DYSTINCT")
song1.next = song2
song2.next = song3
song3.next = song4
song4.next = song2

print(loop_length(song1))