class Solution(object):
    solutionsDict = {1:1, 2:2}
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        #Recursively iterate at each step, looking at 1 or 2 steps
        #If you ever hit 1, return 1; for 2, return 2
        if n in self.solutionsDict:
            return self.solutionsDict[n]
        else:
            oneAndTwoStep = self.climbStairs(n - 1) + self.climbStairs(n - 2)
            self.solutionsDict[n] = oneAndTwoStep
            return oneAndTwoStep
        return self.climbStairs(n)

solution = Solution()
input = 38
print (solution.climbStairs(input))
