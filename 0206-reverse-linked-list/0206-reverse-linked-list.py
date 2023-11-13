# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # res = []
        
        # if head == None:
        #     return head

        # while head != None:
        #     res.append(head.val)
        #     head = head.next

        # new_list = ListNode(val=res[-1])
        # head = new_list

        # for i in range(len(res)-2, -1, -1):
        #     head.next = ListNode(val=res[i])
        #     head = head.next

        # return new_list
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