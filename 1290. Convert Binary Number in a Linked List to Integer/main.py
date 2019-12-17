# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        res = []
        while head:
            res.append(head.val)
            head = head.next
        ans = 0
        f = 1
        for e in res[::-1]:
            ans += e * f
            f = f * 2
        
        return ans
