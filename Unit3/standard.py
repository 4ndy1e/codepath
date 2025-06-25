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

"""
Understand:  
  Input: list (strings: schedule, cancel, or reschedule)
  Output: List (ID x on the stage)
  Constraints: 
  Edge CaseS: 
    - Empty list: return []

  Plan: 
  Initialize 2 stacks (one represents the scheudle and one represents canceled)

  for string in changes: 
    if it is schedule:
      add to the schedule stack
    otherwise, if it cancel:
      pop off the scheudle stack, add to canceled stack
    otherwise, rechsdule:
      pop off the cancled stack, add back to schedule 

  return schedule stack
"""

def manage_stage_changes(changes):
  schedule = []
  canceled = []

  for change in changes:
    if "Schedule" in change:
      schedule.append(change[-1])
    elif change == "Cancel":
      canceled.append(schedule.pop())
    else:
      schedule.append(canceled.pop())

  return schedule

# print(manage_stage_changes(["Schedule A", "Schedule B", "Cancel", "Schedule C", "Reschedule", "Schedule D"]))  
# print(manage_stage_changes(["Schedule A", "Cancel", "Schedule B", "Cancel", "Reschedule", "Cancel"])) 
# print(manage_stage_changes(["Schedule X", "Schedule Y", "Cancel", "Cancel", "Schedule Z"])) 

"""
1. Sort the `requests` list in descending order based on the priority (first element of each tuple).
2. Initialize a queue and load the sorted requests into it.
3. Initialize an empty list `result` to store the order of performances.
4. Dequeue each request from the queue and append the performance name to the `result` list.
5. Return the `result` list.
"""
from collections import deque

def process_performance_requests(requests):
  sorted_queue = deque(sorted(requests, reverse=True))
  result = []

  while sorted_queue:
    priority, performance = sorted_queue.popleft()
    result.append(performance)

  return result


# print(process_performance_requests([(3, 'Dance'), (5, 'Music'), (1, 'Drama')]))
# print(process_performance_requests([(2, 'Poetry'), (1, 'Magic Show'), (4, 'Concert'), (3, 'Stand-up Comedy')]))
# print(process_performance_requests([(1, 'Art Exhibition'), (3, 'Film Screening'), (2, 'Workshop'), (5, 'Keynote Speech'), (4, 'Panel Discussion')]))

"""
Input: List (numbers)
Output: integer (total of all points)
Constraints: Use stack
Edge Cases: 
  - Empty list: return 0

Plan: 
Initialize a empty stack to keep track of the points
Create a variable to keep track of the total

for point in points:
  add each point to the stack

while stack is not empty:
  pop value on the stack and add it to the total

return total
"""

def collect_festival_points(points):
  stack = []
  total = 0

  for point in points:
    stack.append(point)

  while stack:
    total += stack.pop()

  return total

# print(collect_festival_points([5, 8, 3, 10])) 
# print(collect_festival_points([2, 7, 4, 6])) 
# print(collect_festival_points([1, 5, 9, 2, 8])) 

"""
Input: 2 strings 
Output: string (merged result of the 2 strings)
Constraints: append remaining substring if one string is longer
Edge Cases:
  - One empty string: return other string
  - Two Empty strings: return empty string

Plan:
High level: Use two pointers to iterate through both strings and alternatively add each char to a result string. 

Initialize an empty string to store the result 
Initialize two pointers at the beginning of each string

while both pointers are within the length of their strings:
  result += schedule1[firstPointer]
  move first pointer (incrementing)

  result += schedule2[secondPointer]
  move second pointer (incrementing)

while firstPointer < len(schedule1):
  result += schedule1[firstPointer]
  firstPointer += 1

while secondPointer < len(schedule2):
  result += schedule2[secondPointer]
  secondPointer += 1

return result 
"""

def merge_schedules(schedule1, schedule2):
  result = ""
  pointer1, pointer2 = 0, 0

  while pointer1 < len(schedule1) and pointer2 < len(schedule2):
    result += schedule1[pointer1]
    pointer1 += 1

    result += schedule2[pointer2]
    pointer2 += 1

  while pointer1 < len(schedule1):
    result += schedule1[pointer1]
    pointer1 += 1

  while pointer2 < len(schedule2):
    result += schedule2[pointer2]
    pointer2 += 1

  return result 

# print(merge_schedules("abc", "pqr")) 
# print(merge_schedules("ab", "pqrs")) 
# print(merge_schedules("abcd", "pq")) 

"""
At a cultural festival, you have a schedule of events where each event has a unique popularity score. The schedule is represented by two distinct 0-indexed integer arrays schedule1 and schedule2, where schedule1 is a subset of schedule2.

For each event in schedule1, find its position in schedule2 and determine the next event in schedule2 with a higher popularity score. If there is no such event, then the answer for that event is -1.

Return an array ans of length schedule1.length such that ans[i] is the next greater event's popularity score as described above.

Input: two lists (schedule1 and schedule2)
Output: list (of length schedule1)
Constraints: 
  - schedule1 is a subset of schedule2
  - output is of length schedule1
Edge Cases:
  - two empty lists: return empty list 

Plan: 
Initialize empty dict to store element and indexes of schedule2
Initialize list to keep track of result

for score in schedule2:
  dict[score] = index

for score in schedule1:
  startingIndex = dict[score]

  for i in range(startingIndex, len(schedule2)):
    if schedule2[i] > score:
      result.append(schedule[i])
      break

return result
"""

def next_greater_event(schedule1, schedule2):
  dict = {}

  for i in range(len(schedule2)):
    dict[schedule2[i]] = i

  result = []

  for score in schedule1:
    startingIndex = dict[score]
    nextGreaterScore = -1

    for i in range(startingIndex, len(schedule2)):
      if schedule2[i] > score:
        nextGreaterScore = schedule2[i]
        break
    
    result.append(nextGreaterScore)

  return result

# print(next_greater_event([4, 1, 2], [1, 3, 4, 2])) 
# print(next_greater_event([2, 4], [1, 2, 3, 4])) 

"""
You are organizing a cultural festival and have a list of performances represented by an integer array performances. Each performance is classified as either an even type (e.g., dance, music) or an odd type (e.g., drama, poetry).

Your task is to rearrange the performances so that all the even-type performances appear at the beginning of the array, followed by all the odd-type performances.

Return any array that satisfies this condition.

Input: list (performances)
Output: list (ordered where evens are at the beginning of the array and odds are at the end)
Constraints: evens at the beginning and odds at the end
Edge Case:
  - list of 1 element: return list of that element
  - empty list: return empty list

Plan:
Initialize a queue to store the odd and even types 

for num in performances:
  if number is even:
    append to left of queue
  else:
    append to right of queue

return the queue as a list
""" 

def sort_performances_by_type(performances):
  queue = deque()

  for num in performances:
    if num % 2 == 0:
      queue.appendleft(num)
    else:
      queue.append(num)

  return list(queue)

print(sort_performances_by_type([3, 1, 2, 4]))  
print(sort_performances_by_type([0]))  