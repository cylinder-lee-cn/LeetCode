"""
46. 全排列

给定一个没有重复数字的序列，返回其所有可能的全排列。

示例:
输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""

import itertools


class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return [list(x) for x in itertools.permutations(nums)]


s = Solution()
print(s.permute([1, 2, 3]))

"""
此题解法：
* 使用了itertools.permutations来提供 排列
"""
