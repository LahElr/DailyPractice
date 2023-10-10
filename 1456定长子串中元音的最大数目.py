r'''
给你字符串 s 和整数 k 。
请返回字符串 s 中长度为 k 的单个子字符串中可能包含的最大元音字母数。
英文中的 元音字母 为（a, e, i, o, u）。
题目保证字符串全小写且长度>=k
'''

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a','i','u','e','o'}
        l = len(s)
        current_window_vowel_count = 0
        for ch in s[:k]:
            if ch in vowels:
                current_window_vowel_count+=1
        max_window_vowel_count = current_window_vowel_count
        for lcur in range(1,l-k+1):
            rcur=lcur+k-1
            if s[lcur-1] in vowels:
                current_window_vowel_count-=1
            if s[rcur] in vowels:
                current_window_vowel_count+=1
            max_window_vowel_count = max(current_window_vowel_count,max_window_vowel_count)
        return max_window_vowel_count


s = "abciiidef"
k = 3
print(Solution().maxVowels(s,k))