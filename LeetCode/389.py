"""
389. 找不同


给定两个字符串 s 和 t，它们只包含小写字母。
字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。
请找出在 t 中被添加的字母。

示例:
输入：
s = "abcd"
t = "abcde"
输出：
e
解释：
'e' 是那个被添加的字母。
"""


class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s1 = set(t)
        s2 = set(s)
        r = s1 - s2

        if (len(r) == 1):
            return ''.join(r)

        for c in s1:
            if (t.count(c) > s.count(c)):
                return c


s = Solution()

print(s.findTheDifference('abcd', 'abcde'))
print(s.findTheDifference('a', 'aa'))
