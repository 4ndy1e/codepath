from collections import deque 

# Tree Node class
class TreeNode:
    def __init__(self, value, left=None, right=None):
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

# root = TreeNode("Trunk")
# root.left = TreeNode("McIntosh", TreeNode("Fuji"), TreeNode("Opal"))
# root.right = TreeNode("Granny Smith", TreeNode("Crab"), TreeNode("Gala"))
# print_tree(root)


"""
Input: root 
Output: integer (result of the operation type applied on the leaf nodes)
Constraints:   
    - leaf nodes are integer values
    - root has a string value of +, -, *, /
    - 3 node binary tree 
Edge Cases:

Plan: Identify the operation at the root of the tree and perform that operation on the leaf nodes, from leaf to right.
ex: left node value (operation type) right node value
"""
def calculate_yield(root):
    match(root.val):
        case("+"): return root.left.val + root.right.val
        case("-"): return root.left.val - root.right.val
        case("*"): return root.left.val * root.right.val
        case("/"): return root.left.val / root.right.val

# apple_tree = TreeNode("+", TreeNode(7), TreeNode(5))
# print(calculate_yield(apple_tree

"""
U
    I - root (of an ivy plant)
    O - list of nodes (from root to rightmost node)
    C - none
    E - only root -> [root]
      - there is no root.right -> [root]

P:
    HL: Initialize a right_leaves array.
    Initialize right_pointer = root
    While right_pointer:
        right_leaves.append(right_pointer.val)
        right_pointer = right_pointer.right

    return right_leaves

Time: O(log n)
Space: O(log n)
"""

def right_vine(root):
    right_leaves, right_pointer = [], root

    while right_pointer:
        right_leaves.append(right_pointer.val)
        right_pointer = right_pointer.right

    return right_leaves

"""
        Root
      /      \
    Node1    Node2
  /         /    \
Leaf1    Leaf2  Leaf3
"""
ivy1 = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

"""
      Root
      /  
    Node1
    /
  Leaf1  
"""
ivy2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))

# print(right_vine(ivy1))
# print(right_vine(ivy2))
"""
Input: root node of the tree
Output: list (represents nodes of the rightmost vine)
Constraints: 
    - list only contains node values from the rightmost vine
    - recursive
Edge: 
    - only root node -> [root]
    - no right subtree -> [root]
    
Plan: Use recursion to traverse the tree and add the node values to a list. 

Base Case
if root == None:
    return []
    
return [root.val] + right_vine_recursively(root.right)

Time and Space Complexity:
time - O(log n)
space - O(log n)
"""
def right_vine_recursively(root):
    # base case 
    if root == None:
        return []
    
    return [root.val] + right_vine_recursively(root.right)
    
# print(right_vine_recursively(ivy1))
# print(right_vine_recursively(ivy2)(

"""
U
    I - root (of an acorn tree)
    O - int (number of leaves on the tree)
    C - leaf has no children
    E - root -> 1

P: Traverse through the tree recursively to determine the number of leaves

Base case:
if not root: return 0

if not root.left and not root.right: return 1

return 0 + survey_tree(root.left) + survey_tree(root.right).

Time: O(n)
Space: O(log n) on the call stack
"""
def count_leaves(root):
    if not root:
        return 0

    if not root.left and not root.right:
        return 1

    return 0 + count_leaves(root.left) + count_leaves(root.right)

"""
        Root
      /      \
    Node1    Node2
  /         /    \
Leaf1    Leaf2  Leaf3
"""

oak1 = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

"""
      Root
      /  
    Node1
    /
  Leaf1  
"""
oak2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))

# print(count_leaves(oak1))
# print(count_leaves(oak2))

"""
Input: root node 
Output: list (node values in post order)
Constraints:
    - tree is balanced
    - post order 
Edge Cases:
    - only root -> return root 

Plan: use post order traversal and add nodes to list and return them recursively. 

Base Case
if root == None:
    return []
    
left = survey_tree(root.left)
right = survey_tree(root.right)

return left + right + [root.val]
"""
def survey_tree(root):
    if root == None:
        return []
    
    left = survey_tree(root.left)
    right = survey_tree(root.right)

    return left + right + [root.val] 

"""
        Root
      /      \
    Node1    Node2
  /         /    \
Leaf1    Leaf2  Leaf3
"""

magnolia = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

# print(survey_tree(magnolia))



"""
Day 2
"""

from collections import deque 

# Tree Node class
class TreeNode:
    def __init__(self, value, key=None, left=None, right=None):
        self.key = key
        self.val = value
        self.left = left
        self.right = right

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
    I - binary search root (each node is (key, val))
    O - sorted array of (key, val) part 
    C - do an inorder traversal
    E - no root -> []

P
    HL: Traverse the left subtree until the node is None. Append (key,val)
    to an array. Then, traverse to the right subtree.

    Pseudocode: Initialize plants_arr = []
    current, stack= collections, []

    while stack or current:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        plants_arr.append((current.key, current.val))
        current = current.right
    
    return plants_arr

    Time: O(n squared)
    Space: O(n)
"""
def sort_plants(collection):
    plants_arr = []
    current, stack = collection, []

    while stack or current:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        plants_arr.append((current.key, current.val))
        current = current.right
    
    return plants_arr


"""
         (3, "Monstera")
        /               \
   (1, "Pothos")     (5, "Witchcraft Orchid")
        \                 /
  (2, "Spider Plant")   (4, "Hoya Motoskei")
"""

# Using build_tree() function at the top of page
values = [(3, "Monstera"), (1, "Pothos"), (5, "Witchcraft Orchid"), None, (2, "Spider Plant"), (4, "Hoya Motoskei")]
collection = build_tree(values)

# print(sort_plants(collection))


"""
Input: root (containing flower names in alphabetical order)
Output: bool (indicates whether or not hte flower name is in the tree)
Constraints: 
    - tree is in alphabetical order
Edge Cases:
    -
    
Plan: Use recursion to traverse through the tree and return a boolean based on whether or not the current node is equal to the flower's name. 

Base Case:
if inventory is None:
    return False

if inventory.val == name:
    return True
    
return find_flower(inventory.left, name) or find_flower(inventory.right, name)
"""
def find_flower(inventory, name):
    # base case
    if inventory is None:
        return False
    
    if inventory.val == name:
        return True
    
    # recurisve calls 
    return find_flower(inventory.left, name) or find_flower(inventory.right, name)

"""
         Rose
        /    \
      Lily   Tulip
     /  \       \
  Daisy  Lilac  Violet
"""

# using build_tree() function at top of page
values = ["Rose", "Lily", "Tulip", "Daisy", "Lilac", None, "Violet"]
garden = build_tree(values)

# print(find_flower(garden, "Lilac"))  
# print(find_flower(garden, "Sunflower")) 




def add_plant(collection, name):
    if collection is None:
        return TreeNode(name)
    
    if name < collection.val:
        collection.left = add_plant(collection.left, name)
    else: 
        collection.right = add_plant(collection.right, name)
    
    return collection

"""
            Money Tree
        /              \
Fiddle Leaf Fig    Snake Plant
"""

# Using build_tree() function at the top of page
values = ["Money Tree", "Fiddle Leaf Fig", "Snake Plant"]
collection = build_tree(values)

# Using print_tree() function at the top of page
print_tree(add_plant(collection, "Aloe"))

