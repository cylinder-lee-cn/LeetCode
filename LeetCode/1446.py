"""
给你一个字符串 s ，字符串的「能量」定义为：只包含一种字符的最长非空子字符串的长度。
请你返回字符串的能量。

示例 1：
输入：s = "leetcode"
输出：2
解释：子字符串 "ee" 长度为 2 ，只包含字符 'e' 。

示例 2：
输入：s = "abbcccddddeeeeedcba"
输出：5
解释：子字符串 "eeeee" 长度为 5 ，只包含字符 'e' 。

示例 3：
输入：s = "triplepillooooow"
输出：5

示例 4：
输入：s = "hooraaaaaaaaaaay"
输出：11

示例 5：
输入：s = "tourist"
输出：1

提示：
1 <= s.length <= 500
s 只包含小写英文字母。
"""


class Solution:
    def maxPower(self, s: str) -> int:
        result = 1
        letter = s[0]
        counter = 1
        for c in s[1:]:
            if c == letter:
                counter = counter + 1
                result = max(result, counter)
            else:
                letter = c
                counter = 1
        return result


ss = Solution()
print(ss.maxPower('leetcode'))
print(ss.maxPower('abbcccddddeeeeedcba'))
print(ss.maxPower('triplepillooooow'))
print(ss.maxPower('hooraaaaaaaaaaay'))
print(ss.maxPower('tourist'))

"""
此题解法：
由于是要计算连续相同的字母数量，所以不能使用collections.Counter。
遍历字符串，依次判断字符是否相同，如果相同计数器+1，并且判断是否更新最大值的变量
如果不相同，计数器归1
"""
