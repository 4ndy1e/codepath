"""
You are managing a social media platform and need to ensure that posts are properly formatted. Each post must have balanced and correctly nested tags, such as () for mentions, [] for hashtags, and {} for links. You are given a string representing a post's content, and your task is to determine if the tags in the post are correctly formatted.

Input: String 
Output: Bool
Constraints: Each opening tag has a corresponding closing tag
Edge Cases:
  - Empty String: Return True

Plan: 
1. Create a dict to identify opening and closing tags 
2. Initialize a dict to keep track of opening tags 
2. Loop through each character
  - If it is a opening tag append it to the stack
  - Otherwise, it is a closing tag   
    - If top of stack opening tag matches closing tag, pop
    - Otherwise return false
"""

def is_valid_post_format(posts):
  tagsDict = {
    "}" : "{",
    ")" : "(",
    "]" : "["
  }

  stack = []

  for char in posts:
    # if opening tag, add to stack
    if char in tagsDict.values():
      stack.append(char)
    # otherwise check top of stack's opening tag
    else:
      # if top of stack matches its closing tag, pop and continue, otherwise return false
      if len(stack) != 0 and stack[-1] == tagsDict[char]:
        stack.pop()
      else:
        return False
      
  return True

# print(is_valid_post_format("()"))
# print(is_valid_post_format("()[]{}")) 
# print(is_valid_post_format("(]"))
