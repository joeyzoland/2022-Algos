"""Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.



Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true


Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #Initialize seen set
        #Iterate through array and, at every number
            #If it's in seen set, return True
            #Otherwise, add to set
        #If you make it all through, return False
        seenSet = set()
        for num in nums:
            if num in seenSet:
                return True
            seenSet.add(num)
        return False

solution = Solution()
input = [1,1,1,3,3,4,3,2,4,2]
print(solution.containsDuplicate(input))
