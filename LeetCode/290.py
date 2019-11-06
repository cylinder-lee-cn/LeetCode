"""
290. 单词模式

给定一种 pattern(模式) 和一个字符串 str ，判断 str 是否遵循相同的模式。
这里的遵循指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应模式。

示例1:
输入: pattern = "abba", str = "dog cat cat dog"
输出: true

示例 2:
输入:pattern = "abba", str = "dog cat cat fish"
输出: false

示例 3:
输入: pattern = "aaaa", str = "dog cat cat dog"
输出: false

示例 4:
输入: pattern = "abba", str = "dog dog dog dog"
输出: false

说明:
你可以假设 pattern 只包含小写字母， str 包含了由单个空格分隔的小写字母。
"""


class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """

        dp = {}
        ds = {}

        strs = str.split(' ')
        lp = len(pattern)
        ls = len(strs)

        if (lp != ls):
            return False

        for i in range(lp):
            k, v = pattern[i], strs[i]
            rp = dp.get(k)
            rs = ds.get(v)

            if (rp is None):
                dp[k] = v
            elif (rp != v):
                return False

            if (rs is None):
                ds[v] = k
            elif (rs != k):
                return False
        return True


s = Solution()
print(s.wordPattern('abba', 'dog cat cat dog'))

print(s.wordPattern('aa', 'dog cat'))
