"""
448. 找到所有数组中消失的数字

给定一个范围在  1 ≤ a[i] ≤ n ( n = 数组大小 ) 的 整型数组，数组中的元素一些出现了两次，另一些只出现一次。
找到所有在 [1, n] 范围之间没有出现在数组中的数字。
您能在不使用额外空间且时间复杂度为O(n)的情况下完成这个任务吗? 你可以假定返回的数组不算在额外空间内。

示例:
输入:
[4,3,2,7,8,2,3,1]
输出:
[5,6]
"""


class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ln = len(nums)
        result = []
        for i in range(ln):
            idx = abs(nums[i]) - 1
            if (nums[idx] > 0):
                nums[idx] = -nums[idx]

        for i in range(ln):
            if (nums[i] > 0):
                result.append(i + 1)

        return result


s = Solution()
print(s.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))
"""
此题解法：要求只遍历一次，而且不使用额外的空间。
* 如果使用额外空间的话很容易，利用一个set存放（1-n）的值，然后遍历一下nums，检查是否在set内既可。
* 但是不允许使用额外的空间，所以此题的要点在 1 ≤ a[i] ≤ n ( n = 数组大小 )
  数组中的元素一些出现了两次，另一些只出现一次。
* 也就是说数组长度为n，数组中最大值<=n，换句话说：数组元素的值其实就是数组索引的值。
* 如果不缺失数字，那么数组元素和值是1-1对应的
* 看例子[4,3,2,7,8,2,3,1]，共8个元素，如果不缺失那么元素的值唯一而不重复并且对应索引。
* 现在是（index-value）0-4 1-3 2-2 3-7 4-8 5-2 6-3 7-1，其中index（2，5）均指向2，
  index（1-6）均指向3。如果将value对应的index求负，那么index（5，6）就还是正数。
  这样再遍历一次数组就知道value是正数的索引值就是缺失的数字.应该属于抽屉原理。
"""
