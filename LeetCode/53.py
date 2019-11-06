"""
53. 最大子序和

给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:
输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

进阶:
如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
"""


class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)

        thesum = 0
        maxsum = nums[0]

        for i in range(l):
            thesum = thesum + nums[i]
            if (maxsum < thesum):
                maxsum = thesum
            if (thesum < 0):
                thesum = 0

        return maxsum


s = Solution()

print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

"""
解法, 没采用提示的分治法,而采用了动态规划法(参考自网上)

* 设定maxsum为数列的第一个nums[0], 当前数列累加和为thesum=0
* 然后依次读取数列中的每一个数字,将其与thesum相加.
* 如果maxsum<thesum,那么将thesum的值赋予maxsum
* 如果thesum值为负,那么意味着再加下一位数字的和一定会比那位数字小,说明当前数列累加测试结束,将thesum置0
  然后继续后续的数列测试.
* 整个过程这个数列只需要遍历读取一次,不需要额外的存储空间.效率最高
"""
