r'''删除下标是celi(n/2)的节点
我觉得可以用前后指针，前指针每走一步，后指针走两步
前指针后走，后指针先走，后指针走不了了就去掉前指针所指节点的下一个
但是想想，这样两个指针走的步数加起来还是1+N/2，就是取.next的次数
那我直接先数再删，时间应该不差多少吧？
'''

# Definition for singly-linked list.
from typing import Optional
from LinkedList import LinkedList


class Solution:
    def deleteMiddle(self, head):
        lcur = head
        rcur = head
        if head is None or head.next is None:
            return None #?
        while True:
            print(rcur.val,lcur.val)
            try:
                rcur = rcur.next.next
                assert rcur.next
            except (AttributeError,AssertionError):
                # if rcur is None or rcur.next is None or rcur.next.next is None or rcur.next.next.next is None
                # delete the lcur.next node
                lcur.next = lcur.next.next
                break
            lcur = lcur.next
        return head



head = [1]
ls = LinkedList(data=head)
print(ls)
print(Solution().deleteMiddle(ls.head))
print(ls)