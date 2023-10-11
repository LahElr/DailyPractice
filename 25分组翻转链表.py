r"""
给你链表的头节点 head ，每 k 个节点一组进行翻转，请你返回修改后的链表。
k 是一个正整数，它的值小于或等于链表的长度。
如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
"""

from typing import Optional
from LinkedList import LinkedListNode as ListNode
from LinkedList import LinkedList


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None
        if k <= 1:
            return head
        current_group_start_cur = head
        current_group_end_cur = head
        current_group_start_prev_cur = None
        current_group_end_next_cur = None
        break_flag = False
        while True:
            for _ in range(k - 1):
                current_group_end_cur = current_group_end_cur.next
                if current_group_end_cur is None:
                    break_flag = True
                    break

            if break_flag:
                break

            current_group_end_next_cur = current_group_end_cur.next
            s, e = self.reversePart(current_group_start_cur, current_group_end_cur)
            if current_group_start_prev_cur is not None:
                current_group_start_prev_cur.next = s
            else:
                head = s
            e.next = current_group_end_next_cur

            if current_group_end_next_cur is None:
                break
            current_group_start_prev_cur = current_group_start_cur
            current_group_start_cur = current_group_end_next_cur
            current_group_end_cur = current_group_end_next_cur

        return head

    def reversePart(self, head, end):
        if head.next is None or head == end:
            return head, end
        cur = head.next
        prev = head
        while True:
            next = cur.next
            cur.next = prev

            if cur == end:
                break

            prev = cur
            cur = next

        return end, head


ll = LinkedList([1,2])
s = Solution()
h = s.reverseKGroup(ll.head,k=2)
ll.head = h
print(ll)
print(h)