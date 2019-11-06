"""
665. 非递减数列

给定一个长度为 n 的整数数组，你的任务是判断在最多改变 1 个元素的情况下，该数组能否变成一个非递减数列。
我们是这样定义一个非递减数列的： 对于数组中所有的 i (1 <= i < n)，满足 array[i] <= array[i + 1]。

示例 1:
输入: [4,2,3]
输出: True
解释: 你可以通过把第一个4变成1来使得它成为一个非递减数列。

示例 2:
输入: [4,2,1]
输出: False
解释: 你不能在只改变一个元素的情况下将其变为非递减数列。

说明:  n 的范围为 [1, 10,000]。
"""


class Solution:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n_l = len(nums)
        if (n_l < 3):
            return True

        bad = 0
        for i in range(n_l - 1):
            if (nums[i] > nums[i + 1]):
                bad = bad + 1
                if (bad > 1):
                    return False
                if (i > 0 and nums[i + 1] < nums[i - 1]):
                    nums[i + 1] = nums[i]
                else:
                    nums[i] = nums[i + 1]
        return True


s = Solution()
print(s.checkPossibility([4, 2, 3]))
print(s.checkPossibility([4, 2, 1]))
print(s.checkPossibility([-1, 4, 2, 3]))
print(s.checkPossibility([3, 4, 2, 3]))
"""
此题解法：
* 非递减数列，就是 nums[i+1]>=nums[i]
* 那么在现有数列中只允许改变一个元素，意味着有nums[i]>nums[i+1].
* 遍历nums，当出现nums[i]>nums[i+1]时（bad计数+1），可以选择改变nums[i]或者是nums[i+1].
    改变的依据是比较nums[i-1]和nums[i+1]
    * 如果nums[i-1]大，那么就把nums[i+1]置成nums[i]
    * 如果nums[i+1]大，那么就要把nums[i]置成nums[i+1]
* 如果bad>1那么就False，反之True
"""
