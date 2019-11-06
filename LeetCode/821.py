"""
821. 字符的最短距离
给定一个字符串 S 和一个字符 C。返回一个代表字符串 S 中每个字符到字符串 S 中的字符 C 的最短距离的数组。

示例 1:
输入: S = "loveleetcode", C = 'e'
输出: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]

说明:
字符串 S 的长度范围为 [1, 10000]。
C 是一个单字符，且保证是字符串 S 里的字符。
S 和 C 中的所有字母均为小写字母。
"""


class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        slen = len(S)
        cindexs = []
        result = [slen] * slen

        for i, s in enumerate(S):
            if (s == C):
                cindexs.append(i)

        for j in cindexs:
            result = [min(abs(j - k), n) for k, n in enumerate(result)]

        return result


s = Solution()
print(s.shortestToChar('loveleetcode', 'e'))
"""
此题解法：
* 在S中找到所有C的位置放入cindexs
* 最远的距离不会超过字符串的长度，定义一个最远长度的数组result
* 分别使用C的位置来计算到每一位字符的距离，使用abs获取绝对值
* 逐一将计算出来的距离和已有的位置对应比较，对应位置保存min的即可

"""
