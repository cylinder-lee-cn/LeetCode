"""
394. 字符串解码

给定一个经过编码的字符串，返回它解码后的字符串。

编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。
你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。
此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。

示例:
s = "3[a]2[bc]", 返回 "aaabcbc".
s = "3[a2[c]]", 返回 "accaccacc".
s = "2[abc]3[cd]ef", 返回 "abcabccdcdcdef".
"""


class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []

        def pop_chr(ss):
            temp = ''
            while (not ss[-1].isdigit() and len(ss) > 0):
                t = ss.pop()
                if (t == '['):
                    break
                else:
                    temp = t + temp
            return temp

        def pop_num(ss):
            temp = ''
            while (len(ss) > 0 and ss[-1].isdigit()):
                t = ss.pop()
                temp = t + temp
            return temp

        for c in s:
            if (c != ']'):
                stack.append(c)
            else:
                chrs = pop_chr(stack)
                nums = pop_num(stack)
                tempstr = chrs * (int(nums) if len(nums) > 0 else 1)
                stack.append(tempstr)

            # print(stack)
        return ''.join(stack)


s = Solution()
print(s.decodeString('3[a]2[bc]'))
print(s.decodeString('3[a2[c]]'))
print(s.decodeString('2[abc]3[cd]ef'))
print(s.decodeString('[][]'))
"""
此题解法：
* 此题和判断括号是否成对，是否符合括号成对的合法性的方法类似。
* 第一个栈stack，遍历字符串，只要字符不是‘]’，都要入栈
* 当发现‘]’，就要将对应离栈顶最近的‘[’左边数字和右边字母都出栈，这里利用了2个子函数
* 拿到字母和数字后，将字母按照数字的数量进行重复，得到的结果重新入栈。
* 一直重复到遍历完s
* 返回stack中的结果
"""
