"""
287. 寻找重复数


给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），
可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。

示例 1:
输入: [1,3,4,2,2]
输出: 2

示例 2:
输入: [3,1,3,4,2]
输出: 3

说明：
不能更改原数组（假设数组是只读的）。
只能使用额外的 O(1) 的空间。
时间复杂度小于 O(n2) 。
数组中只有一个重复的数字，但它可能不止重复出现一次。
"""


class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nl = len(nums)
        nlist = [0] * (nl + 1)

        for n in nums:
            if nlist[n] == 1:
                return n
            else:
                nlist[n] = 1


s = Solution()
print(s.findDuplicate([1, 3, 4, 2, 2]))
print(s.findDuplicate([3, 1, 3, 4, 2]))
print(s.findDuplicate([1, 4, 4, 2, 4]))

"""
此题解法：
* 只用O(1)的空间比较费劲
* 用O(n+1)的空间就非常快速和容易了
* 定义一个list长度(n+1)来记录出现的数字，index与n值对应
* 遍历一下nums然后对应看nlist的值即可
"""
