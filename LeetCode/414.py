"""
414. 第三大的数

给定一个非空数组，返回此数组中第三大的数。如果不存在，则返回数组中最大的数。要求算法时间复杂度必须是O(n)。

示例 1:
输入: [3, 2, 1]
输出: 1

解释: 第三大的数是 1.

示例 2:
输入: [1, 2]
输出: 2

解释: 第三大的数不存在, 所以返回最大的数 2 .

示例 3:
输入: [2, 2, 3, 1]
输出: 1

解释: 注意，要求返回第三大的数，是指第三大且唯一出现的数。
存在两个值为2的数，它们都排第二。
"""


class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        t = sorted(set(nums))
        if (len(t) >= 3):
            return t[-3]
        else:
            return t[-1]

s=Solution()
print(s.thirdMax([1,2,3]))
print(s.thirdMax([1,2]))
print(s.thirdMax([1,2,2,3]))
print(s.thirdMax([0]))

"""
解题思路: 要求时间复杂度是O(n),也就是这个list只能遍历一次. 采用空间换时间的方式.
将list装入set中,既可以去重又可高效排序. sorted函数对set排序也应该是O(n)
如果排序后set元素数量大于等于3个,那么返回倒数第3个. 反之就返回最大的(最后一个)

"""