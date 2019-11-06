"""
34. 在排序数组中查找元素的第一个和最后一个位置

给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

你的算法时间复杂度必须是 O(log n) 级别。

如果数组中不存在目标值，返回 [-1, -1]。

示例 1:
输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]

示例 2:
输入: nums = [5,7,7,8,8,10], target = 6
输出: [-1,-1]
"""


class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        if (not nums or target < nums[0] or target > nums[-1]):
            return [-1, -1]

        left, right = 0, len(nums) - 1

        index = -1

        while (left <= right):
            mid = (left + right) // 2
            if (nums[mid] < target):
                left = mid + 1
            elif (nums[mid] > target):
                right = mid - 1
            else:
                index = mid
                break

        low, high = index, index
        if (index > -1):
            while (low > 0):
                if (nums[low - 1] == target):
                    low = low - 1
                else:
                    break
            while (high < len(nums) - 1):
                if (nums[high + 1] == target):
                    high = high + 1
                else:
                    break

        # print(index)
        return [low, high]


s = Solution()
print(s.searchRange([5, 7, 7, 8, 8, 10], 8))
print(s.searchRange([5, 7, 7, 8, 8, 10], 6))
print(s.searchRange([], 0))
print(s.searchRange([2, 2], 2))
print(s.searchRange([1], 1))

"""
此题解法：
* 由于要求是O(logN)的时间复杂度，所以采用二分法查找。
* 如果找到了这个数字等于target，还需要分别向高、低两端再检索一下，是否有相同的数字。
  这样才能最终确定是否找到了这个数字的开始和结束位置。
"""
