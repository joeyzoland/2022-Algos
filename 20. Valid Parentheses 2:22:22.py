"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false


Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #Initialize a list that will hold left brackets in a stack
        #Initialize additional lists for left and right brackets with matching parentheses in same order
        #Iterate through the string (s) left to right
            #If the character is a left parentheses:
                #Add to stack
            #If the character is a right parentheses:
                #Check if left parentheses list is empty
                    #If it is, return false
                #Pop the character off the left parentheses list
                #If the left doesn't match the current right
                    #Return false
        #If there's anything left in the left parentheses list
            #Return false
        #Otherwise, return true

        leftovers = []
        left_list = ["(", "{", "["]
        right_list = [")", "}", "]"]
        for paren in s:
            if paren in left_list:
                leftovers.append(paren)
            elif paren in right_list:
                left_index = right_list.index(paren)
                correct_left_char = left_list[left_index]
                if len(leftovers) == 0:
                    return False
                left_char = leftovers.pop()
                if left_char != correct_left_char:
                    return False
        if len(leftovers) != 0:
            return False
        return True

solution = Solution()
input = "()[]{}"
print(solution.isValid(input))
