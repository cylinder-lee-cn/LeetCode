"""
15. 三数之和

给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，
使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""


class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        num_count = {}
        result = []

        for n in nums:
            num_count[n] = num_count.get(n, 0) + 1

        if num_count.get(0, 0) >= 3:
            result.append([0, 0, 0])

        positive = [n for n in num_count.keys() if n >= 0]
        negative = [n for n in num_count.keys() if n < 0]

        for p in positive:
            for n in negative:
                diff = 0 - p - n
                if diff in num_count:
                    if diff in (p, n) and num_count[diff] >= 2:
                        result.append([n, p, diff])
                    elif diff < n or diff > p:
                        result.append([n, p, diff])
        return result


s = Solution()
print(s.threeSum([-1, 0, 1, 2, -1, -4]))
"""
此题解法：
* 首先统计nums中每个数字以及对应的次数
* 如果num_count中有超过3个0，那么一定有[0，0，0]
* 然后将nums拆分成>=0和小于0的两个数组
* n+p+diff==0 所以 diff=0-n-p
* 判断diff是否在num_count中，如果存在，就继续判断特例：
    1. diff是否与n or p相同，如果相同，那么diff在num_count的计数必须>=2
    2. 如果不相同，就巧妙的利用大小关系进行排重，因为 n < p 所以，仅保存 diff< n or diff>p的情况
"""
