"""
888. 两句话中的不常见单词
用户通过次数 213
用户尝试次数 235
通过次数 220
提交次数 448
题目难度 Easy

给定两个句子 A 和 B 。 （句子是一串由空格分隔的单词。每个单词仅由小写字母组成。）
如果一个单词在其中一个句子中只出现一次，在另一个句子中却没有出现，那么这个单词就是不常见的。
返回所有不常用单词的列表。
您可以按任何顺序返回列表。

示例 1：
输入：A = "this apple is sweet", B = "this apple is sour"
输出：["sweet","sour"]

示例 2：
输入：A = "apple apple", B = "banana"
输出：["banana"]

提示：
0 <= A.length <= 200
0 <= B.length <= 200
A 和 B 都只包含空格和小写字母。
"""


class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        d = {}
        strs = []
        AL = A.split(' ')
        BL = B.split(' ')

        for i in range(len(AL)):
            c = AL[i]
            if d.get(c):
                d[c] = d[c] + 1
            else:
                d[c] = 1

        for j in range(len(BL)):
            c = BL[j]
            if d.get(c):
                d[c] = d[c] + 1
            else:
                d[c] = 1

        for k, v in d.items():
            if v == 1:
                strs.append(k)

        return strs


S = Solution()
print(S.uncommonFromSentences('this apple is sweet', 'this apple is sour'))
