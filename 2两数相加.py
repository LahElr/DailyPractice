r'''
以倒序链表方法存储的两个大数的相加
例：
2->4->3 ===> 342
要求返回以同样形式存储的两数和
“你可以假设除了数字 0 之外，这两个数都不会以 0 开头。”
0 <= Node.val <= 9
题目数据保证列表表示的数字不含前导零
'''

from typing import Optional
from LinkedList import LinkedListNode as ListNode
from LinkedList import LinkedList

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        answer_list = ListNode(0)
        answer_cur = answer_list
        l1_cur = l1
        l2_cur = l2
        carry = 0

        while True:
            v1 = l1_cur.val if l1_cur is not None else 0
            v2 = l2_cur.val if l2_cur is not None else 0
            v = v1+v2+carry
            carry = v//10
            v = v%10
            answer_cur.val = v

            l1_cur = l1_cur.next if l1_cur is not None else None
            l2_cur = l2_cur.next if l2_cur is not None else None
            if l1_cur is None and l2_cur is None and carry ==0:
                break
            answer_cur.next = ListNode(0)
            answer_cur = answer_cur.next

        return answer_list

l1 = LinkedList([9,9,9,9,9,9,9])
l2=LinkedList([9,9,9,9])
s = Solution()
n = s.addTwoNumbers(l1.head,l2.head)
l = LinkedList(n)
print(l)
