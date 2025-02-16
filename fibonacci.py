def fibonacci_iterative(n):
  if n < 2:
    return n
  a = 0
  b = 1
  for i in range(2, n + 1):
    c = a + b
    a = b
    b = c
  return b

def fibonacci_iterative_2(n):
    arr = [0, 1]
    for i in range(2, n + 1):
        arr.append(arr[i - 2] + arr[i - 1])
    return arr[n]

# Using Recursion
def fibonacci_recursive(n):
  if n <= 0:
      return 0
  elif n == 1:
      return 1
  return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def fibonacci_memoized(n, memo={}):
  if n in memo:
      return memo[n]
  if n <= 0:
      return 0
  elif n == 1:
      return 1
  memo[n] = fibonacci_memoized(n - 1, memo) + fibonacci_memoized(n - 2, memo)
  return memo[n]

print(fibonacci_iterative(0))  # Expected: 0
print(fibonacci_iterative(1))  # Expected: 1
print(fibonacci_iterative_2(5))  # Expected: 5 --- O(n)
print(fibonacci_iterative_2(10)) # Expected: 55
print(fibonacci_recursive(5))  # Expected: 5 --- O(2^n)
print(fibonacci_recursive(10)) # Expected: 55
print(fibonacci_memoized(50))  # Expected: 12586269025 (Fast due to memoization)
