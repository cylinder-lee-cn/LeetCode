"""
347. 前K个高频元素


给定一个非空的整数数组，返回其中出现频率前 k 高的元素。

示例 1:
输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]

示例 2:
输入: nums = [1], k = 1
输出: [1]

说明：
你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。
你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。
"""


class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # d = {n: nums.count(n) for n in nums}
        # return [
        #     sorted(d.items(), key=lambda d: d[1], reverse=True)[i][0]
        #     for i in range(k)
        # ]
        from collections import Counter
        return [item[0] for item in Counter(nums).most_common(k)]


s = Solution()
print(s.topKFrequent([1, 1, 1, 2, 2, 3], 2))
print(s.topKFrequent([1], 1))
print(s.topKFrequent([1, 2], 2))
"""
此题解法：
* 首先统计每个元素出现的次数，放入字典，key是数字，value是次数
* 根据value次数降序排列，取前K个即可
* 可以直接使用collections的Conter的most_common方法，取到values最大的k个元素
"""
