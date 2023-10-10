r'''设计一个算法收集某些股票的每日报价，并返回该股票当日价格的 跨度 。

当日股票价格的 跨度 被定义为股票价格小于或等于今天价格的最大连续日数（从今天开始往回数，包括今天）。

例如，如果未来 7 天股票的价格是 [100,80,60,70,60,75,85]，那么股票跨度将是 [1,1,1,2,1,4,6] 。

实现 StockSpanner 类：

StockSpanner() 初始化类对象。
int next(int price) 给出今天的股价 price ，返回该股票当日价格的 跨度 。

'''

r'''
不需要记忆增长序列，大数会掩盖前面的小数，因此：
维护一个栈，保存前序的大数和对应的span
这个栈是保证递减的
'''

class StockSpanner(object):

    def __init__(self):
        self.price_stack = []
        self.span_stack = []

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        if len(self.price_stack) == 0:
            self.price_stack.append(price)
            self.span_stack.append(1)
            return 1
        
        span = 1
        while True:
            if len(self.price_stack)<=0:
                break
            if price >= self.price_stack[-1]:
                span+=self.span_stack.pop()
                self.price_stack.pop()
            else:
                break
        self.price_stack.append(price)
        self.span_stack.append(span)
        return span

operations = ["StockSpanner", "next", "next", "next", "next", "next", "next", "next"]
prices = [[], [100], [80], [60], [70], [60], [75], [85]]

# Your StockSpanner object will be instantiated and called as such:
obj = StockSpanner()
for i in range(1,len(operations)):
    p = obj.next(prices[i][0])
    print(f"{p}->",end="")