# Question: https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Solution:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head
        # Maintain a Gap of 'n' between the pointers
        while n > 0 and right:
            right = right.next
            n -= 1
        while right:
            left = left.next
            right = right.next
        left.next = left.next.next
        return dummy.next
 
# Verdict:
# Runtime: 28 ms, faster than 92.71% of Python3 online submissions for Remove Nth Node From End of List.
# Memory Usage: 14.3 MB, less than 14.63% of Python3 online submissions for Remove Nth Node From End of List.
