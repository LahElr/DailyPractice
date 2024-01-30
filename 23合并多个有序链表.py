# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import List, Optional
import heapq


ListNode.__lt__ = lambda x,y: False if (x is None or y is None) else x.val<y.val
ListNode.__le__ = lambda x,y: False if (x is None or y is None) else x.val<=y.val
ListNode.__eq__ = lambda x,y: False if (x is None or y is None) else x.val==y.val
ListNode.__ne__ = lambda x,y: False if (x is None or y is None) else x.val!=y.val
ListNode.__gt__ = lambda x,y: False if (x is None or y is None) else x.val>y.val
ListNode.__ge__ = lambda x,y: False if (x is None or y is None) else x.val>=y.val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        queue = []
        for head in lists:
            if head is not None:
                queue.append((head.val,head))
        if len(queue) == 0:
            return None

        heapq.heapify(queue)
        
        head = heapq.heappop(queue)[1]
        cur = head
        next_node = head.next
        if next_node is not None:
            heapq.heappush(queue,(next_node.val,next_node))

        while True:
            if len(queue) <= 0:
                cur.next = None
                return head
            cur.next = heapq.heappop(queue)[1]
            cur = cur.next
            next_node = cur.next
            if next_node is not None:
                heapq.heappush(queue,(next_node.val,next_node))
