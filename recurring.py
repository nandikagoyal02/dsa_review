def first_recurring_character(arr):
  seen = []
  for i in arr:
    if i in seen:
      return i
    else:
      seen.append(i)
  return None

print(first_recurring_character([2,5,1,2,3,5,1,2,4]))

def first_recurring_character2(arr):
  seen = {}
  for i in arr:
    if i in seen:
      return i
    else:
      seen[i] = True # adds i to seen
  return None

print(first_recurring_character2([2,5,1,2,3,5,1,2,4]))