
from typing import Optional
from LinkedList import LinkedList,LinkedListNode
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    def reverseList(self, head):
        prev = None
        cur = head
        next_node = None
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        return prev

data = [1,2,3,4,5]
linked_list = LinkedList(data)
new_head = Solution().reverseList(linked_list.head)
while new_head:
    print(f"{new_head.val}->",end="")
    new_head = new_head.next

