"""
35. 搜索插入位置

给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
你可以假设数组中无重复元素。

示例 1:
输入: [1,3,5,6], 5
输出: 2

示例 2:
输入: [1,3,5,6], 2
输出: 1

示例 3:
输入: [1,3,5,6], 7
输出: 4

示例 4:
输入: [1,3,5,6], 0
输出: 0
"""


class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        l = len(nums)

        for i in range(l - 1, -1, -1):
            if (nums[i] == target):
                return i
            elif (nums[i] < target):
                return i + 1
            elif (i == 0 and nums[i] > target):
                return 0


s = Solution()
print(s.searchInsert([1, 3, 5, 6], 5))
print(s.searchInsert([1, 3, 5, 6], 2))
print(s.searchInsert([1, 3, 5, 6], 7))
print(s.searchInsert([1, 3, 5, 6], 0))

"""
解法:此题和27题类似,也是反向遍历List, 逐个和target的值进行比较,只需要遍历一次List就可以完成
* 如果list[i]的值与target相同,说明找到目标,返回当前索引值i
* 如果list[i]的值比target小,说明无相同,需要插入在list[i]的后面,返回当前索引值+1(i+1)
* 如果当前索引已经到0,而且list[i]还比target大,说明应该将target插入到list最前面,故此返回0
"""