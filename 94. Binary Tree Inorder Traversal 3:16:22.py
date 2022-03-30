"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.



Example 1:


Input: root = [1,null,2,3]
Output: [1,3,2]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]


Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def __init__(self):
        self.answer = []
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        #Traverse to current node
        #If it's null, return
        #Run program on left node
        #Append val to answer list
        #Run program on right node
        #Return answer list
        if root == None:
            return self.answer
        self.inorderTraversal(root.left)
        self.answer.append(root.val)
        self.inorderTraversal(root.right)
        return self.answer

solution = Solution()
root = TreeNode(1)
first = TreeNode(2)
second = TreeNode(3)
root.right = first
first.left = second
print(solution.inorderTraversal(root))
