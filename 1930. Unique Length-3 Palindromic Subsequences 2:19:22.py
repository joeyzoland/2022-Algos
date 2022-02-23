"""
Given a string s, return the number of unique palindromes of length three that are a subsequence of s.

Note that even if there are multiple ways to obtain the same subsequence, it is still only counted once.

A palindrome is a string that reads the same forwards and backwards.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".


Example 1:

Input: s = "aabca"
Output: 3
Explanation: The 3 palindromic subsequences of length 3 are:
- "aba" (subsequence of "aabca")
- "aaa" (subsequence of "aabca")
- "aca" (subsequence of "aabca")
Example 2:

Input: s = "adc"
Output: 0
Explanation: There are no palindromic subsequences of length 3 in "adc".
Example 3:

Input: s = "bbcbaba"
Output: 4
Explanation: The 4 palindromic subsequences of length 3 are:
- "bbb" (subsequence of "bbcbaba")
- "bcb" (subsequence of "bbcbaba")
- "bab" (subsequence of "bbcbaba")
- "aba" (subsequence of "bbcbaba")


Constraints:

3 <= s.length <= 105
s consists of only lowercase English letters.
"""

class Solution(object):
    def countPalindromicSubsequence(self, s):
        """
        :type s: str
        :rtype: int
        """
        checkedLetters = set()
        solution = 0
        for i in range(len(s) - 2):
            if s[i] in checkedLetters:
                continue
            checkedLetters.add(s[i])
            for j in range(len(s) - 1, i + 1, -1):
                if s[i] == s[j]:
                    #If you find two letters that match on the inside and
                    #outside, get all unique letters between them and
                    #add that count to your solution
                    internalSet = set()
                    for k in range(i + 1, j):
                        internalSet.add(s[k])
                    solution += len(internalSet)
                    break
        return solution

solution = Solution()
input = "aabca"
print(solution.countPalindromicSubsequence(input))
