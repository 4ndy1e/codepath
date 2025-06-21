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

'''
On your platform, comments on posts are displayed in the order they are received. However, for a special feature, you need to reverse the order of comments before displaying them. Given a queue of comments represented as a list of strings, reverse the order using a stack.

Understand: 
  Input: queue (represents comments as a list of strings)
  Output: list (comments in reversed order)
  Constraints / Considerations: Use a stack
  Edge Cases / Examples: 
    - Empty Queue: return empty list

Plan: 
  Initialize an empty list (for results) and an empty stack (store the comments to reverse)

  For comment in comments:
    append comment to the stack

  pop off each comment on the stack while adding each comment to the result list

  return the list of results
'''

def reverse_comments_queue(comments):
  stack = []
  results = []

  for comment in comments:
      stack.append(comment)

  while stack:
      results.append(stack.pop())

  return results

# print(reverse_comments_queue(["Great post!", "Love it!", "Thanks for sharing."]))
# print(reverse_comments_queue(["First!", "Interesting read.", "Well written."]))



