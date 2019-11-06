"""
162. 寻找峰值

峰值元素是指其值大于左右相邻值的元素。
给定一个输入数组 nums，其中 nums[i] ≠ nums[i+1]，找到峰值元素并返回其索引。
数组可能包含多个峰值，在这种情况下，返回任何一个峰值所在位置即可。

你可以假设 nums[-1] = nums[n] = -∞。

示例 1:
输入: nums = [1,2,3,1]
输出: 2
解释: 3 是峰值元素，你的函数应该返回其索引 2。

示例 2:
输入: nums = [1,2,1,3,5,6,4]
输出: 1 或 5

解释: 你的函数可以返回索引 1，其峰值元素为 2；
     或者返回索引 5， 其峰值元素为 6。
说明:
你的解法应该是 O(logN) 时间复杂度的。
"""


class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # nl = len(nums)
        result = nums.index(max(nums))

        # for i in range(1, nl - 1):
        #     if nums[i - 1] < nums[i] and nums[i] > nums[i + 1]:
        #         return i
        return result


s = Solution()
print(s.findPeakElement([1, 2, 3, 1]))
print(s.findPeakElement([1, 2, 1, 3, 5, 6, 4]))
print(s.findPeakElement(list(range(10))))
"""
此题解法：
* 此题设计的有Bug，题目要求是‘峰值元素是指其值大于左右相邻值的元素’，所以按道理递增或递减数列的最大值应该不是峰值
* 同样数量<=2的数列也应该没有峰值，应该3个元素起
* 所以如果偷懒的做法就是这个数列中最大值一定是峰值，nums.index(max(nums))
* 那标准做法是：
    nl=len(nums)
    if nl<=2:
        return None

    for i in range(1,nl-1):
        if nums[i-1]<nums[i] and nums[i]>nums[i+1]:
            return i
    return None
"""
