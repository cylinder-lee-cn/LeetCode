"""
151. 翻转字符串里的单词

给定一个字符串，逐个翻转字符串中的每个单词。

示例:
输入: "the sky is blue",
输出: "blue is sky the".
说明:

无空格字符构成一个单词。
输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
进阶: 请选用C语言的用户尝试使用 O(1) 空间复杂度的原地解法。

"""


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # s_r = s.split(' ')[::-1]
        # return ' '.join(w for w in s_r if w != '')
        return ' '.join(reversed(s.split()))


s = Solution()
print(s.reverseWords("the   sky   is    blue"))

"""
此题解法：
* python字符串的split方法中分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。
* 不使用带参数的split方法，就直接过滤掉了多余的空格。
* 利用
"""
