"""
453. 最小移动次数使数组元素相等

给定一个长度为 n 的非空整数数组，找到让数组所有元素相等的最小移动次数。每次移动可以使 n - 1 个元素增加 1。

示例:
输入:
[1,2,3]
输出:
3

解释:
只需要3次移动（注意每次移动会增加两个元素的值）：
[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
"""


class Solution:
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_n = min(nums)
        return sum([x - min_n for x in nums])


s = Solution()
print(s.minMoves([1, 2, 3]))
print(s.minMoves([1, 1, 2147483647]))
"""
此题解法：
* 每次移动使n-1个元素加一，直到最大值，倒过来就是每次可使一个元素减一，直到最小值
* 先找到nums中的最小值
* 依次计算最小值和nums中每个元素的差距，累加起来就是总共要移动的次数

网友一句话版本 ：
return sum(nums)- min(nums) * len(nums)
"""
