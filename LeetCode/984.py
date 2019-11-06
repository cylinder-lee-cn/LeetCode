"""
984. 不含 AAA 或 BBB 的字符串

给定两个整数 A 和 B，返回任意字符串 S，要求满足：

S 的长度为 A + B，且正好包含 A 个 'a' 字母与 B 个 'b' 字母；
子串 'aaa' 没有出现在 S 中；
子串 'bbb' 没有出现在 S 中。

示例 1：
输入：A = 1, B = 2
输出："abb"
解释："abb", "bab" 和 "bba" 都是正确答案。

示例 2：
输入：A = 4, B = 1
输出："aabaa"

提示：
0 <= A <= 100
0 <= B <= 100
对于给定的 A 和 B，保证存在满足要求的 S。
"""


class Solution:
    def strWithout3a3b(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: str
        """
        result = []
        while A or B:
            if len(result) >= 2 and result[-1] == result[-2]:
                useA = result[-1] == 'b'
            else:
                useA = A >= B

            if useA:
                A = A - 1
                result.append('a')
            else:
                B = B - 1
                result.append('b')
        return ''.join(result)


s = Solution()
print(s.strWithout3a3b(1, 2))
print(s.strWithout3a3b(4, 1))
print(s.strWithout3a3b(6, 2))
"""
此题解法：
* 应该选择当前剩余多的待写字母写入字符串中，比如A=6，B=2，那么应该写出aabaabaa。
* 假如：当前剩余多的待写字母为x，只有当前两个已经是x的时候，下一个字母才不该选择这个字母

"""
