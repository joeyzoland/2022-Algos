
"""
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

Example 1:

Input: head = [1,1,2]
Output: [1,2]
Example 2:

Input: head = [1,1,2,3,3]
Output: [1,2,3]

Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #Set current node to head
        #From current node, check next until you find a different value or null
            #If different value
                #Set current node's next to that node
                #Set current node to that next for analysis, next to next next, and repeat the process
            #If null
                #Set current node's next to null
                #Return the head

        if head == None:
            return None
        currentNode = head
        nextNode = head.next
        while True:
            if nextNode == None:
                currentNode.next = None
                return head
            elif currentNode.val == nextNode.val:
                nextNode = nextNode.next
            elif currentNode.val != nextNode.val:
                currentNode.next = nextNode
                currentNode = nextNode
                nextNode = nextNode.next

solution = Solution()

firstNode = ListNode(1)
secondNode = ListNode(1)
thirdNode = ListNode(2)
firstNode.next = secondNode
secondNode.next = thirdNodei

newHead = solution.deleteDuplicates(firstNode)
print(newHead.val)
print(newHead.next.val)
print(newHead.next.next)
