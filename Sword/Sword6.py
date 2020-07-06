# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


from collections import deque

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        if head == None:
            return []
        
        ret = []
        while head:
            ret.append(head)
            head = head.next
        
        return reversed(ret)
        
        