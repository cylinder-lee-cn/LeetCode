"""
169. 求众数

给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
你可以假设数组是非空的，并且给定的数组总是存在众数。

示例 1:
输入: [3,2,3]
输出: 3

示例 2:
输入: [2,2,1,1,1,2,2]
输出: 2
"""


class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # ss = set(nums)
        # l = len(nums) / 2
        # for s in ss:
        #     nl = nums.count(s)
        #     if (nl > l):
        #         return s

        # import collections

        # numsLen = len(nums) / 2

        # numsDict = collections.Counter(nums)

        # for k, v in numsDict.items():
        #     if v > numsLen:
        #         return k

        m, count = 0, 0

        for v in nums:
            if count == 0:
                m, count = v, 1
            elif m == v:
                count = count + 1
            else:
                count = count - 1
        return m


s = Solution()
print(s.majorityElement([3, 2, 3]))
print(s.majorityElement([2, 2, 1, 1, 1, 2, 2]))

"""
此题解法：
* 摩尔投票法：
* 数组中超过半数的元素，只会有一个，因为如果有个元素超过半数了，那剩下的肯定小于半数
* 备选元素m=0 是数组的首个元素，计数器count=1
* 遍历nums，当计数器=0时，将当前元素给m，并且计数器+1
* 当计数器不是1时，比较m和v，如果相等，那么计数器+1，如果不相等计数器-1
* 超过半数的元素在过程中会被不断的被其它的元素消耗掉，但是消耗不完。
"""
