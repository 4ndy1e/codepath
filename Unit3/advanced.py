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
# from collections import deque

def process_performance_requests(requests):
  sorted_req = sorted(requests, reverse=True)

  result = []

  for req in sorted_req:
    priority, performance = req
    result.append(performance)

  return result

print(process_performance_requests([(3, 'Dance'), (5, 'Music'), (1, 'Drama')]))
print(process_performance_requests([(2, 'Poetry'), (1, 'Magic Show'), (4, 'Concert'), (3, 'Stand-up Comedy')]))
print(process_performance_requests([(1, 'Art Exhibition'), (3, 'Film Screening'), (2, 'Workshop'), (5, 'Keynote Speech'), (4, 'Panel Discussion')]))