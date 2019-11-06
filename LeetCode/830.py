import itertools
"""
830. 较大分组的位置

在一个由小写字母构成的字符串 S 中，包含由一些连续的相同字符所构成的分组。
例如，在字符串 S = "abbxxxxzyy" 中，就含有 "a", "bb", "xxxx", "z" 和 "yy" 这样的一些分组。
我们称所有包含大于或等于三个连续字符的分组为较大分组。找到每一个较大分组的起始和终止位置。

最终结果按照字典顺序输出。
示例 1:
输入: "abbxxxxzzy"
输出: [[3,6]]
解释: "xxxx" 是一个起始于 3 且终止于 6 的较大分组。

示例 2:
输入: "abc"
输出: []
解释: "a","b" 和 "c" 均不是符合要求的较大分组。

示例 3:
输入: "abcdddeeeeaabbbcd"
输出: [[3,5],[6,9],[12,14]]
说明:  1 <= S.length <= 1000

"""


class Solution:
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        i = 0
        ls = len(S)
        current = ''
        result = []
        ret = []
        while (i < ls):
            s = S[i]
            if (s != current):
                current = s
                result.append('|')
            result.append(str(i))
            i = i + 1

        a = ','.join(result).split('|')
        # print(a)
        for b in a:
            c = [int(x) for x in b.split(',') if len(x) > 0]
            # print(c)
            if (len(c) >= 3):
                # print(c, min(c), max(c))
                ret.append([c[0], c[-1]])

        return ret


# s = Solution()
# print(s.largeGroupPositions('abcdddeeeeaabbbcd'))
# print(s.largeGroupPositions('abbxxxxzzy'))
# print(s.largeGroupPositions('abc'))
"""
此题解法：如果能使用python内置itertools的groupby就非常容易了。

如下是使用内置模块itertools的做法
* 首先将字符串分组（相同的字母成为一组，从左到右的顺序）
* 将分组转换成List
* 计算每组List的长度，如果>=3就是需要的，记录偏移量（头：0），偏移量（尾:List的长度）
* 如果长度不够，那么仅增加偏移量（List长度）
"""


class SolutionA:
    def largeGroupPositions(self, S):
        result = []
        offset = 0
        for k, group in itertools.groupby(S):
            subS = list(group)
            sl = len(subS)
            if (sl >= 3):
                result.append([offset, offset + sl - 1])
            else:
                offset = offset + sl
        return result


sa = SolutionA()
print(sa.largeGroupPositions('abcdddeeeeaabbbcd'))
print(sa.largeGroupPositions('abbxxxxzzy'))
print(sa.largeGroupPositions('abc'))
