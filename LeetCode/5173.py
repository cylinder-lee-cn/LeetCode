"""
5173. 质数排列

请你帮忙给从 1 到 n 的数设计排列方案，使得所有的「质数」都应该被放在「质数索引」（索引从 1 开始）上；你需要返回可能的方案总数。
让我们一起来回顾一下「质数」：质数一定是大于 1 的，并且不能用两个小于它的正整数的乘积来表示。
由于答案可能会很大，所以请你返回答案 模 mod 10^9 + 7 之后的结果即可。

示例 1：
输入：n = 5
输出：12
解释：举个例子，[1,2,5,4,3] 是一个有效的排列，但 [5,2,3,4,1] 不是，因为在第二种情况里质数 5 被错误地放在索引为 1 的位置上。

示例 2：
输入：n = 100
输出：682289015

提示：
1 <= n <= 100
"""

from functools import reduce


class Solution:
    def factorial(self, m: int):
        return reduce(lambda x, y: x * y, range(1, m + 1))

    def numPrimeArrangements(self, n: int) -> int:
        primes = [
            2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61,
            67, 71, 73, 79, 83, 89, 97
        ]

        pCount = len([x for x in primes if x <= n])
        cCount = n - pCount

        a = self.factorial(pCount)
        b = self.factorial(cCount)

        return (a * b) % (10**9 + 7)


"""
此题解法：
* 由于n在1-100内，所以可以先统计出100以内的质数个数
* 排列组合的结果就是，质数全排列的结果乘以合数全排列的结果
* 比如n=5，那么就是2 3 5 全排列结果是6；
  1 4 全排列结果是2，最后结果是6*2
* 那么可以将1-100都计算出最后的结果然后进行查表
"""

s = Solution()
print(s.numPrimeArrangements(7))
