r"""给你一个产品数组 products 和一个字符串 searchWord ，
products  数组中每个产品都是一个字符串。
请你设计一个推荐系统，
在依次输入单词 searchWord 的每一个字母后，
推荐 products 数组中前缀与 searchWord 相同的最多三个产品。
如果前缀相同的可推荐产品超过三个，请按字典序返回最小的三个。
请你以二维列表的形式，返回在输入 searchWord 每个字母后相应的推荐产品的列表。
"""
import bisect
from typing import DefaultDict, List


def order(ch):
    return ord(ch) - 97


class Solution:
    def suggestedProducts(
        self, products: List[str], searchWord: str
    ) -> List[List[str]]:
        # 前缀树？
        # 先排序，然后二分查找
        products.sort()
        ans = []
        pos = 0
        for i in range(len(searchWord)):
            prefix = searchWord[: i + 1]
            pos = bisect.bisect_left(products, prefix, pos)
            ans.append([_ for _ in products[pos : pos + 3] if _.startswith(prefix)])
        return ans


products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
searchWord = "mouse"
print(Solution().suggestedProducts(products, searchWord))
