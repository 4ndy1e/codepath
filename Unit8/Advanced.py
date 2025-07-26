"""
Problem 1
input: TreeNode (root of the tree)
output: list (value of each node in the path from the root to the rightmost leaf)
constraints: 
    - only return the rightmost nodes 
edge cases:
    - empty tree: return []
    - one node: return root 
    
Plan: Create an empty list and use a loop to iterate through all the tree's right node's and adding them to
the list if it is not empty. Once the node is empty, break out of the loop and return the list. 
"""

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def right_vine(root):
    result = []
    
    while root: 
        result.append(root.val)
        root = root.right
        
    return result
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

print(right_vine(ivy1))
print(right_vine(ivy2))

"""
Problem 2
Ivy Cutting II
Same problem as above, but now recursively

Plan: 
"""

def right_vine_recursive(root):
    if root == None:
        return []
    
    return [root.val] + right_vine_recursive(root.right)

# print(right_vine_recursive(ivy1))
# print(right_vine_recursive(ivy2))

"""
Problem 3
Pruning Plans 

Input: TreeNode (represents the root of the tree)
Output: List (values of each node in postorder)
Constraints: 
  - postorder traversal
Edge Cases:
  - empty tree: return []

Plan: Recursively traverse the tree in postorder and return the first element in addition to a recursive call to the function. 

if root == None: 
  return []
  
recursive call to traverse the left tree (store left subtree values)
recursive call to traverse the right tree (store right subtree values)

return left_subtree + right_subtree + [root.val]

Time and SpaceComplexity: 
Time: O(n) - to go through all nodes in a tree
Space Complexity: O(n) - store all nodes in a list
"""

def survey_tree(root):
  if root == None:
    return []
  
  # traverse all the way to the left 
  left_subtree = survey_tree(root.left)
  right_subtree = survey_tree(root.right)
  
  return left_subtree + right_subtree + [root.val]

magnolia = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

# print(survey_tree(magnolia))

"""
Problem 4
Sum Inventory

Input: TreeNode (root)
Output: Integer (sum of all numbers in the tree)
Constraints:
  - tree is balanced
Edge Cases:
  - tree is empty -> return empty list 

Plan: Traverse the tree (in any order) and get the total sum of all node values in the tree. 

Time and Space Complexity: 
Time: O(n) - to go through each element in the tree
Space: O(h) - where h is the height of the tree due to the recursive call stack
"""

def sum_inventory(root):
  if root == None:
    return 0 
  
  left_subtree_sum = sum_inventory(root.left)
  right_subtree_sum = sum_inventory(root.right)
  
  return root.val + left_subtree_sum + right_subtree_sum

inventory = TreeNode(40, 
                    TreeNode(5, TreeNode(20)),
                            TreeNode(10, TreeNode(1), TreeNode(30)))

# print(sum_inventory(inventory))

"""
input: root (root node of a tree containing numbers and operations)
output: integer (represents the value of a node, depending on whether or not it's a leaf)
constraints: 
  - leaf nodes containing a integer value
  - non-leaf nodes contain a string of one of the four operations 
edge cases:
  - if leaf node -> return value of node 
  - if non-leaf -> return value of node from applying it's operation on the two leaf nodes 
  - non-leaf node only contains one leaf node -> perform operation on leaf node and zero 
  
Plan: Recursively traverse the list:
if the current value is a string:
  return value of the left subtree (operation) value of the right subtree
  switch(root.val):
  case '+': return func(root.left) + func(root.right)
  case '-': return func(root.left) - func(root.right)
  case '*': return func(root.left) * func(root.right)
  case '/': return func(root.left) / func(root.right)
otherwise: 
  return the number
  
Time and Space Complexity: 
time: O(n) - traversing through each node 
space: O(h)or O(logn) when balanced - recursive calls on the call stack
"""

def calculate_yield(root):
  if isinstance(root.val, str):
    # check the operation type, then return the proper operation type
    match root.val:
      case "+": return calculate_yield(root.left) + calculate_yield(root.right)
      case "-": return calculate_yield(root.left) - calculate_yield(root.right)
      case "*": return calculate_yield(root.left) * calculate_yield(root.right)
      case "/": return calculate_yield(root.left) / calculate_yield(root.right)

  return root.val

"""
      +
     / \ 
    /   \
   -     *
  / \   / \
 4   2 10  2
"""

# root = TreeNode("+")
# root.left = TreeNode("-")
# root.right = TreeNode("*")
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(2)
# root.right.left = TreeNode(10)
# root.right.right = TreeNode(2)

# print(calculate_yield(root))


"""
Input: root 
Output: list (all leaf nodes of the tree)

Plan: Use recursion to traverse through the tree until the end. If the current node has no children, add it to the list. 

Base Cases:
if root is None:
  return []
  
if root.left is None and root.right is None:
  add to the list 
  
left = call recursive function on left subtree
right = call recursive function on right subtree

return left + right

Time and Space complexity:
time: O(n) - to go through each node and perform the checks
space: O(h) - recursive calls stored on the call stack
"""

def get_most_specific(root):
  # base case
  if root == None:
    return []
  
  if root.left == None and root.right == None:
    return [root.val]
  
  left = get_most_specific(root.left)
  right = get_most_specific(root.right)
  
  return left + right

"""
           Plantae
          /       \
         /         \
        /           \ 
Non-flowering     Flowering
   /      \       /        \
Mosses   Ferns Gymnosperms Angiosperms
                             /     \
                        Monocots  Dicots
"""
plant_taxonomy = TreeNode("Plantae", 
                          TreeNode("Non-flowering", TreeNode("Mosses"), TreeNode("Ferns")),
                                  TreeNode("Flowering", TreeNode("Gymnosperms"), 
                                          TreeNode("Angiosperms", TreeNode("Monocots"), TreeNode("Dicots"))))

print(get_most_specific(plant_taxonomy))

