"""
334. 递增的三元子序列

给定一个未排序的数组，判断这个数组中是否存在长度为 3 的递增子序列。

数学表达式如下:
如果存在这样的 i, j, k,  且满足 0 ≤ i < j < k ≤ n-1，
使得 arr[i] < arr[j] < arr[k] ，返回 true ; 否则返回 false 。
说明: 要求算法的时间复杂度为 O(n)，空间复杂度为 O(1) 。

示例 1:
输入: [1,2,3,4,5]
输出: true

示例 2:
输入: [5,4,3,2,1]
输出: false
"""


class Solution:
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        n_l = len(nums)
        if (n_l < 3):
            return False

        min_num = 2147483647
        middile_num = 2147483647
        for n in nums:
            if (n < min_num):
                min_num = n
            elif (min_num < n < middile_num):
                middile_num = n
            elif (n > middile_num):
                return True
        return False


s = Solution()
print(s.increasingTriplet([1, 2, 3, 4, 5]))
print(s.increasingTriplet([5, 4, 3, 2, 1]))
"""
此题解法：
* 定义最小，中等两个变量，初始化是2^31-1，最大的32位整数。
* 遍历nums，如果n比min_num小，那么min更新成n
* 如果n 介于 min_num 和 middle_num之间，那么更新middle_num
* 如果发现n>middle_num 说明有3个递增的元素，重要的是这三个元素不是连续的。
"""
