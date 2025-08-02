from collections import deque 

# Tree Node class
class TreeNode:
    def __init__(self, value, key=None, left=None, right=None):
        self.key = key
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
guest1 = TreeNode("John Doe", TreeNode("6 ft"), TreeNode("Brown Eyes"))
guest2 = TreeNode("John Doe", TreeNode("6 ft"), TreeNode("Brown Eyes"))

"""
     John Doe         John Doe
     /                       \
   6 ft                     6 ft
"""
guest3 = TreeNode("John Doe", TreeNode("6 ft"))
guest4 = TreeNode("John Doe", None, TreeNode("6 ft"))

print(is_clone(guest1, guest2))
print(is_clone(guest3, guest4))