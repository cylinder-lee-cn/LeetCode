"""
724. 寻找数组的中心索引

给定一个整数类型的数组 nums，请编写一个能够返回数组“中心索引”的方法。
我们是这样定义数组中心索引的：数组中心索引的左侧所有元素相加的和等于右侧所有元素相加的和。
如果数组不存在中心索引，那么我们应该返回 -1。如果数组有多个中心索引，那么我们应该返回最靠近左边的那一个。

示例 1:
输入:
nums = [1, 7, 3, 6, 5, 6]
输出: 3
解释:
索引3 (nums[3] = 6) 的左侧数之和(1 + 7 + 3 = 11)，与右侧数之和(5 + 6 = 11)相等。
同时, 3 也是第一个符合要求的中心索引。

示例 2:
输入:
nums = [1, 2, 3]
输出: -1
解释:
数组中不存在满足此条件的中心索引。

说明:
nums 的长度范围为 [0, 10000]。
任何一个 nums[i] 将会是一个范围在 [-1000, 1000]的整数。
"""


class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ln = len(nums)
        left, right = 0, sum(nums)

        for i in range(ln):
            right = right - nums[i]
            if (left == right):
                return i
            left = left + nums[i]
        return -1


s = Solution()
print(s.pivotIndex([1, 2, 3]))
print(s.pivotIndex([1, 7, 3, 6, 5, 6]))
print(s.pivotIndex([-1, -1, -1, 0, 1, 1]))
print(s.pivotIndex([-1, -1, 0, 1, 1, 0]))
print(s.pivotIndex([]))
"""
此题解法：一种是分别计算左右两边元素的和（左边初始是0，右边是sum（nums））
然后遍历nums，用右边先减去nums[i]和左边进行比较，如果相同就得知i
否则就left+nums[i]，重复。

还一种解法是计算总和的方式：如果左边=右边，那么：左边+右边+nums[i]=sum（nums）
也就是 左边×2+nums[i]=sum（nums）

total=sum(nums)
left=0
for i in range(len(nums)):
    if (left*2)+nums[i]==total):
        return i
    else:
        left=left+nums[i]
return -1
"""
