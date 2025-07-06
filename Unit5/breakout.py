class Villager:
    def __init__(self, name, species, personality, catchphrase, neighbor=None):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.personality = personality
        self.furniture = []
        self.neighbor = neighbor


    def add_item(self, item_name):
        self.furniture.append(item_name)

# Problem 2
# alice = Villager("Alice", "Koala", "guvnor")
# print(alice.furniture)

# alice.add_item("acoustic guitar")
# print(alice.furniture)

# alice.add_item("cacao tree")
# print(alice.furniture)

# alice.add_item("nintendo switch")
# print(alice.furniture)


# Problem 3
"""
input: townies (list of villagers), personaility_type (string)
output: list (villigers of personanility type x)
"""

def of_personality_type(townies, personility_type):
    result = []
    
    for villager in townies:
        if villager.personality == personility_type:
            result.append(villager.name)
            
    return result

# isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
# bob = Villager("Bob", "Cat", "Lazy", "pthhhpth")
# stitches = Villager("Stitches", "Cub", "Lazy", "stuffin'")

# print(of_personality_type([isabelle, bob, stitches], "Lazy"))
# print(of_personality_type([isabelle, bob, stitches], "Cranky"))


# Problem 4
""" 
U 
    I - two villagers (start and target)
    O - boolean
    C - able to pass a message from start to target through a series of neighbors
    E - if one of the neighbors is None, return False

P
    Navigate through the linked using the conditions "villager.neighbor is not None"
        if neighbor == target:
            return True
        else:
            move to the neighbor
    return False
"""
def message_received(start_villager, target_villager):
    current = start_villager

    while current:
        if current.neighbor == target_villager:
            return True
        current = current.neighbor

    return False

# isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
# tom_nook = Villager("Tom Nook", "Raccoon", "Cranky", "yes, yes")
# kk_slider = Villager("K.K. Slider", "Dog", "Lazy", "dig it")
# isabelle.neighbor = tom_nook
# tom_nook.neighbor = kk_slider

# print(message_received(isabelle, kk_slider))
# print(message_received(kk_slider, isabelle))

# Problem 5
"""
Plan: Connect the nodes to their respective next nodes given in the example
"""
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

# kk_slider = Node("K.K. Slider")
# harriet = Node("Harriet")
# saharah = Node("Saharah")
# isabelle = Node("Isabelle")

# kk_slider.next = harriet
# harriet.next = saharah
# saharah.next = isabelle

# print_linked_list(kk_slider)

# Problem 6
"""
U 
    I - head of a linked list
    O - return new head or print "Aw! Better luck next time!", return None
    C - print name of fish in head using given format
    E - 

P  
    if head: 
        print the name of the fish, change head to head.next
    print the error message
    return None
"""
class Node:
    def __init__(self, fish_name, next=None):
        self.fish_name = fish_name
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.fish_name, end=" -> " if current.next else "\n")
        current = current.next

def catch_fish(head):
    if head:
        print(f"I caught a ${head.fish_name}")
        head = head.next
        return head
    else:
        print("Aw! Better luck next time!")
        return None
    
# fish_list = Node("Carp", Node("Dace", Node("Cherry Salmon")))
# empty_list = None

# print_linked_list(fish_list)
# print_linked_list(catch_fish(fish_list))
# print(catch_fish(empty_list))

# Problem 7
"""
Input: linked list (head) and string (fish name)
Output: return number rounded to nearest hundreth (chances that the player will catch a fish of type fish_name)
Constraints: rounding down
Edge Cases:
    - empty list: reutrn 0.00
    
Plan: 
* divide number of fish_name by the total fishes in the list

length = 0
totalFishName = 0
current = head 

while current:
    increment length
    
    if current.fish_name == fish_name:
        increment totalFishName 
        
return round(float(totalFishName / length), 2)

"""
class Node:
    def __init__(self, fish_name, next=None):
        self.fish_name = fish_name
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.fish_name, end=" -> " if current.next else "\n")
        current = current.next

def fish_chances(head, fish_name):
    length = 0
    totalFishName = 0
    
    current = head 
    
    while current:
        length += 1
        
        if current.fish_name == fish_name:
            totalFishName += 1
            
        current = current.next
            
    return round((float(totalFishName) / float(length)), 2)

fish_list = Node("Carp", Node("Dace", Node("Cherry Salmon")))
# print(fish_chances(fish_list, "Dace"))
# print(fish_chances(fish_list, "Rainbow Trout"))

