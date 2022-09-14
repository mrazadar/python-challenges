# Given a binary array nums, return the maximum number of consecutive 1's in the array.

# Example 1:

# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
# Example 2:

# Input: nums = [1,0,1,1,0,1]
# Output: 2

# Constraints:

# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.

class Solution:
    def findMaxConsecutiveOnes(self, nums):
        maxOnes = 0
        tempMax = 0
        for i in nums:
            if i == 1:
                tempMax += 1
                if maxOnes < tempMax:
                    maxOnes += 1
            else:
                tempMax = 0
        return maxOnes

s = Solution()

print(s.findMaxConsecutiveOnes([1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1]))
print(s.findMaxConsecutiveOnes([1, 0, 1, 1, 0, 0, 0, 1]))