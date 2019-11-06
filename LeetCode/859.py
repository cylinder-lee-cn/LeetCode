"""
859. 亲密字符串

给定两个由小写字母构成的字符串 A 和 B ，只要我们可以通过交换 A 中的两个字母得到与 B 相等的结果，
就返回 true ；否则返回 false 。


示例 1：
输入： A = "ab", B = "ba"
输出： true

示例 2：
输入： A = "ab", B = "ab"
输出： false

示例 3:
输入： A = "aa", B = "aa"
输出： true

示例 4：
输入： A = "aaaaaaabc", B = "aaaaaaacb"
输出： true

示例 5：
输入： A = "", B = "aa"
输出： false

提示：
0 <= A.length <= 20000
0 <= B.length <= 20000
A 和 B 仅由小写字母构成。
"""


class Solution:
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if (len(A) != len(B)):
            return False

        if (A == B):
            duplicate = set()
            for a in A:
                if (a in duplicate):
                    return True
                else:
                    duplicate.add(a)
            return False
        else:
            pairs = [[x, y] for x, y in zip(A, B) if x != y]
            if (len(pairs) != 2):
                return False
            else:
                return (pairs[0] == pairs[1][::-1])


s = Solution()
print(s.buddyStrings('ab', 'ab'))
print(s.buddyStrings('ab', 'ba'))
print(s.buddyStrings('aa', 'aa'))
print(s.buddyStrings('aaaaaaabc', 'aaaaaaacb'))
print(s.buddyStrings('', 'aa'))
"""
此题解法：
* 首先要求A、B长度相同
* 如果A与B是相同的字符串，就需要字符串中有重复字母，这样交换2个字母，字符串才会不变
* 如果A、B不相同，那么相同索引下不一样的字母只能有2对，比如A[i]：B[i]，A[j]：B[j]
    而且必须满足交换后相同 A[i]==B[j] and A[j]==B[i]
"""
