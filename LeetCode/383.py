"""
383. 赎金信

给定一个赎金信 (ransom) 字符串和一个杂志(magazine)字符串，
判断第一个字符串ransom能不能由第二个字符串magazines里面的字符构成。如果可以构成，返回 true ；否则返回 false。
(题目说明：为了不暴露赎金信字迹，要从杂志上搜索各个需要的字母，组成单词来表达意思。)

注意：
你可以假设两个字符串均只含有小写字母。

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
"""


class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        words = {}

        rl = len(ransomNote)
        ml = len(magazine)

        if (rl > ml):
            return False

        if (rl == 0):
            return True

        while (rl > 0):
            rw = ransomNote[rl - 1]
            if (words.get(rw)):
                words[rw] = words[rw] - 1
            else:
                words[rw] = -1
            rl = rl - 1

        while (ml > 0):
            mw = magazine[ml - 1]
            if (words.get(mw)):
                words[mw] = words[mw] + 1
            ml = ml - 1

        print(words)

        for i in words.values():
            if (i < 0):
                return False
        return True



s = Solution()
print(s.canConstruct('fihjjjjei', 'hjibagacbhadfaefdjaeaebgi'))
