"""
面试题 01.06. 字符串压缩
字符串压缩。利用字符重复出现的次数，编写一种方法，实现基本的字符串压缩功能。
比如，字符串aabcccccaaa会变为a2b1c5a3。若“压缩”后的字符串没有变短，则返回原先的字符串。
你可以假设字符串中只包含大小写英文字母（a至z）。

示例1:
 输入："aabcccccaaa"
 输出："a2b1c5a3"

示例2:
 输入："abbccd"
 输出："abbccd"
 解释："abbccd"压缩后为"a1b2c2d1"，比原字符串长度更长。

提示：
字符串长度在[0, 50000]范围内。
"""


class Solution:
    def compressString(self, S: str) -> str:
        lenS = len(S)
        if lenS <= 2:
            return S

        tmp = S[0]
        count = 0
        result = []

        for s in S:
            if s == tmp:
                count = count+1
            else:
                result.append(tmp)
                result.append(count)
                tmp = s
                count = 1
        result.append(tmp)
        result.append(count)

        if len(result) < lenS:
            return ''.join([str(x) for x in result])
        else:
            return S


s = Solution()
print(s.compressString('aabcccccaa'))
print(s.compressString('abbcccccccccd'))
print(s.compressString('abbcccc'))
"""
此题解法:
* 遍历字符串，先取第一个元素作为标准，从第一个进行判断，如果和标准相同，那么计数器+1
* 如果不相同，就将当前tmp和计数器的值放入list中，再将当前的元素作为标准，计数器置1
* 全部遍历完后，将最后未入list的tmp和计数器都加入list即可
* 最后比较一下list的长度与原字符串的长度，返回短的那个
* 由于使用了List，所以内存消耗比较高
"""
