"""
686. 重复叠加字符串匹配

给定两个字符串 A 和 B, 寻找重复叠加字符串A的最小次数，使得字符串B成为叠加后的字符串A的子串，
如果不存在则返回 -1。

举个例子，A = "abcd"，B = "cdabcdab"。

答案为 3， 因为 A 重复叠加三遍后为 “abcdabcdabcd”，此时 B 是其子串；
A 重复叠加两遍后为"abcdabcd"，B 并不是其子串。

注意:
A 与 B 字符串的长度在1和10000区间范围内。
"""


class Solution:
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        for i in range(1, len(B) // len(A) + 3):
            t = A * i
            if (B in t):
                return i
        return -1


s = Solution()
print(s.repeatedStringMatch('abcd', 'cdabcdab'))
"""
此题解法：
* 如果B in A 那么 len(A)>=len(B)
* A重复n次后，A长度>=B长度，如果依然不包含B，再重复一次就可以最终验证B是否是A的子串
"""
