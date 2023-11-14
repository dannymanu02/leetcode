# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        temp = head
        cnt = 0

        while temp != None:
            cnt += 1
            temp = temp.next

        p2 = head
        p1 = head
        temp = head

        if cnt == 1 or cnt == 2:
            return

        if cnt%2 != 0:
            for i in range(0, cnt//2+1):
                temp = p2
                p2 = p2.next
        else:
            for i in range(0, cnt//2):
                temp = p2
                p2 = p2.next

        temp.next = None

        # reverse start 

        prev = None
        cur = p2
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        # reverse end

        p2 = prev

        t1 = p1.next
        t2 = p2.next

        for passNum in range(1, cnt):
            if passNum%2 != 0:
                p1.next = p2
                p1 = t1
                if t1!= None:
                    t1 = t1.next
            else:
                p2.next = p1
                p2 = t2
                if t2!= None:
                    t2 = t2.next

