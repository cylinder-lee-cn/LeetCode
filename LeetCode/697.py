"""
697. 数组的度

给定一个非空且只包含非负数的整数数组 nums, 数组的度的定义是指数组里任一元素出现频数的最大值。
你的任务是找到与 nums 拥有相同大小的度的最短连续子数组，返回其长度。

示例 1:
输入: [1, 2, 2, 3, 1]
输出: 2
解释:
输入数组的度是2，因为元素1和2的出现频数最大，均为2.
连续子数组里面拥有相同度的有如下所示:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
最短连续子数组[2, 2]的长度为2，所以返回2.

示例 2:
输入: [1,2,2,3,1,4,2]
输出: 6

注意:
nums.length 在1到50,000区间范围内。
nums[i] 是一个在0到49,999范围内的整数。
"""


class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_count = 0
        dict_num = {}
        for i, n in enumerate(nums):
            if (dict_num.get(n) is None):
                dict_num[n] = [1, [i]]
            else:
                dict_num[n][0] = dict_num[n][0] + 1
                dict_num[n][1].append(i)
            max_count = max(dict_num[n][0], max_count)

        return min([
            v[1][-1] - v[1][0] + 1 for v in dict_num.values()
            if v[0] == max_count
        ])


s = Solution()
print(s.findShortestSubArray([1, 2, 2, 3, 1]))
print(s.findShortestSubArray([1, 2, 2, 3, 1, 4, 2]))
"""
此题解法：
* 使用字典来统计每个数字出现的次数以及对应的index，[count，[index，index，index...]]
* 遍历nums，初始一个数字 n：[1，[i]]，每当找到同样的，count+1, 同时append（index）
* 顺便再比较一个count的最大值，存入max_count中
* 最后，遍历字典，根据count==max_count，拿出所有的index，利用 尾-头+1来计算子字符串的长度
* 返回最小的结果即可
"""
