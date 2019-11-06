"""
58. 最后一个单词的长度


给定一个仅包含大小写字母和空格 ' ' 的字符串，返回其最后一个单词的长度。
如果不存在最后一个单词，请返回 0 。

说明：一个单词是指由字母组成，但不包含任何空格的字符串。

示例:
输入: "Hello World"
输出: 5
"""

class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if (len(s)==0):
            return 0

        a=s.rstrip(' ').split(' ')[-1]
        if (a.isalpha()):
            return len(a)
        else:
            return 0

s=Solution()

print(s.lengthOfLastWord(' i love you    ! '))
print(s.lengthOfLastWord("Hello World"))
print(s.lengthOfLastWord("a "))



