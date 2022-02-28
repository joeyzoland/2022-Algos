"""
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.


Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.


Constraints:

-231 <= x <= 231 - 1
"""

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        #If number is negative:
            #Return False
        #If the number of characters is odd:
            #Start i at midpoint - 1 and j at midpoint + 1
        #Else if the number of characters is even:
            #Start i at left midpoint and j at right midpoint
        #Iterate in both directions:
            #If characters at i and j don't match
                #Return False
            #Subtract 1 from i and add 1 to j
        #Return True

        if x < 0:
            return False
        stringX = str(x)
        if len(stringX) % 2 == 1:
            i = int((len(stringX) / 2) - 0.5)
            j = int((len(stringX) / 2) + 1.5)
        elif len(stringX) % 2 == 0:
            i = int((len(stringX) / 2) - 1)
            j = int((len(stringX) / 2))
        while j < len(stringX):
            if stringX[i] != stringX[j]:
                return False
            i -= 1
            j += 1
        return True

solution = Solution()
input = 121
print(solution.isPalindrome(input))
