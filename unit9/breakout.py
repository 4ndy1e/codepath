from collections import deque 

# Tree Node class
class TreeNode:
    def __init__(self, value, key=None, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def print_tree(root):
    if not root:
        return "Empty"
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    print(result)

def build_tree(values):
    if not values:
        return None

    def get_key_value(item):
        if isinstance(item, tuple):
            return item[0], item[1]
        else:
            return None, item

    key, value = get_key_value(values[0])
    root = TreeNode(value, key)
    queue = deque([root])
    index = 1

    while queue:
        node = queue.popleft()
        if index < len(values) and values[index] is not None:
            left_key, left_value = get_key_value(values[index])
            node.left = TreeNode(left_value, left_key)
            queue.append(node.left)
        index += 1
        if index < len(values) and values[index] is not None:
            right_key, right_value = get_key_value(values[index])
            node.right = TreeNode(right_value, right_key)
            queue.append(node.right)
        index += 1

    return root

"""
U 
    I - roots of two binary trees (guest1 and guest2)
    O - boolean
    C - binary trees must be structurally identical and nodes have the same values
    E - both nodes at the same position are empty -> True
      - nodes have different values -> False
      - one node is None -> False

P   
    HL: Base cases:
    if not guest1 and not guest2: return True
    if not guest1 or not guest2: return False
    if guest1.val != guest2.val: return False
    return is_clone(guest1.left, guest2.left) and is_clone(guest1.right, guest2.right)

Time: O(n)
Space: O(h) - on the call stack
"""

def is_clone(guest1, guest2):
    if not guest1 and not guest2: 
        return True

    if not guest1 or not guest2: 
        return False

    if guest1.val != guest2.val: 
        return False
        
    return is_clone(guest1.left, guest2.left) and is_clone(guest1.right, guest2.right)

"""
     John Doe               John Doe
     /      \             /       \
  6 ft    Brown Eyes      6ft      Brown Eyes
"""
# guest1 = TreeNode("John Doe", TreeNode("6 ft"), TreeNode("Brown Eyes"))
# guest2 = TreeNode("John Doe", TreeNode("6 ft"), TreeNode("Brown Eyes"))

"""
     John Doe         John Doe
     /                       \
   6 ft                     6 ft
"""
# guest3 = TreeNode("John Doe", TreeNode("6 ft"))
# guest4 = TreeNode("John Doe", None, TreeNode("6 ft"))

# print(is_clone(guest1, guest2))
# print(is_clone(guest3, guest4))


class Room:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

"""
Input: root (binary tree that represents hotel)
Output: list (each room level by level froml left to right)
Constraints: 
    - in the order of left to right level by level
Edge Cases:
    - empty root: return []

Plan: use a BFS to traverse level by level through the tree and add the nodes from in the order of left to right. 

Psuedo Code:
queue = deque()
queue.append(root)

visited = []

# traverse the tree 
while there is a node in the queue:
    currentNode = queue.popleft()
    
    add the currentNode to the visitied list
    
    add the currentNode's left and right subtrees to the queue if they exist
    
return visited 

Time and Space Complexity:
Time - O(n): go through all nodes level by level
Space: O(n): visited nodes array to store result
"""
def map_hotel(hotel):
    # base 
    if not hotel:
        return []
    
    queue = deque()
    queue.append(hotel)
    
    visited = []
    
    while queue:
        currentNode = queue.popleft()
        
        visited.append(currentNode.val)
        
        if currentNode.left:
            queue.append(currentNode.left)
        if currentNode.right:
            queue.append(currentNode.right)

    return visited

"""
         Lobby
        /     \
       /       \
      101      102
     /   \    /   \
   201  202  203  204
   /                \ 
 301                302
"""

# hotel = Room("Lobby", 
#                 Room(101, Room(201, Room(301)), Room(202)),
#                 Room(102, Room(203), Room(204, None, Room(302))))

# print(map_hotel(hotel))

"""
U   
    I - root of a binary tree (door)
    O - integer (minimum depth)
    C - minimum depth is number of nodes from root to nearest leaf node
    E - root is None -> 0
      - [root] -> 1

P   
    HL: Base case: if not root: return 0

    return 1 + min(min_depth(root.left), min_depth(root.right))

Time: O(n) 
Space: O(n) - on the call stack
"""
def min_depth(door):
    if not door:
        return 0

    return 1 + min(min_depth(door.left), min_depth(door.right))


door = Room("Door", Room("Attic"), Room("Cursed Room", Room("Crypt"), Room("Haunted Cellar")))

# print(min_depth(door))

"""
Plan: Use BFS to find the minimum dpeth of the secret path by visited the tree level by level from left to right. 

Base Case:
if root is empty:
    return 0

queue = deque()
queue.append(root)

depth = 1

while queue:
    currentNode = queue.popleft()
    
    if currentNode does not have a left and right child (leaf node):
        break
    if currentNode.left:
        add to the queue
    if current.right:
        add to the queue
        
    depth += 1

return depth

Time and Space Complexity:
Time - O(n): worse case, we got through all nodes
Space - O(n): O(n/2) = O(n)
"""

def min_depth_bfs(root):
    if not root:
        return 0
    
    queue = deque()
    queue.append(root)
    
    depth = 1
    
    while queue:
        currentNode = queue.popleft()
        
        if not currentNode.left and not currentNode.right:
            break
        if currentNode.left:
            queue.append(currentNode.left)    
        if currentNode.right:
            queue.append(currentNode.right)
            
        depth += 1
        
    return depth


print(min_depth_bfs(door))