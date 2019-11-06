"""
204. 计数质数

统计所有小于非负整数 n 的质数的数量。

示例:
输入: 10
输出: 4
解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
"""


class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if (n==0):
            return 0

        isprime = [True] * (n + 1)
        isprime[0] = False  # 0不是素数
        isprime[1] = False  # 1不是素数
        count = 0

        for i in range(2, int(n ** 0.5) + 1):
            if isprime[i]:
                for j in range(i * i, n + 1, i):
                    isprime[j] = False

        for k in range(2, n):
            if isprime[k]:
                count = count + 1
        return count


s = Solution()
print(s.countPrimes(2))
"""
此题解法(参考Wiki百科上的埃拉托斯特尼筛法,
https://zh.wikipedia.org/wiki/%E5%9F%83%E6%8B%89%E6%89%98%E6%96%AF%E7%89%B9%E5%B0%BC%E7%AD%9B%E6%B3%95)

埃拉托斯特尼筛法（希腊语：κόσκινον Ἐρατοσθένους，英语：sieve of Eratosthenes ），简称埃氏筛，也有人称素数筛。
这是一种简单且历史悠久的筛法，用来找出一定范围内所有的素数。

所使用的原理是从2开始，将每个素数的各个倍数，标记成合数。一个素数的各个倍数，是一个差为此素数本身的等差数列。
此为这个筛法和试除法不同的关键之处，后者是以素数来测试每个待测数能否被整除。

埃拉托斯特尼筛法是列出所有小素数最有效的方法之一，其名字来自于古希腊数学家埃拉托斯特尼，
并且被描述在另一位古希腊数学家尼科马库斯所著的《算术入门》中。
"""
