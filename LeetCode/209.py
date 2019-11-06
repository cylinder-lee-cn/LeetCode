"""
209. 长度最小的子数组
给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组。
如果不存在符合条件的连续子数组，返回 0。

示例:
输入: s = 7, nums = [2,3,1,2,4,3]
输出: 2
解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。

进阶:
如果你已经完成了O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。
"""


class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, 0
        num_sum = 0
        l_n = len(nums)
        min_len = l_n + 1
        while (left < l_n):
            if (right < l_n and num_sum < s):
                num_sum = num_sum + nums[right]
                right = right + 1
            else:
                num_sum = num_sum - nums[left]
                left = left + 1

            if (num_sum >= s):
                min_len = min(min_len, right - left)

        return min_len if min_len != l_n + 1 else 0


s = Solution()
print(s.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
print(s.minSubArrayLen(11, [1, 2, 3, 4, 5]))
print(s.minSubArrayLen(3, [1, 1]))
"""
此题解法：
* 使用双指针的滑动窗口方法
* 左右两个指针一开始都指向index 0的元素，如果累加和<s，就将右指针的元素累加到num_sum上
  然后向右移动右指针，反之就从累加和中减去左指针的元素，然后将左指针向右移动

* 如果累加和>=s，记录左右指针的间距，放入min_len中（min_len永远保存最小值）
* 最后还要判断一下min_len是否从l_n+1有所变化，如果没有就返回0

官网代码：
class Solution:
    def minSubArrayLen(self, s, nums):
        n = len(nums)
        if (n < 1 or sum(nums) < s):
            return 0

        # 维护一个滑动窗口nums[i,j], nums[i...j] < s
        i = 0
        j = -1
        total = 0
        res = n + 1
        while i <= n-1:
            if (j + 1 < n) and total < s:
                j += 1
                total += nums[j]
            else:
                total -= nums[i]
                i += 1

            if (total >= s):
                res = min(res, j-i+1)
        if res == n+1:
            return 0
        return res
"""
