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

Time: O(2^n)
Space: O(n)
"""
def fibonacci_growth(n):
    # base case 
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    return fibonacci_growth(n-1) + fibonacci_growth(n-2)

# print(fibonacci_growth(5))
# print(fibonacci_growth(8))

"""
Problem 5: 
Input: integer (n, which represents 4^n)
Output: integer (4^n)

Time: O(n)
Space: O(n)
"""

def power_of_four(n):
    if n <= 1 and n >= -1:
        return 4
    
    if n > 1:
        return 4 * power_of_four(n-1)
    
    return 1 / (power_of_four(n+1))

# print(power_of_four(2))
# print(power_of_four(-2))

"""
Problem 6
Input: list (stengths of the avengers)
Output: integer (max strength)
Contraints: use recursion

Plan: 
1) Base case: If the list `strengths` has only one element, return that element as the maximum.
2) Recursive case:
    a) Call the function recursively on the rest of the list `strengths[1:]`.
    b) Compare the first element `strengths[0]` with the maximum of the rest of the list.
    c) Return the larger value.
    
Time Complexity: O(n)
Space Complexity: O(n)
"""

def strongest_avenger(strengths):
    if len(strengths) == 1:
        return strengths[0]
    
    first = strengths[0]
    maxFromRemainingList = strongest_avenger(strengths[1:])
    
    return first if first >= maxFromRemainingList else maxFromRemainingList


print(strongest_avenger([88, 92, 95, 99, 97, 100, 94]))
print(strongest_avenger([50, 75, 85, 60, 90]))