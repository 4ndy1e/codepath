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
Ivy Cutting II
Same problem as above, but now recursively

Plan: 
"""

def right_vine_recursive(root):
    if root == None:
        return []
    
    return [root.val] + right_vine_recursive(root.right)

print(right_vine_recursive(ivy1))
print(right_vine_recursive(ivy2))