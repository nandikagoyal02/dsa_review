# Sorting Algorithms

def bubbleSort(arr):
  length = len(arr)
  for i in range(length):
    for j in range(length-i-1):
      if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
  return arr

print(bubbleSort([1, 4, 2, 8, 345, 123, 43, 32, 5643, 63, 123, 43, 2, 55, 1, 234, 92])) # O(n^2)

def selectionSort(arr):
  length = len(arr)
  for i in range(length):
    min = i
    for j in range(i + 1, length):
      if arr[j] < arr[min]:
        min = j
    arr[i], arr[min] = arr[min], arr[i]
  return arr

print(selectionSort([1, 4, 2, 8, 345, 123, 43, 32, 5643, 63, 123, 43, 2, 55, 1, 234, 92])) # O(n^2)

def insertionSort(arr):
  length = len(arr)
  for i in range(1, length):
    key = arr[i]
    j = i - 1
    while j >= 0 and key < arr[j]:
      arr[j + 1] = arr[j]
      j -= 1
    arr[j + 1] = key
  return arr

print(insertionSort([1, 4, 2, 8, 345, 123, 43, 32, 5643, 63, 123, 43, 2, 55, 1, 234, 92])) # O(n^2)

def mergeSort(arr):
  if len(arr) > 1:
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    mergeSort(left)
    mergeSort(right)
    i = j = k = 0 
    # i is left index, j is right index, k is arr (results) index
    while i < len(left) and j < len(right):
      if left[i] < right[j]:
        arr[k] = left[i]
        i += 1
      else:
        arr[k] = right[j]
        j += 1
      k += 1
    while i < len(left):
      arr[k] = left[i]
      i += 1
      k += 1
    while j < len(right):
      arr[k] = right[j]
      j += 1
      k += 1
  return arr

print(mergeSort([1, 4, 2, 8, 345, 123, 43, 32, 5643, 63, 123, 43, 2, 55, 1, 234, 92])) # O(nlogn)

def quickSort(arr):
  if len(arr) <= 1:
    return arr
  else:
    pivot = arr[0]
    left = []
    right = []
    for i in range(1, len(arr)):
      if arr[i] < pivot:
        left.append(arr[i])
      else:
        right.append(arr[i])
    return quickSort(left) + [pivot] + quickSort(right)

print(quickSort([1, 4, 2, 8, 345, 123, 43, 32, 5643, 63, 123, 43, 2, 55, 1, 234, 92])) # O(nlogn)

# Sorting Interview

#1. Sort 10 schools around your house by distance
#2. eBay sorts listings by the current Bid amount
#3. Sport scores on ESPN
#4. Massive database (can't fit all into memory) needs to sort through past year's user data
#5. Almost sorted Udemy review data needs to update and add 2 new reviews
#6. Temperature records for the past 50 years in Canada
#7. Large user name database needs to be sorted. Data is very random.
#8. You want to teach sorting for the first time

#1. Insertion Sort (fast on small sorts, easy to code, space comlexity of O(1), schools could be nearly sorted)
#2. Radix/Counting Sort  (bids btwn $1-100 probs, fixed length of integers)
#3. Quick Sort (most efficient, worried about in memory sorting, scores are probably not going to be sorted)
#4. Merge Sort (sort externally, not in memory, data is large, worried about performance)
#5. Insertion Sort (most of previous data is already sorted, add 2 new reviews)
#6. Radix/Counting Sort (if no decimals) or Quick Sort (in memory sorting if there are decimals)
#7. Merge Sort (if have enough memory) or Quick Sort (to save on memory)
#8. Bubble/Selection Sort




  