"""
345. 反转字符串中的元音字母

编写一个函数，以字符串作为输入，反转该字符串中的元音字母。

示例 1:

输入: "hello"
输出: "holle"
示例 2:

输入: "leetcode"
输出: "leotcede"
说明:
元音字母不包含字母"y"。

"""


class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        # 从s中选出所有元音作为一个List
        vs = [c for c in s if c in vowels]

        r = ''.join([c if c not in vowels else vs.pop() for c in s])

        return r


"""
此题说明，整个字符串中的元音字母（a e i o u）作为一个串进行翻转，比如在leetcode中，元音串是eeoe，翻转后是eoee。
标准解法：双指针，一个从头看，一个从尾看，如果是都是元音字母就交换两个元素的位置，直到指针相遇（位置相同）

更Pythonic的做法见上方代码
"""

s = Solution()
print(s.reverseVowels('leetcode'))
