"""
594. 最长和谐子序列
和谐数组是指一个数组里元素的最大值和最小值之间的差别正好是1。
现在，给定一个整数数组，你需要在所有可能的子序列中找到最长的和谐子序列的长度。

示例 1:
输入: [1,3,2,2,5,2,3,7]
输出: 5
原因: 最长的和谐数组是：[3,2,2,2,3].

说明: 输入的数组长度最大不超过20,000.
"""


class Solution:
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        max_len = 0

        for n in nums:
            d[n] = d.get(n, 0) + 1

        for k, v in d.items():
            tmp_v = (d.get(k + 1, 0) + v if (d.get(k + 1, 0) > 0) else 0)
            max_len = max(tmp_v, max_len)

        return max_len


s = Solution()

print(s.findLHS([1, 3, 2, 2, 5, 2, 3, 7]))
print(s.findLHS([1, 1, 1, 1]))
"""
此题解法：
* 首先统计每个数字以及出现的个数，存入字典
* 然后遍历字典的每个数字，找每个数字k 以及 k+1对应的个数，相加后存入max_len中。
* 注意：如果不到k+1 那么合计就应该记为0，即为不存在对应的和谐数组

"""
