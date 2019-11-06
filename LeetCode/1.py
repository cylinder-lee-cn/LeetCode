"""
1. 两数之和
给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。
你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。

示例:
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

"""


class Solution:
    def twosum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i in range(len(nums)):
            b = target - nums[i]
            if b in d:
                return (d.get(b), i)
            else:
                d[nums[i]] = i


d = Solution()
print(d.twosum([3, 3], 6))
print(d.twosum([2, 7, 11, 15], 9))
"""
解题思路(最优解,方法参考官网,时间复杂度O(n),空间复杂度O(n)):
只遍历一次列表,利用HashMap(Python的字典dict实际上是HashMap)的快速查找进行定位.

* 建立一个空的字典d
* 顺序取list中的一个元素
* 用减法计算对应的减数
* 在字典中查找是否有这个减数的key
* 如果没有,就将此减数和list中对应序号作为字典的key和value加入字典
* 如果找到,终止查找,返回字典中此key对应的value和当前list的序号
"""
