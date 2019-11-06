"""
917. 仅仅反转字母

给定一个字符串 S，返回 “反转后的” 字符串，其中不是字母的字符都保留在原地，而所有字母的位置发生反转。

示例 1：
输入："ab-cd"
输出："dc-ba"

示例 2：
输入："a-bC-dEf-ghIj"
输出："j-Ih-gfE-dCba"

示例 3：
输入："Test1ng-Leet=code-Q!"
输出："Qedo1ct-eeLg=ntse-T!"

提示：
S.length <= 100
33 <= S[i].ASCIIcode <= 122
S 中不包含 \ or "
"""


class Solution:
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        SS = list(S)
        i = 0
        j = len(S) - 1
        while (i < j):
            left = S[i]
            right = S[j]
            if not left.isalpha():
                i = i + 1
                continue
            if not right.isalpha():
                j = j - 1
                continue
            if (left.isalpha() and right.isalpha()):
                SS[i], SS[j] = right, left
            i = i + 1
            j = j - 1
        return ''.join(SS)


s = Solution()
print(s.reverseOnlyLetters('ab-cd'))
print(s.reverseOnlyLetters('a-bC-dEf-ghIj'))
print(s.reverseOnlyLetters('Test1ng-Leet=code-Q!'))
print(s.reverseOnlyLetters(''))

"""
此题解法：使用双指针来进行字符串（仅仅是字母的翻转），一个从头取，一个从尾取，如果其中一个不是字母，将指针指向下一个。跳到下次循环。
如果两个字符都是字母，那就交换位置。交换完成后，头尾指针均指向下一个。
"""
