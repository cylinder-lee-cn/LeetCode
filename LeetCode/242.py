"""
242. 有效的字母异位词

给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的一个字母异位词。

示例 1:
输入: s = "anagram", t = "nagaram"
输出: true

示例 2:
输入: s = "rat", t = "car"
输出: false

说明:
你可以假设字符串只包含小写字母。
进阶:
如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？
"""


class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ds = {}
        dt = {}

        for sc in s:
            if (sc in ds):
                ds[sc] = ds[sc] + 1
            else:
                ds[sc] = 1

        for tc in t:
            if (tc in dt):
                dt[tc] = dt[tc] + 1
            else:
                dt[tc] = 1

        if (len(ds) != len(dt)):
            return False

        for k in ds.keys():
            if (dt.get(k) is None):
                return False
            if (ds[k] != dt[k]):
                return False

        return True


s = Solution()
print(s.isAnagram('silent', 'listen'))

print(s.isAnagram('apple', 'aplee'))

print(s.isAnagram('nagaram', 'anagram'))

print(s.isAnagram('a', 'b'))
print(s.isAnagram('a', 'ab'))
