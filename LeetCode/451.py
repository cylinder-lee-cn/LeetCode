"""
451. 根据字符出现频率排序

给定一个字符串，请将字符串里的字符按照出现的频率降序排列。

示例 1:
输入:
"tree"
输出:
"eert"
解释:
'e'出现两次，'r'和't'都只出现一次。
因此'e'必须出现在'r'和't'之前。此外，"eetr"也是一个有效的答案。

示例 2:
输入:
"cccaaa"
输出:
"cccaaa"
解释:
'c'和'a'都出现三次。此外，"aaaccc"也是有效的答案。
注意"cacaca"是不正确的，因为相同的字母必须放在一起。

示例 3:
输入:
"Aabb"
输出:
"bbAa"
解释:
此外，"bbaA"也是一个有效的答案，但"Aabb"是不正确的。
注意'A'和'a'被认为是两种不同的字符。
"""


class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """

        d = {}
        for c in s:
            d[c] = d.get(c, 0) + 1

        return ''.join([
            x[0] * x[1]
            for x in sorted(d.items(), key=lambda d: d[1], reverse=True)
        ])


s = Solution()
print(s.frequencySort('tree'))
print(s.frequencySort('cccaaa'))
print(s.frequencySort('Aabb'))
"""
此题解法：
* 统计每个字母出现的个数
* 根据字母的个数进行排序（递减）
* 排序完成后，再拼接成 字母×次数 的模式

一句话版本：
 return ''.join(c*-n for n,c in sorted((-s.count(c),c) for c in set(s)))

这里巧妙的使用了负数来进行逆序的排列，
"""
