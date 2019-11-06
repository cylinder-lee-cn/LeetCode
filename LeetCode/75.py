"""
75. 颜色分类

给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，
使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

注意:
不能使用代码库中的排序函数来解决这道题。

示例:
输入: [2,0,2,1,1,0]
输出: [0,0,1,1,2,2]

进阶：
一个直观的解决方案是使用计数排序的两趟扫描算法。
首先，迭代计算出0、1 和 2 元素的个数，然后按照0、1、2的排序，重写当前数组。
你能想出一个仅使用常数空间的一趟扫描算法吗？
"""


class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        left, right = -1, len(nums)
        i = 0
        while (i < right):
            if (nums[i] == 1):
                i = i + 1
            elif (nums[i] == 2):
                right = right - 1
                nums[right], nums[i] = nums[i], nums[right]
            else:
                left = left + 1
                nums[left], nums[i] = nums[i], nums[left]
                i = i + 1

        print(nums)


s = Solution()
s.sortColors([2, 0, 2, 1, 1, 0])

"""
此题解法：
* 使用了3指针，最左（指向0），最右（指向2），i是当前元素指针
* 遍历nums，当元素是1时，不做动作，i增1
* 当是2时，换到最右边，并且最右边指针向左挪1
* 当是0时，换到最左边，并且最左指针向右挪一位，同时i增1

"""
