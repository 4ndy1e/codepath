# Probelm 1: Next in Queue

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

# For testing
def print_queue(head):
    current = head.front
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()

# Solve here
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def is_empty(self):
        return not self.front
    
    """
    edge cases: empty queue -> tuple will be front and rear
    """
    def enqueue(self, my_tuple):
        my_node = Node(my_tuple)

        if not self.front:
            self.front = my_node
            self.rear = my_node
            return

        self.rear.next = my_node
        self.rear = my_node
    
    """edge cases: empty queue -> None
                   queue has one node -> self.front
    """
    def dequeue(self):
        if not self.front:
            return None

        if not self.front.next:
            my_node = self.front
            self.front, self.rear = None, None
            return my_node.value

        front_node = self.front
        self.front = self.front.next
        return front_node.value
    
    def peek(self):
        if not self.front:
            return None

        return self.front.value

# q = Queue()

# # Add elements to the queue
# q.enqueue(('Love Song', 'Sara Bareilles'))
# q.enqueue(('Ballad of Big Nothing', 'Elliot Smith'))
# q.enqueue(('Hug from a Dinosaur', 'Torres'))
# print_queue(q)

# # View the front element
# print("Peek: ", q.peek()) 

# # Remove elements from the queue
# print("Dequeue: ", q.dequeue()) 
# print("Dequeue: ", q.dequeue()) 

# # Check if the queue is empty
# print("Is Empty: ", q.is_empty()) 

# # Remove the last element
# print("Dequeue: ", q.dequeue()) 

# # Check if the queue is empty
# print("Is Empty:", q.is_empty()) 


"""
input: head of two linked lists (playlist1 and playlist 2), positions of a and b
output: playlist1 with the modified ath to the bth node and put playlist2 in its place
constraints: 
    - ath to bth must be playlist2 in its place 
edge cases:
    - both lists are empty -> empty list
    - playlist1 is empty -> return empty list
    - playlist2 is empty -> playlist1
    
Plan: 
High Level: keep track of the index of playlist1 until we get to the a-1th position. At index a-1, point the current node's pointer to playlist2's head. Move through the list2 until we get to the end of linkedlist2, then refer back to the current node at b+1th position in list1. 

currentIndex = 0
currA = playlist1
currB = playlist1

while currA and currIndex < a:
    currA = currA.next
    currIndex += 1
    
while currB and currIndex < b+2:
    currB = currB.next
    currentindex += 1
    
currA.next (represent a-1th node) = playlist2
curr2  = currA.next

while curr2:
    curr2 = curr2.next
    
curr2.next = currB

return playlist1
"""

def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()



def merge_playlists(playlist1, playlist2, a, b):
    if not playlist1 and not playlist2:
        return None
    if not playlist1: 
        return None
    if not playlist2:
        return playlist1
    
    currIndex = 0
    currA = playlist1
    currB = playlist1

    while currA and currIndex < a-1:
        currA = currA.next
        currB = currB.next
        currIndex += 1
        
    while currB and currIndex < b+1:
        currB = currB.next
        currIndex += 1
    
    print(f"Current node A ({currA.value})")
    currA.next = playlist2
    curr2  = currA.next

    while curr2.next:
        curr2 = curr2.next
    
    print(f"Current node B ({currB.value})")
    curr2.next = currB

    return playlist1

playlist1 = Node(('Flea', 'St. Vincent'),
                Node(('Juice', 'Lizzo'), 
                    Node(('Tenderness', 'Jay Som'),
                        Node(('Ego Death', 'The Internet'),
                            Node(('Empty', 'Kevin Abstract'))))))

playlist2 = Node(('Dreams', 'Solange'), Node(('First', 'Gallant')))

print_linked_list(merge_playlists(playlist1, playlist2, 2, 3))

