"""
423. 从英文中重建数字


给定一个非空字符串，其中包含字母顺序打乱的英文单词表示的数字0-9。按升序输出原始的数字。

注意:
输入只包含小写英文字母。
输入保证合法并可以转换为原始的数字，这意味着像 "abc" 或 "zerone" 的输入是不允许的。
输入字符串的长度小于 50,000。

示例 1:
输入: "owoztneoer"
输出: "012" (zeroonetwo)

示例 2:
输入: "fviefuro"
输出: "45" (fourfive)
"""


class Solution:
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """

        d_en = {}
        result = []
        t = 0
        for n in s:
            d_en[n] = d_en.get(n, 0) + 1

        t = d_en.get('z', 0)
        if t > 0:
            result.append('0' * t)
            for m in 'zero':
                d_en[m] = d_en[m] - t

        t = d_en.get('w', 0)
        if t > 0:
            result.append('2' * t)
            for m in 'two':
                d_en[m] = d_en[m] - t

        t = d_en.get('u', 0)
        if t > 0:
            result.append('4' * t)
            for m in 'four':
                d_en[m] = d_en[m] - t

        t = d_en.get('x', 0)
        if t > 0:
            result.append('6' * t)
            for m in 'six':
                d_en[m] = d_en[m] - t

        t = d_en.get('g', 0)
        if t > 0:
            result.append('8' * t)
            for m in 'eight':
                d_en[m] = d_en[m] - t

        t = d_en.get('o', 0)
        if t > 0:
            result.append('1' * t)
            for m in 'one':
                d_en[m] = d_en[m] - t

        t = d_en.get('r', 0)
        if t > 0:
            result.append('3' * t)
            for m in 'tree':
                d_en[m] = d_en[m] - t

        t = d_en.get('f', 0)
        if t > 0:
            result.append('5' * t)
            for m in 'five':
                d_en[m] = d_en[m] - t

        t = d_en.get('s', 0)
        if t > 0:
            result.append('7' * t)
            for m in 'seven':
                d_en[m] = d_en[m] - t

        t = d_en.get('i', 0)
        if t > 0:
            result.append('9' * t)
            for m in 'nine':
                d_en[m] = d_en[m] - t

        # print(d_en)
        # print(result)
        return ''.join(sorted(result))


s = Solution()
print(s.originalDigits('zeroonetwo'))
print(s.originalDigits('fourfive'))
"""
此题解法：
* 通过统计发现，0 2 4 6 8 分别对应唯一的字母 z w u x g
* 如果筛选出如上的偶数，那么根据统计又可以发现
* 1->o 3->r or t 5->f or v 7->s 9->i

"""
