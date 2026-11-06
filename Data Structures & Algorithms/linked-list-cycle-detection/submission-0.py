# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        '''
        O(n) space approach would to have a set of all nodes we've visited
        -also O(n) time

        With O(1) space, we need two indicies: fast and slow pointer, because 
        the fast pointer will catch up to the slow pointer if there exists
        a loop in the linked list
        '''
        fast, slow = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        
        return False