"""
66. 加一

给定一个非负整数组成的非空数组，在该数的基础上加一，返回一个新的数组。

最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

示例 1:
输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。

示例 2:
输入: [4,3,2,1]
输出: [4,3,2,2]
解释: 输入数组表示数字 4321。
"""


class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        l = len(digits)
        addone = 1

        for i in range(l - 1, -1, -1):
            t = digits[i]
            t = t + addone
            if (t == 10):
                t = 0
                addone = 1
            else:
                addone = 0

            digits[i] = t

            if (i == 0 and t == 0):
                digits[0] = 1
                digits.append(0)

        return digits


s = Solution()
print(s.plusOne([1, 2, 9]))
print(s.plusOne([1, 2, 3]))
print(s.plusOne([9]))
print(s.plusOne([6]))
print(s.plusOne([0]))
print(s.plusOne([1, 9]))
print(s.plusOne([1, 9, 9]))
print(s.plusOne([9, 9, 9, 9]))

"""
此题解法, 使用最原始的进位加1方式,只遍历数列一次
* 默认要加1,因此addone=1
* 反向依次读取数列,将获取元素=元素+addone,如果等于10(此元素置为0),那么需要进位,addone继续为1, 反之无需进位addone=0
* 如果加到最后一个元素(最高位)也等于10,那么就需要将最高位置为1,并且在末尾补0
"""
