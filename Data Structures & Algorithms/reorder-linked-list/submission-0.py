# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        '''
        build two linked lists? then weave them together, but O(1) space is
        advised

        note that beginning half points to the second half of the list
        firs half merged with reversed second half
        '''
        slow, fast = head, head.next

        while fast and fast.next:
            # first, get to the midway point, since once fast reaches
            # the end, slow will be at the middle
            slow = slow.next
            fast = fast.next.next
        
        # now slow is at the midway, or stops right before the midpoint if
        # list is even. Thus we can reverse the rest of the list starting
        # at slow, then loop through the front and weave together the twp
        # parts of the list
        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
            

