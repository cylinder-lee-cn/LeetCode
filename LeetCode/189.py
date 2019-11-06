"""
189. 旋转数组

给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。

示例 1:
输入: [1,2,3,4,5,6,7] 和 k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右旋转 1 步: [7,1,2,3,4,5,6]
向右旋转 2 步: [6,7,1,2,3,4,5]
向右旋转 3 步: [5,6,7,1,2,3,4]

示例 2:
输入: [-1,-100,3,99] 和 k = 2
输出: [3,99,-1,-100]
解释:
向右旋转 1 步: [99,-1,-100,3]
向右旋转 2 步: [3,99,-1,-100]

说明:
尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
要求使用空间复杂度为 O(1) 的原地算法。
"""


class Solution:
    def reverse(self, subnums, i, j):
        """
        :type subnus: List[int]
        :type i: int
        :type j: int
        """
        while (i < j):
            subnums[i], subnums[j] = subnums[j], subnums[i]
            i = i + 1
            j = j - 1

    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        k = k % l

        if (k == 0):
            print(nums)
            return

        self.reverse(nums, 0, l - k - 1)
        self.reverse(nums, l - k, l - 1)
        self.reverse(nums, 0, l - 1)

        print(nums)

s = Solution()

s.rotate([1, 2, 3, 4, 5], 1)
s.rotate([1, 2, 3, 4, 5], 2)
s.rotate([1, 2, 3, 4, 5], 3)
s.rotate([1, 2, 3, 4, 5], 4)
s.rotate([1, 2, 3, 4, 5], 5)
s.rotate([1, 2, 3, 4, 5, 6, 7], 3)
"""
标准解法: 三次数组的翻转, 将数组分成0:l-k-1 和 l-k:length-1 两段, 分别翻转两个子数组,
最后再将数组完整的翻转一次.
"""
