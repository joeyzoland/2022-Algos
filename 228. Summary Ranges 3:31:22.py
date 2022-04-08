"""
You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b


Example 1:

Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"
Example 2:

Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"


Constraints:

0 <= nums.length <= 20
-231 <= nums[i] <= 231 - 1
All the values of nums are unique.
nums is sorted in ascending order.
"""

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        #Handle edge cases of length 0 and 1
        #Initialize a solution list
        #Initialize start and end as first number
        #Iterate through rest of nums
            #If they are consecutive:
                #Update end to current num
            #When you find a number that isn't consecutive:
                #If the start and end are the same:
                    #Add string of that number to solution list
                #If they're different
                    #Format appropriately and add to solution list
                #Update start and end to new, non-consecutive number
        #After you reach the end of the list, perform above comparison once more
        #Return solution list
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [str(nums[0])]
        solution = []
        start = nums[0]
        end = nums[0]
        for number in nums[1:]:
            if number != end + 1:
                if start == end:
                    solution.append(str(start))
                else:
                    solution.append(str(start) + "->" + str(end))
                start = number
            end = number
        if start == end:
            solution.append(str(start))
        else:
            solution.append(str(start) + "->" + str(end))
        return solution

solution = Solution()
input = [0,1,2,4,5,7]
print solution.summaryRanges(input)
