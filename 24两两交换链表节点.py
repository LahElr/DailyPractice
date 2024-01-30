from LinkedList import LinkedListNode as ListNode
from typing import Optional


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        dummy_head = ListNode(0,head)
        cur = dummy_head

        while True:
            if not cur:
                return dummy_head.next
            next_node = cur.next
            if not next_node:
                return dummy_head.next
            nnext_node = cur.next.next
            if not nnext_node:
                return dummy_head.next
            nnnext_node = nnext_node.next

            next_node.next = nnnext_node
            nnext_node.next = next_node
            cur.next = nnext_node

            cur = next_node