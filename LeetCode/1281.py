"""
给你一个整数 n，请你帮忙计算并返回该整数「各位数字之积」与「各位数字之和」的差。

示例 1：
输入：n = 234
输出：15
解释：
各位数之积 = 2 * 3 * 4 = 24
各位数之和 = 2 + 3 + 4 = 9
结果 = 24 - 9 = 15

示例 2：
输入：n = 4421
输出：21
解释：
各位数之积 = 4 * 4 * 2 * 1 = 32
各位数之和 = 4 + 4 + 2 + 1 = 11
结果 = 32 - 11 = 21

提示：
1 <= n <= 10^5
"""


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum_result = 0
        mul_result = 1

        while (n != 0):
            n, a = divmod(n, 10)
            sum_result = sum_result+a
            mul_result = mul_result*a

        return mul_result-sum_result


s = Solution()
print(s.subtractProductAndSum(234))
print(s.subtractProductAndSum(4421))
