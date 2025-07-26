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

apple_tree = TreeNode("+", TreeNode(7), TreeNode(5))
print(calculate_yield(apple_tree))