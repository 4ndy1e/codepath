"""
As the curator of an art gallery, you are organizing a new exhibition. You must ensure the collection of art pieces are balanced to attract the right range of buyers. A balanced collection is one where the difference between the maximum and minimum value of the art pieces is exactly 1.

Given an integer array art_pieces representing the value of each art piece, write a function find_balanced_subsequence() that returns the length of the longest balanced subsequence.

A subsequence is a sequence derived from the array by deleting some or no elements without changing the order of the remaining elements.

Input: Array (art_pieces, representing the value of each art piece)
Output: Integer (longest subsequence derived from the array)
Constraints: balanced collection is one where difference between max and min val of art peices is 1
Edge Cases: 
  - list of all the same number

Plan: Coun tthe freequency of each number, then find the longest subseqeunce where the difference beteween the max and min value is exactly 1. 
  1. Initialize an empty dict and find the frequency of each number in art_pieces
  2. Initialize max_lenght = 0
  3. Iterate through each unique number in the array:
    - If 'num+1' exists, calculate the length of the balanced subsequence involving 'num' and 'num+1'
    - Update the max_lenght variable when the length is larger
"""

def find_balanced_subsequence(art_pieces):
  # Create an empty dict to map the frequency of each element, and variable to represent the max_length
  frequency = {}
  max_length = 0

  for num in art_pieces:
    frequency[num] = frequency.get(num, 0) + 1

  # Iterate through each element of the array and calculate the max length of their subsequence
  for num in art_pieces:

    # Check if num+1 exists in the dict (represents max val)
    if num+1 in frequency:
      # if exists, then the sum of the dict[num] + dict[num+1] is the length of the subsequence
      length = frequency[num] + frequency[num+1] 
      max_length = max(length, max_length)

  # return the max length
  return max_length

art_pieces1 = [1,3,2,2,5,2,3,7]
art_pieces2 = [1,2,3,4]
art_pieces3 = [1,1,1,1]

print(find_balanced_subsequence(art_pieces1))
print(find_balanced_subsequence(art_pieces2))
print(find_balanced_subsequence(art_pieces3))