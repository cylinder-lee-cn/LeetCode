"""
1009. 十进制整数的反码

每个非负整数 N 都有其二进制表示。例如， 5 可以被表示为二进制 "101"，11 可以用二进制 "1011" 表示，依此类推。
注意，除 N = 0 外，任何二进制表示中都不含前导零。

二进制的反码表示是将每个 1 改为 0 且每个 0 变为 1。例如，二进制数 "101" 的二进制反码为 "010"。

给定十进制数 N，返回其二进制表示的反码所对应的十进制整数。

示例 1：
输入：5
输出：2
解释：5 的二进制表示为 "101"，其二进制反码为 "010"，也就是十进制中的 2 。

示例 2：
输入：7
输出：0
解释：7 的二进制表示为 "111"，其二进制反码为 "000"，也就是十进制中的 0 。

示例 3：
输入：10
输出：5
解释：10 的二进制表示为 "1010"，其二进制反码为 "0101"，也就是十进制中的 5 。

提示：
0 <= N < 10^9
"""


class Solution(object):
    def bitwiseComplement(self, N):
        """
        :type N: int
        :rtype: int
        """
        # result = ['0b']
        # for n in bin(N)[2:]:
        #     if n == '1':
        #         result.append('0')
        #     else:
        #         result.append('1')

        # return int(''.join(result), 2)

        result = '0b'
        result = result + bin(N)[2:].rjust(32, '1')
        return ~int(result, 2) & 0xffffffff


s = Solution()
print(s.bitwiseComplement(5))
print(s.bitwiseComplement(7))
print(s.bitwiseComplement(10))
"""
此题解法：
一、最简单的就是将数字转成2进制字符串，然后遍历将字符1 \ 0 对调。获取转换后的字符串再转成int

二、用位运算的求反，但是python里都是有符号数
* 先将数字转二进制，然后左侧补1，成字符串
* 再转回数字，利用位运算来获取
"""
