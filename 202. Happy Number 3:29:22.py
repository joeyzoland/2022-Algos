"""Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.



Example 1:

Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
Example 2:

Input: n = 2
Output: false


Constraints:

1 <= n <= 231 - 1
"""

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        #Initialize a set that will hold seen values
        #Start a while loop where you add the sum of squares of digits
            #If you ever hit 1, return True
            #If you ever see a number that you've seen before, return False
        #EXAMPLE: How to iterate through digits without len conversion
        #195
        #mod 10, get 5
        #square 5 and hold
        #subtract 5 from n (n = 190)
        #divide n by 10 (19)
        #repeat
        seenSet = set()
        while True:
            if n == 1:
                return True
            if n in seenSet:
                return False

            seenSet.add(n)
            newN = 0

            while n > 0:
                currentDigit = n % 10
                newN += (currentDigit * currentDigit)
                n -= currentDigit
                n /= 10
            n = newN

solution = Solution()
input = 19
print solution.isHappy(input)
