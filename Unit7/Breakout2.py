import math

"""
U
    I - integer list and integer ID
    O - boolean
    C - solution must have O(log n) time complexity
      - integer list is sorted in ascending order
    E - [] -> False
      - no integer ID in the list -> False

P
    HL: Return False if inventory == []. Initialize left = 0
    and right = len(inventory - 1). Compute mid = (left + right) // 2
    While left <= right, if inventory[mid] == part_id, return True. If
    midpoint < part_id, update left to mid + 1. Otherwise, update right to 
    mid - 1. Rdturn False at the end.

Time: O(log n)
Space: O(1)
"""
def check_stock(inventory, part_id):
    if inventory == []:
        return False

    left, right = 0, len(inventory) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if inventory[mid] == part_id:
            return True
        elif inventory[mid] < part_id:
            left = mid + 1
        else:
            right = mid - 1
    
    return False

# print(check_stock([1, 2, 5, 12, 20], 20))
# print(check_stock([1, 2, 5, 12, 20], 100))


"""
Problem 2
input: 
    inventory: list of inventory id's 
    part_id: id of the part that we are looking for 
output:
    boolean: whether or not the part exists in the inventory
constraints: 
    - inventory ids are sprted om ascending order 
    - log n time complexity 
    - use recursion
edge cases:
    - empty list -> return false 
    - not found -> return false 
    
Plan: Use binary search recursion to search through the inventory, partitioning the list in half whenever the 
inventory id is not found. Search the left or right partition depending on the id's value (whether it is greater than or less than the middle value).

Time and Space Complexity:
Time: O(log n)
Space: O(log n)
"""
def check_stock_recursively(inventory, part_id):
    if not inventory: 
        return False
    
    def search_stock(left, right, target):
        # base case 
        if left > right:
            return False
        
        mid = (left + right) // 2
        
        if inventory[mid] == target:
            return True
        elif inventory[mid] > target: 
            return search_stock(left, mid-1, target)
        return search_stock(mid+1, right, target)
    
    return search_stock(0, len(inventory) - 1, part_id)

# print(check_stock_recursively([1, 2, 5, 20, 12], 20))
# print(check_stock_recursively([1, 2, 5, 20, 12], 100))

"""
U
    I - integer array and integer target
    O - integer tuple (with the first and last indices for the target)
    C - solution must have O(log n) time complexity
      - integers in array are sorted
    E - [] -> (-1, -1)
      - the target is not in array -> (-1, -1)

P
    HL: Return (-1, -1) if transmissions == []. Initialize left = 0 and right = len(transmissions) - 1.
    Initialize first_occurrence and last_occurrence to math.inf. 
    Compute mid = (left + right) // 2. While left <= right, if midpoint == target, first_occurrence will be equal to mid, and break
    from the loop. If midpoint is greater, update right to mid - 1. else, update left to mid + 1. if first_occurrence > len(transmissions),
    return (-1, -1). For i in range(first_occurrence, len(transmissions)), if i is equal == target, update last_occurrence.
    Return (first, last).
"""
def find_frequency_positions(transmissions, target_code):
    if not transmissions:
        return (-1, -1)

    left, right = 0, len(transmissions) - 1
    first_occurrence = last_occurrence = math.inf

    while left <= right:
        mid = (left + right) // 2
        if transmissions[mid] == target_code:
            first_occurrence = mid
            break
        elif transmissions[mid] > target_code:
            right = mid - 1
        else:
            left = mid + 1
    
    if first_occurrence > len(transmissions):
        return (-1, -1)

    i = first_occurrence
    while transmissions[i] == target_code:
        first_occurrence = i
        i -= 1

    last_occurrence = first_occurrence
    for i in range(first_occurrence, len(transmissions)):
        if transmissions[i] != target_code:
            break
        last_occurrence = i

    return (first_occurrence, last_occurrence)

print(find_frequency_positions([5,7,7,8,8,10], 8))
print(find_frequency_positions([5,7,7,8,8,10], 6))
print(find_frequency_positions([], 0))

"""
input: 
    - list: characters in lexicogrpahic order 
    - char: target character we are looking for 
output: 
    - char: smallest character that is lexicographically larger than the target
constraints: 
    - character has to be alphabetically greater than the target
    - at least two different characters in the list
edge cases:
    - no lixcographically greater characters than the target -> return letter[0]

Match: Divide and Conquer - Binary Search Pattern

Plan: Use a binary search to find the target and adjust the mid point point depending on the alphabetical value of the midpoint character to the target. 
    - if the midpoint character > target: adjust midpoint to left partition
    - if the midpoint character <= target: adjust midpoint to the right partition
"""

def next_greatest_letter(letters, target):
    left, right = 0, len(letters) - 1
    mid = (left + right) // 2
    
    while left <= right:
        mid = (left + right) // 2
        
        if letters[mid] <= target:
            # search the right partition
            left = mid + 1
        else:
            # search the left partition
            right = mid - 1
            
    # If low is out of bounds, it means we didn't find a larger element, so wrap around
    return letters[left % len(letters)]

letters = ['a', 'a', 'b', 'c', 'c', 'c', 'e', 'h', 'w']

print(next_greatest_letter(letters, 'a'))
print(next_greatest_letter(letters, 'd'))
print(next_greatest_letter(letters, 'y'))
