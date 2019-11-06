"""
268. 缺失数字

给定一个包含 0, 1, 2, ..., n 中 n 个数的序列，找出 0 .. n 中没有出现在序列中的那个数。

示例 1:
输入: [3,0,1]
输出: 2

示例 2:
输入: [9,6,4,2,3,5,7,0,1]
输出: 8

说明:
你的算法应具有线性时间复杂度。你能否仅使用额外常数空间来实现?
"""


class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = sum(nums)
        n = len(nums)

        return n * (n + 1) // 2 - a


s = Solution()

print(s.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))
print(s.missingNumber([3, 0, 1]))
print(s.missingNumber([0, 1]))
"""
此题解法（源自网络）：先对整个数组求和（sum（nums）），然后获取数组长度n，由于缺失一个数字，所以完整的数组应该是n+1个数字，
n+1也就是这个数组中元素的最大值。
那数组nums：0+1+2+3+...（n+1个元素）的和就是 n*（n+1）//2 ，将真实的和减去现有的和，就是缺失的数字。
"""
