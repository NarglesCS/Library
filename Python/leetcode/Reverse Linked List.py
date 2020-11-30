# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            #queue up the rest of list stariting with next node
            temp = curr.next
            #set the next rest of the list to what has been reversed so far
            curr.next = prev
            # Update the progress as completed
            prev = curr
            # move onto the nest item in the unreversed list
            curr = temp
        return prev
