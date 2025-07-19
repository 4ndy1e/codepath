"""
U   
    I - list of strings
    O - int (length of the list)
    C - do not use len() for the iterative implementation
    E - [] -> 0

P   
    Iterative HL: Return 0 if list == []. Initialize a length counter and pointer. 
    While list[pointer], increment length and increment pointer. Return length.

    Recursive HL: Initialize a length counter and pointer. If not list[pointer], return 0.
    Else, return 1 + list[pointer + 1:] 
"""

def count_suits_iterative(suits):
    if suits == []:
        return 0

    length = 0

    for suit in suits:
        length += 1

    return length

def count_suits_recursive(suits):
    pointer = 0

    if suits == []:
        return 0
    
    return 1 + count_suits_recursive(suits[pointer + 1:])

# print(count_suits_iterative(["Mark I", "Mark II", "Mark III"]))
# print(count_suits_recursive(["Mark I", "Mark I", "Mark III", "Mark IV"]))


"""
Problem 2
input: array (stones)
output: integer (total power)
contraints: use a recursive approach 
edge case:
    - empty: return 0
    
Plan
High Level: Use recursion to go through each element with a base case of stone being empty ([]) (return 0).

Time Complexity:
Time: O(n)
Space: O(n)
"""
def sum_stones(stones):
    # base case
    if stones == []:
        return 0
    
    return stones[0] + sum_stones(stones[1:])

print(sum_stones([12, 8, 22, 16, 10]))

print(sum_stones([5, 10, 15, 20, 25, 30]))

"""
U   
    I - list of strings (suits)
    O - int (total number of unique suits)
    C - none
    E - [] -> 0
    

P 
    Iterative: Initialize a hash map to store all suits and occurrences. 
    Count all the items in the hash map once using a unique_suits counter. 
    Return unique_suits.
    Time: O(n)
    Space: O(n)

    Recursive: If list is empty, return 0. If first = suits[0] in suits[1:], 
    return recursive call on rest of list. Else, add 1 + recursive call on rest of list
    Time: O(n * n)
    Space: O(n) on call stack
"""
def count_suits_iterative(suits):
    hash_map = {}

    for suit in suits:
        hash_map[suit] = hash_map.get(suit, 0) + 1

    unique_suits = 0
    for suit in hash_map:
        unique_suits += 1

    return unique_suits

def count_suits_recursive(suits):
    if suits == []:
        return 0

    first = suits[0]

    if first in suits[1:]:
        return count_suits_recursive(suits[1:])

    return 1 + count_suits_recursive(suits[1:])


# print(count_suits_iterative(["Mark I", "Mark II", "Mark III"]))
# print(count_suits_recursive(["Mark I", "Mark I", "Mark III"]))

"""
Problem 4
Input: integer (integer n - months)
Output: integer (height)

Time: O(n)
Space: O(n)
"""
def fibonacci_growth(n):
    # base case 
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    return fibonacci_growth(n-1) + fibonacci_growth(n-2)

print(fibonacci_growth(5))
print(fibonacci_growth(8))