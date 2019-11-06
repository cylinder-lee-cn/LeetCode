"""
220. 存在重复元素 III

给定一个整数数组，判断数组中是否有两个不同的索引 i 和 j，
使得 nums [i] 和 nums [j] 的差的绝对值最大为 t，并且 i 和 j 之间的差的绝对值最大为 ķ。

示例 1:
输入: nums = [1,2,3,1], k = 3, t = 0
输出: true

示例 2:
输入: nums = [1,0,1,1], k = 1, t = 2
输出: true

示例 3:
输入: nums = [1,5,9,1,5,9], k = 2, t = 3
输出: false

"""


class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        nums_k = set()
        for i, n in enumerate(nums):
            if (t == 0):
                if n in nums_k:
                    return True
            else:
                for nk in nums_k:
                    if (abs(n - nk) <= t):
                        return True
            nums_k.add(n)
            if (len(nums_k) == k + 1):
                nums_k.remove(nums[i - k])
        return False


s = Solution()
print(s.containsNearbyAlmostDuplicate([1, 2, 3, 1], 3, 0))

"""
此题解法：
* 首先定义一个set来保存最多k个数字，set可以过滤掉重复的数字，避免重复计算
* 如果t==0，也就是如果有重复数字就能满足要求
* 如果t>0，遍历nums，将数字依次和set中的进行差值计算，如果abs<=t 返回True
  如果>t，将n放入set中。每次都检查set的长度，最大不能超过k+1，如果超过k，就要移除nums[i-k]

"""
