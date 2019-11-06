"""
1002. 查找常用字符

给定仅有小写字母组成的字符串数组 A，返回列表中的每个字符串中都显示的全部字符（包括重复字符）组成的列表。
例如，如果一个字符在每个字符串中出现 3 次，但不是 4 次，则需要在最终答案中包含该字符 3 次。

你可以按任意顺序返回答案。

示例 1：
输入：["bella","label","roller"]
输出：["e","l","l"]

示例 2：
输入：["cool","lock","cook"]
输出：["c","o"]

提示：
1 <= A.length <= 100
1 <= A[i].length <= 100
A[i][j] 是小写字母
"""


class Solution:
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        result = ''
        al = len(A)
        amap = [[0] * al for _ in range(26)]
        # print(amap)
        for idx, word in enumerate(A):
            for c in word:
                amap[ord(c) - 97][idx] = amap[ord(c) - 97][idx] + 1

        for idx, item in enumerate(amap):
            if all(c > 0 for c in amap[idx]):
                result = result + chr(97 + idx) * min(amap[idx])
        return list(result)


s = Solution()
print(s.commonChars(["bella", "label", "roller"]))
# print('-' * 10)
print(s.commonChars(["cool", "lock", "cook"]))
