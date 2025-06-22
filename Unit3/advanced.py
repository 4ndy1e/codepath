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

