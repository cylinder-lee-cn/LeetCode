"""
326. 3的幂

给定一个整数，写一个函数来判断它是否是 3 的幂次方。

示例 1:
输入: 27
输出: true

示例 2:
输入: 0
输出: false

示例 3:
输入: 9
输出: true

示例 4:
输入: 45
输出: false

进阶：
你能不使用循环或者递归来完成本题吗？
"""


class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """

        if (n <= 0):
            return False

        if (1162261467 % n == 0):
            return True
        else:
            return False


"""
我们首先分析3的幂的特点，假设一个数Num是3的幂，那么所有Num的约数都是3的幂，
如果一个数n小于Num且是3的幂，那么这个数n一定是Num的约数。

了解上述性质，我们只需要找到一个最大的3的幂，看看参数n是不是此最大的幂的约数就行了，
假设参数是整型，那么3的最大的幂的求法为：

int maxPower = (int) Math.pow(3,(int)(Math.log(0x7fffffff)/Math.log(3)));

0x7fffffff是整型最大值(2147483647)，也就是Integer.maxValue()。表达式后面两个对数相处结果为double，要转化为整型。
下一步只要判断n是不是maxPower(1162261467)的约数即可：maxPower其实是3的19次方.

maxPower % n == 0
"""
