"""
167. 两数之和 II - 输入有序数组

给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。
函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。

说明:
返回的下标值（index1 和 index2）不是从零开始的。
你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。

示例:
输入: numbers = [2, 7, 11, 15], target = 9
输出: [1,2]
解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。
"""


class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i in range(len(numbers)):
            b = target - numbers[i]
            if b in d:
                return (d.get(b) + 1, i + 1)
            else:
                d[numbers[i]] = i


s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))
"""
此题解法: 现在是使用了第一题的解法. 效果也还行. 但是这题中强调了是'升序排列'的有序数组.
依据'升序排列'有序数组这一关键条件. 最有效的解法是:
1. 取数组一头(index 0)一尾(index len(numbers)-1)的两个数字相加, 和sum与target比较
2. 如果sum>target 说明多了, 那么取个第二大的数,也就是 index len(numbers)-2, 依次继续比较
3. 如果sum< target 说明小了, 那么要取index(1), 如果还小就继续取
4. 如果相等那就获取到两个数的index
"""
