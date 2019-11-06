"""
78. 子集

给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:
输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""

import itertools


class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [nums]
        for i in range(len(nums)):
            result.extend([list(x) for x in itertools.combinations(nums, i)])
            print(result)

        return result


s = Solution()
s.subsets([1, 2, 3])

"""
此题解法：
* 投机取巧的使用了Python的itertools库，使用combinations方法来提供元素的组合
"""
