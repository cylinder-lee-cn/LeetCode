"""
540. 有序数组中的单一元素


给定一个只包含整数的有序数组，每个元素都会出现两次，唯有一个数只会出现一次，找出这个数。

示例 1:
输入: [1,1,2,3,3,4,4,8,8]
输出: 2

示例 2:
输入: [3,3,7,7,10,11,11]
输出: 10
注意: 您的方案应该在 O(log n)时间复杂度和 O(1)空间复杂度中运行。
"""


class Solution:
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        t = nums[0]
        for i in range(1, len(nums)):
            t = t ^ nums[i]
        return t


"""
此题解法：
* 利用xor的运算，两个相同数字的xor计算结果是0，0与任何数字的xor结果还是原来的数字
"""
