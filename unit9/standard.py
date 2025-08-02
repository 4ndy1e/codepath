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
Problem 1:
Input: two roots (order1 and order2)
Output: root (root of the merged tree)
Constraints:    
    - two nodes overlap: take the sum
    - one node: take the value of the not None node

Plan:

Base Case
If one of the orders is empty return the other one 
    
Recursive merge:
create a new node representing the current sum of the two order node values
recursively call the left and right subtrees and add their values 

return the merged node

Psuedocode:
if not order1:
    return order2
if not order2: 
    return order1
    
newnode = TreeNode(order1.val + order2.val)

newNode.left = recursiveCall(order1.left, order2.left)
newNode.right = recursivecall(order1.right, order2.right)

return newNode

Time and Space Complexity:
Time: O(n) - going through each node in the trees
Space: O(n) - for the call stack recursive calls and creating a new tree representing merged
"""

def merge_orders(order1, order2):
    # base case
    if not order1:
        return order2
    if not order2:
        return order1
    
    # merged node with the subtrees being recursively calculated
    mergedNode = TreeNode(order1.val + order2.val)
    
    mergedNode.left = merge_orders(order1.left, order2.left)
    mergedNode.right = merge_orders(order2.right, order2.right)
    
    return mergedNode

"""
     1             2         
    /  \         /   \       
   3    2       1     3   
 /               \      \   
5                 4      7   
"""
# Using build_tree() function included at top of page
cookies1 = [1, 3, 2, 5]
cookies2 = [2, 1, 3, None, 4, None, 7]
order1 = build_tree(cookies1)
order2 = build_tree(cookies2)

# Using print_tree() function included at top of page
# print_tree(merge_orders(order1, order2))

"""
Problem 2
Input: root 
Output: print list of flavors (vals) in level order from left to right
Constraints:
    - level order from left to right

Plan: Use a BFS to explore the nodes level by level from left to right

If tree is empty:
    return tree
    
instantiate a queue to store our nodes in the order to be visited 
instantiate a list for nodes that have been visited 

add root to the queue

while queue:
    pop off the queue 
    add the node to visited 
    
    add the popped node's left child to the queue
    add the popped node's right child to the queue
    
return list of nodes that have been visited

Time and Space Complexity:
Time - O(n): go through each element level by level
Space - O(n): store the visited nodes to return back
"""

class Puff():
     def __init__(self, flavor, left=None, right=None):
        self.val = flavor
        self.left = left
        self.right = right

def print_design(root):
    if not root:
        return root
    
    queue = deque()
    visited = []
    
    queue.append(root)
    
    while queue:
        currentNode = queue.popleft()
        visited.append(currentNode.val)
        
        if currentNode.left:
            queue.append(currentNode.left)
        if currentNode.right:
            queue.append(currentNode.right)
            
    print(visited)

"""
            Vanilla
           /       \
      Chocolate   Strawberry
      /     \
  Vanilla   Matcha  
"""
# croquembouche = Puff("Vanilla", 
#                     Puff("Chocolate", Puff("Vanilla"), Puff("Matcha")), 
#                     Puff("Strawberry"))

# print_design(croquembouche)

"""
Input: root
Output: integer (maximum number of tiers in your cake)
Edge Cases:
    - empty root -> return 0

Plan: Use a DFS to find the longest path in the tree and explore each nodes left and right subtrees until none

Base Case:
if root is None:
    return 0
    
recursively calculate the depth of the left subtree
recursively calculate the depth of the right subtree

return the greater of the two depths plus one for the current node level

Time and Space Complexity:
Time: O(N) - go through each element in the tree to determine the longest path
Space: O(h) - recursive calls on the call stack
"""

def max_tiers_dfs(root):
    # base case
    if not root:
        return 0
    
    # search
    left = max_tiers_dfs(root.left)
    right = max_tiers_dfs(root.right)
    
    # return values
    return max(left, right) + 1

"""
        Chocolate
        /        \
    Vanilla    Strawberry
                /     \
         Chocolate    Coffee
"""
# Using build_tree() function included at top of page
# cake_sections = ["Chocolate", "Vanilla", "Strawberry", None, None, "Chocolate", "Coffee"]
# cake = build_tree(cake_sections)

# print(max_tiers_dfs(cake))

"""
Maximum Depth of Binary Tree
Problem 4: recreate the same problem as above using bfs instead

Time and Space Complexity:
Time: O(n) - traversing through each node in the tree 
Space: O(n) - queue storing nodes for each node when traversing through levels
"""

def max_tiers_bfs(root):
    if not root:
        return 0
    
    queue = deque()
    queue.append(root)
    
    tiers = 0
    
    while queue:
        currentLevelLen = len(queue)
        
        for i in range(currentLevelLen):
            currentNode = queue.popleft()
            
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(queue)
            
            tiers += 1
            
    return tiers

# cake_sections = ["Chocolate", "Vanilla", "Strawberry", None, None, "Chocolate", "Coffee"]
# cake = build_tree(cake_sections)

# print(max_tiers_dfs(cake))

"""
Path Sum
Input: root (represents the inventory)
Output: boolean (represents if an order can be fulfilled)
Constraints:  
    - root-to-leaf path such that adding up all values alonmg the path = order_size
Edge Case:
    - empty root -> false
    - one node -> return true if it is a leaf node and equal to order_size
    
Plan: Use a DFS to go down each branch of the tree and determine whether or not the current sum when traversing
though the branch is equal to the order_size or not. If it is, return True, if not, it will go all the way to
the end of the branch and return False. 

Base Case:
if root is None:
    return False
    
if root.val == order_size and not root.left and not root.right:
    return True
    
subtract the current root value from the order size

recursive call to the left subtree until base case is satisfied
recursive call to the right subtree until basecase is satisfied

return left or right 

Time and Space Complexity:
Time: O(n) - go through each node using a dfs traversal
Space: O(n) - recursive calls to the function on the call stack
"""

def can_fulfill_order(root, order_size):
    if not root:
        return False
    
    if root.val == order_size and not root.left and not root.right:
        return True
    
    newOrderSize = order_size - root.val
    
    return can_fulfill_order(root.left, newOrderSize) or can_fulfill_order(root.right, newOrderSize)

quantities = [5,4,8,11,None,13,4,7,2,None,None,None,1]
baked_goods = build_tree(quantities)

print(can_fulfill_order(baked_goods, 22))
print(can_fulfill_order(baked_goods, 2))
