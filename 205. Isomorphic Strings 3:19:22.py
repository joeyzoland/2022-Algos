"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.



Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true


Constraints:

1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.
"""

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        #Create two dictionaries, one for s and one for t, where the keys are letters and the values are lists of indices
        #Iterate through the strings and, if every list of indices for s matches the same list of indices for t, keep going (if they don't return false)
        #If you get all the way through, return true
        sDict = {}
        tDict = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            sLetter = s[i]
            tLetter = t[i]
            if sLetter not in sDict:
                sDict[sLetter] = [i]
            else:
                sDict[sLetter].append(i)
            if tLetter not in tDict:
                tDict[tLetter] = [i]
            else:
                tDict[tLetter].append(i)
        for i in range(len(s)):
            sLetter = s[i]
            tLetter = t[i]
            if sDict[sLetter] != tDict[tLetter]:
                return False
        return True

solution = Solution()
s = "egg"
t = "add"
print(solution.isIsomorphic(s, t))
