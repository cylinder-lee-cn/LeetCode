"""
187. 重复的DNA序列

所有 DNA 由一系列缩写为 A，C，G 和 T 的核苷酸组成，例如：“ACGAATTCCG”。
在研究 DNA 时，识别 DNA 中的重复序列有时会对研究非常有帮助。

编写一个函数来查找 DNA 分子中所有出现超多一次的10个字母长的序列（子串）。

示例:
输入: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
输出: ["AAAAACCCCC", "CCCCCAAAAA"]
"""


class Solution:
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ds = {}
        sl = len(s)

        result = []
        if sl < 10:
            return []

        for i in range(sl - 10 + 1):
            dna = s[i:i + 10]
            ds[dna] = ds.get(dna, 0) + 1
        print(ds)

        for k, v in ds.items():
            if v >= 2:
                result.append(k)
        return result


s = Solution()
print(s.findRepeatedDnaSequences('AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT'))
"""
此题解法：
* 遍历s，取s[i，i+10]，然后利用字典来判断s的片段是否重复。
* 也可以使用set来判断是否重复

        r, record = set(), set()
        for i in range(len(s)-9):
            tmp = s[i:i+10]
            if tmp not in record:
                record.add(tmp)
            else:
                r.add(tmp)
        return list(r)
"""
