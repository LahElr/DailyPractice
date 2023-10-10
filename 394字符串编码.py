r"""
给定一个经过编码的字符串，返回它解码后的字符串。
编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。
你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。
此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/decode-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

r'''
写了栈，题解方法二：这是BNF范式下的LL(1)文法，给了个递归
死去的编译原理突然开始攻击我.gif
'''


class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = f"1[{s}]" # ;)
        # 有对应关系，数字栈会一直多一个
        numeral_stack = []
        str_stack = []
        current_in_num_flag = False

        for character in s:
            ch = ord(character)
            if 97 <= ch <= 122:
                # alpha
                str_stack[-1].append(character)
            elif 48 <= ch <= 57:
                # num
                if not current_in_num_flag:
                    numeral_stack.append([])
                    current_in_num_flag = True
                numeral_stack[-1].append(character)
            elif ch == 91:
                # [
                str_stack.append([])
                current_in_num_flag = False
            elif ch == 93:
                # ]
                num = int("".join(numeral_stack.pop()))
                cur_str = ("".join(str_stack.pop())) * num
                if len(str_stack) > 0:
                    str_stack[-1].append(cur_str)
                else:
                    return cur_str
            else:
                raise ValueError(f"Unexpected character {character} of value {ch}!")


s = "3[a]2[bc]"
s = "3[a2[c]]"
s = '2[abc]3[cd]ef'
s = 'abc3[cd]xyz'
x = Solution()
print(x.decodeString(s))
