from collections import deque
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        number_to_chars = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        ans = deque([""])
        l = len(digits)
        if l == 0:
            return []
        while True:
            cur = ans.popleft()
            if len(cur) >= l:
                ans.append(cur)
                break
            digit = digits[len(cur)]
            for char in number_to_chars[digit]:
                ans.append(cur + char)
        return list(ans)
