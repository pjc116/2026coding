#week09-5.py 學習計畫Linked List 第1題
#LeetCode 2095. Delete the Middle Node of a Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head

        while fast != None and fast.next != None:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        prev.next = slow.next
        return head
