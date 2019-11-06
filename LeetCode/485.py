"""
485. 最大连续1的个数


给定一个二进制数组， 计算其中最大连续1的个数。

示例 1:
输入: [1,1,0,1,1,1]
输出: 3
解释: 开头的两位和最后的三位都是连续1，所以最大连续1的个数是 3.

注意：
输入的数组只包含 0 和1。
输入数组的长度是正整数，且不超过 10,000。

"""


class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max1 = 0
        count = 0

        for n in nums:
            if (n == 1):
                count = count + 1
            else:
                max1 = max(max1, count)
                count = 0

        return max(max1, count)


s = Solution()
print(s.findMaxConsecutiveOnes([1,0]))
