"""
70. 爬楼梯

假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

示例 1：
输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶

示例 2：
输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶
"""


class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if (n==0):
            return 0

        a, b = 0, 1
        n = n + 1
        for i in range(n):
            a, b = b, a + b
        return a


s = Solution()
print(0, s.climbStairs(0))
print(1, s.climbStairs(1))
print(2, s.climbStairs(2))
print(3, s.climbStairs(3))
print(4, s.climbStairs(4))
print(5, s.climbStairs(5))
print(6, s.climbStairs(6))

"""
分析得知,此题是一个典型的斐波那契数列. 第0项=0,第一项=1, N+1(项)=N(项)+N-1(项)
0,1,1,2,3,5,8,13,21........

台阶数对应关系
1(阶)->1 : 此处是fib数列的第2项
2(阶)->2
3(阶)->3
4(阶)->5
5(阶)->8
.....
"""
