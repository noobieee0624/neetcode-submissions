# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
        have two pointers that are n distance apart, so that when we reach 
        the end, the second pointer would be at the node we want to remove,
        so say we have [1,2,3,4], then we have two pointers slow and fast

        slow = 0
        fast = 0

        slow.next
        fast.next*n

        if we are at the end, then slow is at the node right before we need
        to remove--we bypass that node
        '''
        dummy = ListNode(0, head)
        slow = fast = dummy

        # create the gap: fast moves n + 1 steps ahead
        for _ in range(n + 1):
            fast = fast.next

        # move both until fast falls off the end
        while fast:
            slow = slow.next
            fast = fast.next

        # slow is now right before the node to remove
        slow.next = slow.next.next
        return dummy.next




