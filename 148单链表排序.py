from typing import Optional
from LinkedList import LinkedList
from LinkedList import LinkedListNode as ListNode


class Solution:
    def sortList_bubble(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        if length == 1:
            return head

        for i in range(length - 1, 0, -1):
            cur = head
            for j in range(i):
                if cur.next.val < cur.val:
                    cur.next.val, cur.val = cur.val, cur.next.val
                cur = cur.next
        return head
    
    def sortList(self, head: ListNode) -> ListNode:
        #lahelr 自底向上归并
        r'''
        作者：力扣官方题解
        链接：https://leetcode.cn/problems/sort-list/solutions/492301/pai-xu-lian-biao-by-leetcode-solution/
        来源：力扣（LeetCode）
        著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
        '''
        def merge(head1: ListNode, head2: ListNode) -> ListNode:
            dummyHead = ListNode(0)
            temp, temp1, temp2 = dummyHead, head1, head2
            while temp1 and temp2:
                if temp1.val <= temp2.val:
                    temp.next = temp1
                    temp1 = temp1.next
                else:
                    temp.next = temp2
                    temp2 = temp2.next
                temp = temp.next
            if temp1:
                temp.next = temp1
            elif temp2:
                temp.next = temp2
            return dummyHead.next
        
        if not head:
            return head
        
        length = 0
        node = head
        while node:
            length += 1
            node = node.next
        
        dummyHead = ListNode(0, head)
        subLength = 1
        while subLength < length:
            prev, curr = dummyHead, dummyHead.next
            while curr:
                head1 = curr
                for i in range(1, subLength):
                    if curr.next:
                        curr = curr.next
                    else:
                        break
                head2 = curr.next
                curr.next = None
                curr = head2
                for i in range(1, subLength):
                    if curr and curr.next:
                        curr = curr.next
                    else:
                        break
                
                succ = None
                if curr:
                    succ = curr.next
                    curr.next = None
                
                merged = merge(head1, head2)
                prev.next = merged
                while prev.next:
                    prev = prev.next
                curr = succ
            subLength <<= 1
        
        return dummyHead.next
    
    def sortList_trick(self,head):
        content = []
        cur = head
        while cur:
            content.append(cur.val)
            cur = cur.next

        content.sort()
        cur = head
        for n in content:
            cur.val = n
            cur = cur.next
        return head



# l1 = LinkedList([15, 13, 3, 2, 17, 2, 5, 13, 8, 16])
# l2 = LinkedList([15, 13, 3, 2, 17, 2, 5, 13, 8, 16])

l = [4,2,1,3]
l1 = LinkedList(l)
l2 = LinkedList(l)

l1.sort()
print(l1)
print(Solution().sortList(l2.head))
print(l2)

2,1,4,3
