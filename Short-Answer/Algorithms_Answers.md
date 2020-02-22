#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) - incrementing a by n^2, n number of times, is bounded by n^3. So the loop should execute on order of n times


b) O(n^2) for loop = O(n) nested while loop = O(n/2) ≈ O(n) multiply them because they're nested O(n) * O(n) = O(n^2)


c) linear O(n) - recursion function calling one function per call -- it's a linear function of n

## Exercise II
I would use a binary search. 

1- I would start at the center floor of the building and test out whether the egg broke on that floor

    middle = high + low // 2

  1a- if the egg did break I would know that it would also break on all the floor above me so I can eliminate those floors

2 - I would then move to the floor half way between where I am now and the bottom floor and toss an egg off that floor
  
  2a- if the egg did not break, I can eliminate the floors below me and move to the mid point of my first drop and my previous one and continue until I have exhausted all the drops in this pattern


example: 
```python
def dont_break_me(arr, target):

  if len(arr) == 0:
    return -1 # array empty
    
  low = 0 # start
  high = len(arr)-1 # end
  
  while(low <= high):
    mid = (low + high) // 2
    if arr[mid] == target:
      return mid
    elif target < arr[mid]:
      high = mid - 1
    else: 
      low = mid + 1
  
  return -1 # not found



