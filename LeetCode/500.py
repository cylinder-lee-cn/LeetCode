"""
500. 键盘行

给定一个单词列表，只返回可以使用在键盘同一行的字母打印出来的单词。键盘如下图所示。

American keyboard

示例1:
输入: ["Hello", "Alaska", "Dad", "Peace"]
输出: ["Alaska", "Dad"]

注意:
你可以重复使用键盘上同一字符。
你可以假设输入的字符串将只包含字母。
"""


class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        s1 = {'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'}
        s2 = {'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'}
        s3 = {'Z', 'X', 'C', 'V', 'B', 'N', 'M'}

        r = []
        for w in words:
            ws = set(w.upper())
            if (ws.issubset(s1) or ws.issubset(s2) or ws.issubset(s3)):
                r.append(w)

        return r


s = Solution()
print(s.findWords(["Hello", "Alaska", "Dad", "Peace"]))
