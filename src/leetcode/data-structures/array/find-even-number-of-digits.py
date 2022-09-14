# Find Numbers with Even Number of Digits
# Given an array nums of integers, return how many of them contain an even number of digits.

 

# Example 1:

# Input: nums = [12,345,2,6,7896]
# Output: 2
# Explanation: 
# 12 contains 2 digits (even number of digits). 
# 345 contains 3 digits (odd number of digits). 
# 2 contains 1 digit (odd number of digits). 
# 6 contains 1 digit (odd number of digits). 
# 7896 contains 4 digits (even number of digits). 
# Therefore only 12 and 7896 contain an even number of digits.
# Example 2:

# Input: nums = [555,901,482,1771]
# Output: 1 
# Explanation: 
# Only 1771 contains an even number of digits.
 

# Constraints:

# 1 <= nums.length <= 500
# 1 <= nums[i] <= 105

class Solution:
  #solution1
  def findNumbers1(self, nums):
    count = 0
    for n in nums:
        if not (len(str(n)) % 2):
            count += 1
    # time complexity = O(n*n) # str conversion time complexity is * n 
    # space complexity = O(1)
    return count
  
  #solution2
  def findNumbers2(self, nums):
    count = 0
    for n in nums:
      if n >= 10:
        temp = n
        total_digits = 1
        while temp >= 10:
          temp = temp / 10
          total_digits += 1          
        # even or odd          
        if not (total_digits % 2):
          count += 1
    # time complexity = O(n(logn)) = O(nlogn)
    # space complexity = O(1)
    return count

s = Solution()
print(s.findNumbers2([12, 345, 2, 6, 7896])) # 2


