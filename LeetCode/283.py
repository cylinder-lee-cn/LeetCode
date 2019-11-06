"""
283. 移动零

给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:
输入: [0,1,0,3,12]
输出: [1,3,12,0,0]

说明:
必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。
"""


class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = 0
        for i, num in enumerate(nums):
            if (num != 0):
                if (i != k):
                    nums[i], nums[k] = nums[k], nums[i]
                k = k + 1
        # print(nums)
        return


s = Solution()
s.moveZeroes([0, 1, 7, 13, 2])
"""
此题解法：不断的将0和非零的元素交换位置
"""
