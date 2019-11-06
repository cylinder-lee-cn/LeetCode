"""
179. 最大数

给定一组非负整数，重新排列它们的顺序使之组成一个最大的整数。

示例 1:
输入: [10,2]
输出: 210

示例 2:
输入: [3,30,34,5,9]
输出: 9534330
说明: 输出结果可能非常大，所以你需要返回一个字符串而不是整数。

"""


class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        import functools

        result = ''

        strnums = [str(n) for n in nums]

        def acmp(a, b):
            if a + b > b + a:
                return 1
            else:
                return -1

        result = ''.join(
            sorted(strnums, key=functools.cmp_to_key(acmp), reverse=True))

        if result.count('0') == len(result):
            return '0'
        else:
            return result


s = Solution()
print(s.largestNumber([10, 2]))
print(s.largestNumber([3, 30, 34, 5, 9]))
"""
此题解法：
* 首先将数组转成字符串数组。
* 排序的原则是，相邻两个字符串，都要满足 a+b > b+a a要排在b的前面，这样链接起来才会是最大的
* a=3 b=30 a+b=330 b+a=303，所以a要排在b前面
* 由于python3之后sorted函数中没有cmp关键字，所以引入functools包，使用functools.cmp_to_key来自定义排序
* 最后要检查一下是否是全0的情况，如果是，就返回一个0
"""
