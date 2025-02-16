def reverser(string):
  reversed=[]
  for i in range(len(string)):
    reversed.append(string[len(string) - i - 1])
  return "".join(reversed)

def reverse_string_test(string):
    return string[::-1]

print(reverser("hello"))
print(reverse_string_test("hello"))
print("".join(reversed("hello")))

def merge_sorted_arrays(arr1, arr2):
  merged = []
  for i in range(len(arr1)):
    merged.append(arr1[i])
  for j in range(len(arr2)):
    merged.append(arr2[j])
  merged.sort()
  return merged

print(merge_sorted_arrays([0,3,4,31], [4,6,30]))

# Using Recursion
def reverse_string(string):
  str = list(string)
  reversed = []
  for i in range(len(str)):
    reversed.append(str.pop())
  return ''.join(reversed)

def reverse_string_recursive(string):
  if len(string) == 0:
    return ""
  else:
    return reverse_string_recursive(string[1:]) + string[0]

print(reverse_string('hello'))
print(reverse_string_recursive('hello'))