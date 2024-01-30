from sortedcontainers import SortedList

class MedianFinder:

    def __init__(self):
        self.nums = SortedList()
        self.lptr = None
        self.rptr = None

    def addNum(self, num: int) -> None:

        n = len(self.nums)
        self.nums.add(num)

        if n == 0:
            self.lptr = self.rptr = 0
        else:
            if num < self.nums[self.lptr]:
                self.lptr += 1
            if num < self.nums[self.rptr]:
                self.rptr += 1

            if n % 2 == 1:
                if num < self.nums[self.lptr]:
                    self.lptr -= 1
                else:
                    self.rptr += 1
            else:
                if self.nums[self.lptr] < num < self.nums[self.rptr]:
                    self.lptr += 1
                    self.rptr -= 1
                elif num >= self.nums[self.rptr]:
                    self.lptr += 1
                else:
                    self.rptr -= 1
                    self.lptr = self.rptr

    def findMedian(self) -> float:
        return (self.nums[self.lptr] + self.nums[self.rptr]) / 2