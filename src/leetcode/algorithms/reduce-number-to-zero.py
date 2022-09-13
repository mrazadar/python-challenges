# 1342. Number of Steps to Reduce a Number to Zero

# Given an integer num, return the number of steps to reduce it to zero.

# In one step, if the current number is even, you have to divide it by 2, 
# otherwise, you have to subtract 1 from it.

# Example 1:

# Input: num = 14
# Output: 6
# Explanation: 
# Step 1) 14 is even; divide by 2 and obtain 7. 
# Step 2) 7 is odd; subtract 1 and obtain 6.
# Step 3) 6 is even; divide by 2 and obtain 3. 
# Step 4) 3 is odd; subtract 1 and obtain 2. 
# Step 5) 2 is even; divide by 2 and obtain 1. 
# Step 6) 1 is odd; subtract 1 and obtain 0.

def reduce_to_zero(num):
  steps = 0
  n = num
  while n != 0:
    if n % 2 == 1:
      n = n-1
    else:
      n = n/2
    steps += 1
  return steps

#bitwise binary operation
def binary_reduce_to_zero(num):
  steps = 0
  while num > 0:
    if num & 1 == 1: #bitmask to check if number is odd or even
      num -= 1
    else: 
      num = num >> 1      
    steps += 1
  return steps


# Time complexity of both solution O(logn)
# Space comlexity of both solution O(1)
print(binary_reduce_to_zero(14)) #6
print(reduce_to_zero(14)) #6
print(reduce_to_zero(8)) #4
print(reduce_to_zero(123)) #12
