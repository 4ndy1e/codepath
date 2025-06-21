# hello wworld

def is_valid_post_format(posts):
    stack = []
    hmap = {")":"(", "]":"[","}":"{"}

    for char in posts:
        if char not in hmap:
            stack.append(char) 
        else:
            if stack:
                n = stack.pop()
                if not hmap[char] == n:
                    return False 
    return True if len(stack) == 0 else False
                
# U ...check if the parens are valid, thus opened is followed with close for a particular
#      type of parenthesis
#   i - string of parens    o - boolean    c -- open must match with close  e- empty string True
# P ..
#    High level: use stacks for this problem
#                use dict to track the correct pair for a particular parenthesis {):(}
#                if we meet an open parens we add to the stack
#                if we meet a close parens, if the stack is not empty : we pop from the stack and check
#                if key ( current close parens) h as
#                correct open parens as the value
#                if the stack is empty we return True, otherwise False
#                ()))
# Implementation


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



