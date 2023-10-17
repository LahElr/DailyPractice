from typing import Optional
from LinkedList import LinkedListNode as ListNode
from LinkedList import LinkedList

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #1 <= n <= size <= 30
        target_record = 0
        tgt = head
        n_prev_cur = None
        n_1_prev_cur = None
        if n==1:
            while tgt:
                n_1_prev_cur,n_prev_cur,tgt = n_prev_cur,tgt,tgt.next
        else:
            while True:
                if tgt.next is None:
                    break
                target_record+=1
                if target_record==n-1:
                    n_prev_cur = head
                elif target_record>n-1:
                    n_1_prev_cur = n_prev_cur
                    n_prev_cur = n_prev_cur.next
                tgt = tgt.next
        
        # delete n_prev_cur
        print(n_1_prev_cur,"-->",n_prev_cur)
        if n_prev_cur is None:
            return head
        if n_1_prev_cur is None:
            return head.next
        n_1_prev_cur.next = n_prev_cur.next
        return head
    
ll = LinkedList([1,2,3,4,5,6,7,8,9,10])
s = Solution()
head = s.removeNthFromEnd(ll.head,7)
ll.head = head
print(ll)