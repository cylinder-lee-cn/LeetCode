"""
384. 打乱数组

打乱一个没有重复元素的数组。

示例:
// 以数字集合 1, 2 和 3 初始化数组。
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

// 打乱数组 [1,2,3] 并返回结果。任何 [1,2,3]的排列返回的概率应该相同。
solution.shuffle();

// 重设数组到它的初始状态[1,2,3]。
solution.reset();

// 随机返回数组[1,2,3]打乱后的结果。
solution.shuffle();
"""

import random


class Solution:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.old = list(nums)
        self.nums = list(nums)

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.old

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        random.shuffle(self.nums)
        return self.nums


# Your Solution object will be instantiated and called as such:
obj = Solution({1, 2, 3})
param_2 = obj.shuffle()
param_1 = obj.reset()
print(param_1)
print(param_2)
"""
此题解法：
* 主要考察随机数的使用。
* 一个数组的“均匀打乱”，比较好的是使用“Fisher-Yates shuffle”算法。
-- To shuffle an array a of n elements (indices 0..n-1):
for i from n−1 downto 1 do
     j ← random integer such that 0 ≤ j ≤ i
     exchange a[j] and a[i]
"""
