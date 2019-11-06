"""
645. 错误的集合

集合 S 包含从1到 n 的整数。不幸的是，因为数据错误，
导致集合里面某一个元素复制了成了集合里面的另外一个元素的值，导致集合丢失了一个整数并且有一个元素重复。

给定一个数组 nums 代表了集合 S 发生错误后的结果。
你的任务是首先寻找到重复出现的整数，再找到丢失的整数，将它们以数组的形式返回。

示例 1:

输入: nums = [1,2,2,4]
输出: [2,3]
注意:

给定数组的长度范围是 [2, 10000]。
给定的数组是无序的。

"""


class Solution:
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        a, b = 0, 0
        l_nums = len(nums)
        d = {i: 0 for i in range(1, l_nums + 1)}

        for n in nums:
            d[n] = d[n] + 1

        for k, v in d.items():
            if (v == 2):
                a = k
            if (v == 0):
                b = k
        return [a, b]


s = Solution()
print(s.findErrorNums([1, 2, 2, 4]))
"""
此题解法：
以上用的是统计法，先生成一个1-n计数为0的字典。然后遍历nums增加字典中对应数字的计数
最后找到计数==2 和计数==0的两个。

现在是纯数学的方法：
* nums的长度就是应该是最大的n，所以标准情况1-n的合计等于 n*(n+1)//2 ：sumCorrect
* 对nums直接求和sum(nums)：sumWithDuplicate
* 将nums放入set中去重，再求和 sum(set(nums)) ：sumMissOne
* sumWithDuplicate-sumMissOne 的差就是那个重复的数字
* sumCorrect-sumMissOne的差就是那个缺失的数字

    max_n=len(nums)
    sumCorrect= n*(n+1)//2
    sumWithDuplicate=sum(nums)
    sumMissOne=sum(set(nums))

    missone=sumWithDuplicate-sumMissOne
    duplicate=sumCorrect-sumMissOne

"""
