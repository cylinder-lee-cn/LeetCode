"""
581. 最短无序连续子数组

给定一个整数数组，你需要寻找一个连续的子数组，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。

你找到的子数组应是最短的，请输出它的长度。

示例 1:

输入: [2, 6, 4, 8, 10, 9, 15]
输出: 5
解释: 你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。
说明 :

输入的数组长度范围在 [1, 10,000]。
输入的数组可能包含重复元素 ，所以升序的意思是<=。

"""


class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        new_nums = sorted(nums)
        lp, rp = 0, len(nums) - 1

        if (nums == new_nums):
            return 0

        while 1:
            if (new_nums[lp] == nums[lp]):
                lp = lp + 1
            else:
                print(lp)
                break
        while 1:
            if (new_nums[rp] == nums[rp]):
                rp = rp - 1
            else:
                print(rp)
                break

        return (rp - lp + 1)


s = Solution()
print(s.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))
"""
此题解法：将原数组排序，然后对比排序后数组和原数组，分别从左右两端进行比较
* 从左边找到第一个不相同元素的索引
* 再从右边找到第一个不相同元素的索引
* 这两个索引中间就是需要被排序的连续子数组。
* 通过两个索引计算子数组的长度。
"""
