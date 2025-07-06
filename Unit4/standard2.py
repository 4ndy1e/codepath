"""
Undertand
    Input - array of string and integer to represent max length 
    Output - array of string within max length
    Constraints - add memes that are less than or equal to max length
    Examples/edge cases - empty array -> []

Plan
    HL: Iterate through the array, check for length for string, and append
        string to result array if its less than or equal to max length

    1. Initialize the result array
    2. Iterate through the array using for loop
        - check if length of string is less than or equal to max length
        - append to result array
    3. return the result array

Time: O(n)
Space: O(n)
"""
def filter_meme_lengths(memes, max_length):
    result_arr = []

    for meme in memes:
        if len(meme) <= max_length:
            result_arr.append(meme)

    return result_arr

# memes = ["This is hilarious!", "A very long meme that goes on and on and on...", "Short and sweet", "Too long! Way too long!"]
# memes_2 = ["Just right", "This one's too long though, sadly", "Perfect length", "A bit too wordy for a meme"]
# memes_3 = ["Short", "Tiny meme", "Small but impactful", "Extremely lengthy meme that no one will read"]

# print(filter_meme_lengths(memes, 20))
# print(filter_meme_lengths(memes_2, 15))
# print(filter_meme_lengths(memes_3, 10))


"""
Understand:
  Input: list (contains dict of creator and their meme)
  Output: dict (key: creator, value: number of memes created)
  Constraints: 
  Edge Cases: 
    - Empty list: return empty dict

Plan: 
Initialize empty dict

for meme in memes:
  if creator in dict:
    incrememnt their count 
  else: 
    make their count = 1

return dict

Time and Space Complexity:
  - Time: O(n)
  - Space: O(n)
"""

def count_meme_creators(memes):
  creatorCount = {}

  for meme in memes:
    creatorCount[meme["creator"]] = creatorCount.get(meme["creator"], 0) + 1

  return creatorCount

# memes = [
#     {"creator": "Alex", "text": "Meme 1"},
#     {"creator": "Jordan", "text": "Meme 2"},
#     {"creator": "Alex", "text": "Meme 3"},
#     {"creator": "Chris", "text": "Meme 4"},
#     {"creator": "Jordan", "text": "Meme 5"}
# ]

# memes_2 = [
#     {"creator": "Sam", "text": "Meme 1"},
#     {"creator": "Sam", "text": "Meme 2"},
#     {"creator": "Sam", "text": "Meme 3"},
#     {"creator": "Taylor", "text": "Meme 4"}
# ]

# memes_3 = [
#     {"creator": "Blake", "text": "Meme 1"},
#     {"creator": "Blake", "text": "Meme 2"}
# ]

# print(count_meme_creators(memes))
# print(count_meme_creators(memes_2))
# print(count_meme_creators(memes_3))

"""
Understand
    Input: array of memes (string)
    Output: array of memes
    Constraints: a trending meme must appear more than once in a list
    Examples/ edge cases: empty -> []
                          none of the memes appear more than once -> []

    Plan
    HL: Create a dictionary with memes and their frequencies, then iterate 
    through the dictionary to add memes that appear more than once into a new array,
    and return that array

    1. Initialize empty dictionary
    2. Add memes to dictionary by iterating through array with for loop
    3. Initialize the results array
    4. Iterate through results array
        if the value of meme > 1, append to results array
    5. return the results array

    Time: O(n)
    Space: O(n)
"""
def find_trending_memes(memes):
    meme_freq = {}

    for meme in memes:
        meme_freq[meme] = meme_freq.get(meme, 0) + 1

    results_array = []

    for meme in meme_freq:
        if meme_freq[meme] > 1:
            results_array.append(meme)

    return results_array

# memes = ["Dogecoin to the moon!", "One does not simply walk into Mordor", "Dogecoin to the moon!", "Distracted boyfriend", "One does not simply walk into Mordor"]
# memes_2 = ["Surprised Pikachu", "Expanding brain", "This is fine", "Surprised Pikachu", "Surprised Pikachu"]
# memes_3 = ["Y U No?", "First world problems", "Philosoraptor", "Bad Luck Brian"]

# print(find_trending_memes(memes))
# print(find_trending_memes(memes_2))
# print(find_trending_memes(memes_3))

"""
Input: list (memes)
Output: list (reverse order of memes)
Constraints: 
Edge Cases:
  - empty list input: return empty
  - list of 1 element: return list

Plan: 
Initialize two pointers: one represents the first index and one represents the last index

while left < right: 
  swap the string values at the left and right pointers with each other

return array

Time and Space Complexity:
Time: O(n)
Space: O(1)
"""

def reverse_memes(memes):
  left, right = 0, len(memes)-1

  while left < right:
    memes[left], memes[right] = memes[right], memes[left]

    left += 1
    right -= 1

  return memes

# memes = ["Dogecoin to the moon!", "Distracted boyfriend", "One does not simply walk into Mordor"]
# memes_2 = ["Surprised Pikachu", "Expanding brain", "This is fine"]
# memes_3 = ["Y U No?", "First world problems", "Philosoraptor", "Bad Luck Brian"]

# print(reverse_memes(memes))
# print(reverse_memes(memes_2))
# print(reverse_memes(memes_3))

"""
Understand
    Input: array of arrays of memes
    Output: array of tuples of memes that frequently appear together
    Constraints:pairs need to appear more than once
    Examples/edge cases: empty list -> []
                         one list -> []

Plan:
"""


