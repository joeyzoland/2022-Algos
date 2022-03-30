"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than [n / 2] times. You may assume that the majority element always exists in the array.



Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2


Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Determine number of elements needed for majority element
        #Create frequency dictionary, noting frequencies of each element
        #Iterate through array
        #On each element seen, add to dictionary
        #If that element is greater than majority frequency, return it
        majorityFreq = len(nums) / 2
        freqDict = {}
        for num in nums:
            if num not in freqDict:
                freqDict[num] = 1
            else:
                freqDict[num] += 1
            if freqDict[num] > majorityFreq:
                return num

solution = Solution()
input = [2,2,1,1,1,2,2]
print(solution.majorityElement(input))
