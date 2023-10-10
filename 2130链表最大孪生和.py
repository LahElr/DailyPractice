r'''在一个大小为 n 且 n 为 偶数 的链表中，
对于 0 <= i <= (n / 2) - 1 的 i ，第 i 个节点（下标从 0 开始）的孪生节点为第 (n-1-i) 个节点 。

比方说，n = 4 那么节点 0 是节点 3 的孪生节点，
节点 1 是节点 2 的孪生节点。这是长度为 n = 4 的链表中所有的孪生节点。
孪生和 定义为一个节点和它孪生节点两者值之和。

给你一个长度为偶数的链表的头节点 head ，请你返回链表的 最大孪生和 。
'''

from LinkedList import LinkedList,LinkedListNode
class Solution:
    def pairSum(self, head):
        r'''
        双向链表的话只要O(N)的时间复杂度和额外O(N)的空间复杂度啊……
        '''
        slow = head
        fast = head.next
        while True:
            if fast.next is None:
                break
            slow = slow.next
            fast = fast.next.next # 题目保证链表长度不会是奇数，这里可以放心引用
        first_half_cur = head
        second_half_cur = slow.next
        slow.next = None

        prev = None
        cur = second_half_cur
        next = None
        while cur:
            n = cur.next
            cur.next = prev
            prev = cur
            cur = n
        second_half_cur = prev
        
        max_twin_sum = -float('inf')
        while first_half_cur and second_half_cur:
            v = first_half_cur.val + second_half_cur.val
            max_twin_sum = max(max_twin_sum,v)
            first_half_cur = first_half_cur.next
            second_half_cur = second_half_cur.next
        return max_twin_sum



head = [5,4,2,1,9,10]
ls = LinkedList(head)
ans = Solution().pairSum(ls.head)
print(ans)
