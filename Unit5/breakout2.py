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

# Problem 1
"""
U
    I - head of linked list
    O - number (int/float), 
    C - the linked list only contains numerical values
    E - empty -> None

P
    If empty, return None. Keep track of max value. Traverse through the linked list, updating
    the maximum value (while current). Return the max value.
"""
def find_max(head):
    if not head:
        return None

    current, max_value = head, float("-inf")

    while current:
        max_value = max(max_value, current.value)
        current = current.next

    return max_value

head1 = Node(5, Node(6, Node(7, Node(8))))

# # Linked List: 5 -> 6 -> 7 -> 8
# print(find_max(head1))

# head2 = Node(5, Node(8, Node(6, Node(7))))

# # Linked List: 5 -> 8 -> 6 -> 7
# print(find_max(head2))  


# Problem 2
"""
input: head (linked list)
output: head (linked list with the tail removed)
constraints: 
edge cases: 
    - linked list of one element -> return None
    - empty list -> return None
    
Plan: 
High Level: Iterate through the linked list until we get to the last node. Set the second to last node's next pointer to None. 

current = head
prev = None

while current.next != None: 
    prev = current
    current = current.next
    
prev.next = None
return head

Time and Space Complexity:
time: O(n) 
space: O(1)
"""

def remove_tail(head):
    if head is None:
        return None
    if head.next is None:
        return None 
        
    current = head
    prev = None
    
    while current.next: 
        prev = current
        current = current.next

    prev.next = None 
    return head

head = Node("Isabelle", Node("Alfonso", Node("Cyd")))

# Linked List: Isabelle -> Alfonso -> Cyd
# print_linked_list(remove_tail(head))


# Problem 3
"""
U
    I - head of linked list
    O - head of linked list (without all duplicated elements)
    C - the output should maintain a sorted order
      - all duplicated elements must be removed
    E - all duplicated elements -> return None
      - empty -> return None
    
P
Create a dictionary to keep count of the elements and occurrences.
remove the elements that appear once in the linked list from the dictionary
Keep track of prev node and current node
If value of current node appears more than once:
    point prev.next to current.next
    decrement the value of the current node in the dictionary
    current becomes current.next
return head

{2: 2, 3: 2}
1 -> 3 -> 3 -> 4
"""
# def delete_dupes(head):
#     curr = head
#     node_dict = {}

#     while curr:
#         node_dict[curr.value] = node_dict.get(curr.value, 0) + 1
#         curr = curr.next

#     for key in node_dict:
#         if node_dict[key] == 1:
#             node_dict.pop(key)

#     prev, current = None, head

#     while current and current.next:
#         if current.value in node_dict and node_dict[current.value] > 0:
#             prev.next = current.next
#             node_dict[current.value] -= 1
#             current = current.next

#     return head

# head = Node(1, Node(2, Node(3, Node(3, Node(4, Node(5))))))

# # Linked List: 1 -> 2 -> 3 -> 3 -> 4 -> 5
# print_linked_list(delete_dupes(head))

# Andy's Problem 3
"""
I - head of linked list
O - head of linked list (without all duplicated elements)
C - the output should maintain a sorted order
    - all duplicated elements must be removed
E - all duplicated elements -> return None
    - empty -> return None

Plan: 
High Level: Create three pointers representing the previous, current, and next nodes. We know that there is a duplicate if the current node and the next node's pointers have the same value. 
temp_head = Node("head")
temp_head.next = head
prev = temp_head
curr = head
next_node = head.next

while curr and curr.next:
    if the current node is a duplicate (current node's value = next node's value):
        while next_node.value == current.value:
            next_node = next_node.next
        
        prev_node.next = next_node
        current = next_node
        next_node = current.next
    else:
        prev = current
        current = next_node
        next = current.next
    
return temp_head.next
"""

def delete_dupes(head):
    temp_head = Node("head")
    temp_head.next = head
    prev = temp_head
    curr = head
    next_node = head.next
    
    while curr and curr.next:
        if curr.value == next_node.value:
            while next_node.value == curr.value:
                next_node = next_node.next
                
            prev.next = next_node
            curr = next_node
            next_node = curr.next
        else:
            prev = curr
            curr = next_node
            next_node = curr.next
    
    return temp_head.next

head = Node(1, Node(2, Node(3, Node(3, Node(4, Node(5))))))

# Linked List: 1 -> 2 -> 3 -> 3 -> 4 -> 5
print_linked_list(delete_dupes(head))

# looks good 