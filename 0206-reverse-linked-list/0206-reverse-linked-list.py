# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        try:
            body = head
            temp = head.next
            tail = temp.next
            head.next = None

            while tail != None:
                temp.next = body
                body = temp
                temp = tail
                tail = tail.next

            temp.next = body
            head = temp

            return head
        except:
            return head