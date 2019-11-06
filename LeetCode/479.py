"""
479. 最大回文数乘积

你需要找到由两个 n 位数的乘积组成的最大回文数。
由于结果会很大，你只需返回最大回文数 mod 1337得到的结果。

示例:
输入: 2
输出: 987

解释: 99 x 91 = 9009, 9009 % 1337 = 987

说明:
n 的取值范围为 [1,8]。
"""


class Solution:
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        if (n == 1):
            return 9

        up = 10**n - 1
        low = 10**(n - 1)
        # max_n = up * up

        for i in range(up, low, -1):
            left = str(i)
            num_str = left + left[::-1]
            num = int(num_str)
            j = up
            while (j * j > num):
                if (num % j == 0):
                    return (i, j, num, num % 1337)
                else:
                    j = j - 1
        # r = [9, 987, 123, 597, 677, 1218, 877, 475]
        # return r[n - 1]


s = Solution()
print(s.largestPalindrome(2))
print(s.largestPalindrome(3))
print(s.largestPalindrome(4))
print(s.largestPalindrome(5))
print(s.largestPalindrome(6))
print(s.largestPalindrome(7))
print(s.largestPalindrome(8))

# [987, 123, 597, 677, 1218, 877, 475]
"""
此题解法：
* n位数乘n位数的积一定是2n位，所以可以利用这个特征来构造回文数
* n位数最大就是10^n-1,最小是10^(n-1)
* 因为最大的回文数，所以从最大的n位数倒着取，比如n=2时从99取，回文数是9999，98时是9889.利用字符串的反转
* 取到回文数后就要开始验证是否能被两位数整除，也得从最大的up开始
"""
