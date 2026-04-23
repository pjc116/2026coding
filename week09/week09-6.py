#week09-6.py 學習計畫Linked List 第2題
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        even = []
        while head:
            even.append(head.val)
            head = head.next
        n = len(even)
        now = ans = ListNode()
        for i in range(0, n, 2):
            now.next = ListNode(even[i])
            now = now.next
        for i in range(1, n, 2):
            now.next = ListNode(even[i])
            now = now.next
        return ans.next
