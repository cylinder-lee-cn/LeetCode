"""
784. 字母大小写全排列

给定一个字符串S，通过将字符串S中的每个字母转变大小写，我们可以获得一个新的字符串。
返回所有可能得到的字符串集合。

示例:
输入: S = "a1b2"
输出: ["a1b2", "a1B2", "A1b2", "A1B2"]

输入: S = "3z4"
输出: ["3z4", "3Z4"]

输入: S = "12345"
输出: ["12345"]

注意：
S 的长度不超过12。
S 仅由数字和字母组成。
"""


class Solution:
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        result = ['']
        for s in S:
            l_r = len(result)
            for i in range(l_r):
                a = result[i]
                if (s.isdigit()):
                    result[i] = (a + s)
                if (s.isalpha()):
                    result[i] = (a + s.lower())
                    result.append(a + s.upper())

        # print(result)
        return result


s = Solution()
s.letterCasePermutation('a1b2')
s.letterCasePermutation('3z4')
s.letterCasePermutation('12345')
"""
此题解法：每一个字母位就会将字符串产生两种结果，一种是大写，一种是小写。
生成的每个新字符串又会产两个可能的字符串。
如果有S中有N个字母，那就是 2的N次方个子字符串。就是N个组合C(2,1)
* 先预设result['']
* 当取到s是数字，那就依次给result中的字符串 +s
* 当取到s是字母时，那就依次给result中的字符串+ s.lower()，
    再给result.append(原字符串+s.upper())，可以先把result[i]取出来备用。
* 遍历完S，result就是结果

如下写得很优雅：
        res = ['']
        for ch in S:
            if ch.isalpha():
                res = [i+j for i in res for j in [ch.upper(), ch.lower()]]
            else:
                res = [i+ch for i in res]
        return res

"""
