"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.



Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23


Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #NOTE: This was first draft of pseudo-code.  Keeping here as a reference but changed greatly as time went on.

        #It always makes sense to start and end on a positive number or the widest berth when there are two contiguous positive numbers
        #Keep track of the past combination of numbers at previous
        #Keep track of the most recent positive number set
        #If the previous + present is greater than present
            #Sum everything and overwrite max with it
            #Overwrite previous with this as well
        #Otherwise, overwrite previous with current

        #Initialize max at the first number of nums
        #Initialize previous as 0
        #Iterate through the array
            #If the current number is bigger than max, overwrite (for all negatives)
            #If the current number is positive
                #Sum all contiguous positive numbers and write that as current
                #Afterwards, if this number is greater than max, overwrite max
                #If previous + present is greater than max
                    #Overwrite previous and max with this sum
                #Otherwise
                    #Set previous to current
        #Return max

        maximum = nums[0]
        previous = 0 #Holds everything before next positive contiguous section
        current = 0 #Holds positive contiguous section
        lastPositive = False
        for i in range(len(nums)):
            if nums[i] > 0:
                current += nums[i]
                lastPositive = True
            elif nums[i] <= 0:
                #Catches edge case where the greatest number might be negative
                maximum = max(nums[i], maximum)
                if lastPositive == True:
                    if previous >= 0:
                        previous += current
                        if maximum < previous:
                            maximum = previous
                    elif previous < 0:
                        previous = current
                        #Handles edge case where you end with a 0 and maximum still needs to be updated, as you can't include this in the last check below for current as 0 is initialization value and it would wrongly give you 0 instead of a negative number
                        maximum = max(maximum, current)
                    current = 0
                previous += nums[i]
                lastPositive = False
        #Checks for maximum one last time if the last number wasn't negative and performed all of that necessary code
        if current > 0:
            maximum = max(maximum, current, (current + previous))
        return maximum

solution = Solution()
#input = [-2,1,-3,4,-1,2,1,-5,4]
#input = [5,4,-1,7,8]
#input = [1,2,-1,-2,2,1,-2,1]
#input = [1,2,-1]
input = [-2,1,0]
print (solution.maxSubArray(input))
