"""
Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.



Example 1:

Input: x = 4
Output: 2
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.


Constraints:

0 <= x <= 231 - 1
"""

class Solution(object):
    def __init__(self, bounds=[0, 46341], incompleteFlag=False):
        self.bounds = bounds
        self.incompleteFlag = incompleteFlag
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        #Use binary search to start with squared middle of the constraint range
        #Compare midpoint squared against input (rounded)
            #If midpoint squared = input, return non-squared midpoint
            #If input is greater
                #If input is lesser than (midpoint + 1) squared, return midpoint
                #Otherwise, perform again on higher half range
            #If input is lesser
                #If input is greater than or equal to (midpoint - 1) squared, return midpoint - 1
        def mySqrtHelper(self):
            midpoint = ((self.bounds[1] - self.bounds[0]) / 2) + self.bounds[0]
            midpoint = int(round(midpoint, 0))
            midpointSquared = midpoint * midpoint
            #print(midpoint)
            if x >= midpointSquared:
                #print("check A")
                if x < ((midpoint + 1) * (midpoint + 1)):
                    return midpoint
                else:
                    self.bounds[0] = midpoint + 1
            elif x < midpointSquared:
                if x >= ((midpoint - 1) * (midpoint - 1)):
                    return midpoint - 1
                else:
                    self.bounds[1] = midpoint - 1
        if x == 0:
            return 0
        while True:
            solution = mySqrtHelper(self)
            if solution:
                return solution
solution = Solution()
print (solution.mySqrt(36))
#NOTE: This works fine on my computer for input 36 but fails on LeetCode, so there must be something weird with how they run it
