"""
47. 全排列 II

给定一个可包含重复数字的序列，返回所有不重复的全排列。

示例:
输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""

import itertools


class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        p = set()
        for n in itertools.permutations(nums):
            p.add(n)

        return [list(x) for x in p]


s = Solution()
print(s.permuteUnique([1, 1, 2]))

"""
此题解法：
* 使用了itertools.permutations来提供所有的‘排列’
* 然后使用一个set来去重
"""
