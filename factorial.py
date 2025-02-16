def factorial_iterative(value):
  answer = 1
  for i in range(1, value + 1):
      answer *= i
  return answer

# Using Recursion
def factorial_recursive(value):
  if value == 2:
    return 2
  return value*factorial_recursive(value-1)

print(factorial_iterative(5)) # O(n)
print(factorial_recursive(5)) # O(n)