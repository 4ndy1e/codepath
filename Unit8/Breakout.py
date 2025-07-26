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
    
print(right_vine_recursively(ivy1))
print(right_vine_recursively(ivy2))