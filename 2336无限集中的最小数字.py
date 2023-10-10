r'''
现有一个包含所有正整数的集合 [1, 2, 3, 4, 5, ...] 。

实现 SmallestInfiniteSet 类：

SmallestInfiniteSet() 初始化 SmallestInfiniteSet 对象以包含 所有 正整数。
int popSmallest() 移除 并返回该无限集中的最小整数。
void addBack(int num) 如果正整数 num 不 存在于无限集中，则将一个 num 添加 到该无限集中。
'''

r'''
分别记录当前最小的数字和已经被删去的数字
这个用来记录被删去的数字的结构需要：高效的查询、添加、删除
~~最好能对序列查询有特别优化~~
'''

class SmallestInfiniteSet(object):

    def __init__(self):
        self.current_smallest = 1
        self.current_deleted_numbers = set()

    def popSmallest(self):
        """
        :rtype: int
        """
        ret = self.current_smallest
        self.current_deleted_numbers.add(ret)
        while True:
            self.current_smallest +=1
            if self.current_smallest in self.current_deleted_numbers:
                continue
            else:
                break
        return ret


    def addBack(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num in self.current_deleted_numbers:
            self.current_deleted_numbers.remove(num)
            if num < self.current_smallest:
                self.current_smallest = num 



# Your SmallestInfiniteSet object will be instantiated and called as such:
obj = SmallestInfiniteSet()

operations = ["SmallestInfiniteSet", "addBack", "popSmallest", "popSmallest", "popSmallest", "addBack", "popSmallest", "popSmallest", "popSmallest"]
nums = [[], [2], [], [], [], [1], [], [], []]
for operation,num in zip(operations[1:],nums[1:]):
    if operation == "popSmallest":
        param = obj.popSmallest()
    elif operation == "addBack":
        param = obj.addBack(num[0])
    print(param,end=" - ")


