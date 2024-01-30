from typing import Optional
from LinkedList import LinkedListNode as ListNode
from LinkedList import LinkedList
from LinkedList import merge_ordered_lists
from copy import deepcopy


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # 将两个升序链表合并为一个新的 升序 链表并返回
        if list1 is None:
            return deepcopy(list2)
        if list2 is None:
            return deepcopy(list1)

        root = ListNode()
        cur = root
        ptr1 = list1
        ptr2 = list2

        while True:
            if ptr1 is None and ptr2 is None:
                ret = root.next
                del root
                return ret
            a = float("inf") if ptr1 is None else ptr1.val
            b = float("inf") if ptr2 is None else ptr2.val
            if a < b:
                cur.next = ListNode(val=a)
                ptr1 = ptr1.next
                cur = cur.next
            else:
                cur.next = ListNode(val=b)
                ptr2 = ptr2.next
                cur = cur.next


a = LinkedList([1, 2, 4])
b = LinkedList([1, 3, 4])
c = LinkedList([])
c.length = len(a) + len(b)
c.head = Solution().mergeTwoLists(a.head, b.head)
print(c)

print(merge_ordered_lists(a,b))
