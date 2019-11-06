"""
704. 二分查找

给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，
写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。

示例 1:
输入: nums = [-1,0,3,5,9,12], target = 9
输出: 4
解释: 9 出现在 nums 中并且下标为 4

示例 2:
输入: nums = [-1,0,3,5,9,12], target = 2
输出: -1
解释: 2 不存在 nums 中因此返回 -1
 
提示：
你可以假设 nums 中的所有元素是不重复的。
n 将在 [1, 10000]之间。
nums 的每个元素都将在 [-9999, 9999]之间。
"""


class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        r_index = 0

        try:
            r_index = nums.index(target)
        except:
            r_index = -1

        return r_index


s = Solution()
print(s.search([-1, 0, 3, 5, 9, 12], 2))
print(s.search([-1, 0, 3, 5, 9, 12], 9))


"""
此题解法：
未采用题目要求的二分法查找，而是利用了异常处理的方式，如果查到了就返回正常的index值，如果异常就说明没找到，
返回-1
"""